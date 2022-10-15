from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('fr_main.ui', self)
        self.t2 = uic.loadUi('ordem_serv.ui')

        self.button = self.findChild(QtWidgets.QPushButton, 'btn_ordemservico')
        self.button.clicked.connect(self.ordemServico)

    def ordemServico(self):
    
        window.close()
        self.t2.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
