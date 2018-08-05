# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.device_combobox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_combobox.sizePolicy().hasHeightForWidth())
        self.device_combobox.setSizePolicy(sizePolicy)
        self.device_combobox.setObjectName("device_combobox")
        self.horizontalLayout.addWidget(self.device_combobox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.baudrate_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.baudrate_combobox.setObjectName("baudrate_combobox")
        self.baudrate_combobox.addItem("")
        self.baudrate_combobox.addItem("")
        self.baudrate_combobox.addItem("")
        self.horizontalLayout.addWidget(self.baudrate_combobox)
        self.open_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.open_pushbutton.setEnabled(True)
        self.open_pushbutton.setObjectName("open_pushbutton")
        self.horizontalLayout.addWidget(self.open_pushbutton)
        self.clear_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clear_pushbutton.setObjectName("clear_pushbutton")
        self.horizontalLayout.addWidget(self.clear_pushbutton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.rx_textbrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.rx_textbrowser.setFont(font)
        self.rx_textbrowser.setObjectName("rx_textbrowser")
        self.verticalLayout.addWidget(self.rx_textbrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionScan = QtWidgets.QAction(MainWindow)
        self.actionScan.setObjectName("actionScan")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionScan)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.clear_pushbutton.clicked.connect(self.rx_textbrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CP2110 HID USB-to-UART"))
        self.label.setText(_translate("MainWindow", "Device List:"))
        self.label_2.setText(_translate("MainWindow", "Baudrate:"))
        self.baudrate_combobox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrate_combobox.setItemText(1, _translate("MainWindow", "38400"))
        self.baudrate_combobox.setItemText(2, _translate("MainWindow", "115200"))
        self.open_pushbutton.setText(_translate("MainWindow", "Open"))
        self.clear_pushbutton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionScan.setText(_translate("MainWindow", "Scan"))
        self.actionScan.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))

