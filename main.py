import os
import shutil
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI(self)
        self.setWindowTitle("PYTAX - File Organizer")
        appIcon = QIcon("_imgs/icone.png")
        self.setWindowIcon(appIcon)


if __name__ == '_main_':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
