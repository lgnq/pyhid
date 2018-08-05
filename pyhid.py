import sys
import queue
import pywinusb

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from mainwindow import Ui_MainWindow

class Thread(QtCore.QThread):
    msg_ready = QtCore.pyqtSignal(list)

    def __init__(self, func):
        super(QtCore.QThread, self).__init__()
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

        self.actionScan.triggered.connect(self.scan)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.about)

        self.pushButton.clicked.connect(self.openclose)

        # self.thread = Thread(self.queue_monitor)
        # self.thread.msg_ready.connect(self.rx_textbrowser_update)
        # self.thread.start()

    def queue_monitor(self):
        if self.queue.qsize():
            try:
                msgs = self.queue.get()
                return msgs

            except queue.Empty:
                pass

    string = ""
    def rx_textbrowser_update(self, item):
        if (item[0] == 1):
            if (item[1] == 10):
                self.textBrowser.append(self.string)
                self.bar.setValue(self.bar.maximum())
                self.string = ""
            elif (item[1] != 13):
                self.string = self.string + chr(item[1])

    def about(self):
        QMessageBox.question(self, 'About', "CP2110 USB-to-UART\r\nVersion: 1.0\r\nAuthor: lgnq", QMessageBox.Ok, QMessageBox.Ok)

    def scan(self):
        print("scan the HID device")
        # self.widget.device_scan()

    def openclose(self):
        print("open or close")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

