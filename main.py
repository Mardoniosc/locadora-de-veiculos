# coding: utf-8
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi


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
        print('aluguel veiculo!')
        print('aluguel veiculo!')

    def frm_cliente_clique(self):
        print('cliente clique!')



if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmPrincipal()
    widget.show()
    sys.exit(app.exec())
