import sys
import random

from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # from ui file
        # self.setupUi(self) # from py file (need to import class from generated .py file)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        r = random.randint(1, 500)
        painter.drawEllipse(40, 40, r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyProgram()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
