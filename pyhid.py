import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.openclose)

    def openclose(self):
        print("open or close")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

