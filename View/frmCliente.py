# coding: utf-8
import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.uic import loadUi


class FrmCliente(QWidget):
    def __init__(self):
        super(FrmCliente, self).__init__()
        loadUi('View/UI/FrmCliente.ui', self)
        self.setWindowTitle('Aluguel')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmCliente()
    widget.show()
    sys.exit(app.exec())
