import sys
import queue
import pywinusb.hid as hid

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QTextCursor

from mainwindow import Ui_MainWindow


class Thread(QThread):
    msg_ready = pyqtSignal(list)

    def __init__(self, func):
        super(QThread, self).__init__()
        self.func = func

    def run(self):
        while True:
            msg = []
            items = self.func()
            
            if items:
                for i in items:
                    msg.append(i)

                self.msg_ready.emit(msg)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.current_device  = 0  # 当前设备编号
        self.previous_device = 0  # 之前设备编号

        self.hid_device = None  # 设备

        # self.receive_buff = " "

        self.queue = queue.Queue()  # 创建队列

        self.actionScan.triggered.connect(self.scan)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.about)

        self.device_scan()

        self.open_pushbutton.clicked.connect(self.device_openclose)

        self.thread = Thread(self.queue_monitor)
        self.thread.msg_ready.connect(self.rx_textbrowser_update)
        # self.thread.start()

    def about(self):
        QMessageBox.question(self, 'About', "CP2110 USB-to-UART\r\nVersion: 1.0\r\nAuthor: lgnq", QMessageBox.Ok, QMessageBox.Ok)

    def scan(self):
        print("todo: scan the HID device")
        # self.widget.device_scan()

    def queue_monitor(self):
        if self.queue.qsize():
            try:
                msgs = self.queue.get()
                return msgs

            except queue.Empty:
                pass

    def rx_textbrowser_update(self, item):           
        if (item[0] == 1):
            if (item[1] != 13):
                self.rx_textbrowser.insertPlainText(chr(item[1]))    
                self.rx_textbrowser.moveCursor(QTextCursor.End)

        # if (item[0] == 1):
        #     if (item[1] == 10):
        #         self.rx_textbrowser.append(self.receive_buff)
        #         # self.bar.setValue(self.bar.maximum())
        #         self.receive_buff = ""
        #     elif (item[1] != 13):    
        #         self.receive_buff = self.receive_buff + chr(item[1])

    def report_recv_handler(self, data):
        self.queue.put(data[0:2])

    def device_change(self):
        self.hid_device = self.all_devices[self.device_combobox.currentIndex()]

    def uart_onoff(self, onoff):
        buff = [0x00] * 64
        buff[0] = 0x41  # Report ID = 0x41 Get/Set UART Enable

        if (onoff == 1):
            buff[1] = 0x1  # UART enable
        else:
            buff[1] = 0x0  # UART disable

        self.hid_device.send_feature_report(buff)

    def uart_config(self, baudrate_idx):
        buff = [0x00] * 64
        buff[0] = 0x50  # Report ID = 0x41 Get/Set UART Enable

        if baudrate_idx == 0:  # 9600
            buff[1] = 0x0
            buff[2] = 0x0
            buff[3] = 0x25
            buff[4] = 0x80
        elif baudrate_idx == 1:  # 38400
            buff[1] = 0x0
            buff[2] = 0x0
            buff[3] = 0x96
            buff[4] = 0x00
        elif baudrate_idx == 2:  # 115200
            buff[1] = 0x0
            buff[2] = 0x01
            buff[3] = 0xC2
            buff[4] = 0x00
        else:  # 9600
            buff[1] = 0x0
            buff[2] = 0x0
            buff[3] = 0x25
            buff[4] = 0x80

        buff[5] = 0x0
        buff[6] = 0x0
        buff[7] = 0x3
        buff[8] = 0x0

        self.hid_device.send_feature_report(buff)

    def device_scan(self):
        # self.device_combobox.__init__()

        self.all_devices = hid.HidDeviceFilter(vendor_id=0x10C4, product_id=0xEA80).get_devices()

        for i in self.all_devices:
            id_information = "vId= 0x{0:04X}, pId= 0x{1:04X}, ppId= 0x{2:04X}".format(i.vendor_id, i.product_id, i.parent_instance_id)
            self.device_combobox.addItem(id_information)

        if self.all_devices:
            self.hid_device = self.all_devices[self.device_combobox.currentIndex()]

        self.device_combobox.currentIndexChanged.connect(self.device_change)

        if self.device_combobox.count() == 0:
            self.statusbar.showMessage('no CP2110 device detected')
            
            self.open_pushbutton.setEnabled(False)
            self.clear_pushbutton.setEnabled(False)
            self.baudrate_combobox.setEnabled(False)
        else:
            self.open_pushbutton.setEnabled(True)
            self.clear_pushbutton.setEnabled(True)
            self.baudrate_combobox.setEnabled(True)

    def device_openclose(self):
        if self.hid_device.is_opened():
            self.thread.quit()

            self.hid_device.close()
            self.open_pushbutton.setText("Open")
            self.device_combobox.setEnabled(True)
            self.baudrate_combobox.setEnabled(True)

            self.statusbar.clearMessage()
        else:
            self.thread.start()

            self.hid_device.open()
            self.open_pushbutton.setText("Close")
            self.device_combobox.setEnabled(False)
            self.baudrate_combobox.setEnabled(False)
        
            self.hid_device.set_raw_data_handler(self.report_recv_handler)
            self.feature_report = self.hid_device.find_feature_reports()

            self.uart_onoff(1)
            self.uart_config(self.baudrate_combobox.currentIndex())

            self.statusbar.showMessage('Open ' + self.hid_device.product_name + ' ' + self.hid_device.vendor_name + ' ' + self.hid_device.serial_number)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

