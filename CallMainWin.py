import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import *

class MainWindow(QMainWindow,Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())