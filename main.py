import sys
import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui import Ui_MainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)
        painter.setPen(QPen(color, 8, Qt.SolidLine))
        painter.setBrush(QBrush(color, Qt.SolidPattern))
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
