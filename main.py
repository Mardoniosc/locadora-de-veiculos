# coding: utf-8
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from View.frmAluguel import FrmAluguel
from View.frmCliente import FrmCliente

class FrmPrincipal(QMainWindow):
    def __init__(self):
        super(FrmPrincipal, self).__init__()
        loadUi('View/UI/FrmPrincipal.ui', self)
        self.setWindowTitle('Principal')


# ---------------------------------------------- Evento de clique ----------------------------------------------
        self.btnAlugar.clicked.connect(self.frm_aluguel_click)
        self.btnCliente.clicked.connect(self.frm_cliente_clique)
# ---------------------------------------------- Funções dos Botões ----------------------------------------------

    def frm_aluguel_click(self):
        self.frmaluguel = QMainWindow()
        self.widget = FrmAluguel()
        self.widget.show()

    def frm_cliente_clique(self):
        self.frmcliente = QMainWindow()
        self.widget = FrmCliente()
        self.widget.show()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmPrincipal()
    widget.show()
    sys.exit(app.exec())
