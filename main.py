from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QComboBox, QLineEdit, QListWidget, QListWidgetItem
import sys
from PyQt5 import uic
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.poisk_btn: QPushButton
        self.poisk_btn.clicked.connect(self.coffee)

    def coffee(self):
        self.comboBox: QComboBox
        self.poisk: QLineEdit
        self.listWidget: QListWidget
        if self.poisk.text() == "":
            return None
        else:
            text = self.poisk.text()
        bd = sqlite3.connect("coffee.sqlite")
        curr = bd.cursor()
        if self.comboBox.currentText() == 'Объем':
            res = curr.execute(f'''SELECT * FROM information
                                    WHERE volum == {text}''').fetchall()
        elif self.comboBox.currentText() == 'Название':
            res = curr.execute(f'''SELECT * FROM information
                                    WHERE name == {text}''').fetchall()
        elif self.comboBox.currentText() == 'Степень обжарки':
            res = curr.execute(f'''SELECT * FROM information
                                    WHERE degree == {text}''').fetchall()
        else:
            res = curr.execute(f'''SELECT * FROM information
                                    WHERE condition == {text}''').fetchall()
        bd.close()
        print(res)
        self.listWidget.clear()
        for i in res:
            word = ''
            for elem in range(1, len(i)):
                word += str(elem) + ", "
            self.listWidget.addItem(QListWidgetItem(word))
        if res == list():
            self.listWidget.addItem(QListWidgetItem("Ничего не найденно!"))

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
