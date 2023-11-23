from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.poisk_btn: QPushButton
        self.poisk_btn.clicked.connect()

    def coffee(self):
