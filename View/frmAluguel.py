# coding: utf-8
import sys

from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi


class FrmAluguel(QDialog):
    def __init__(self):
        super(FrmAluguel, self).__init__()
        loadUi('View/UI/FrmAluguel.ui', self)
        self.setWindowTitle('Aluguel')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmAluguel()
    widget.show()
    sys.exit(app.exec())
