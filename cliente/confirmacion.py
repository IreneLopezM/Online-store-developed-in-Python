from comun.constantes import SEPARADOR
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton

class Confirmacion_agregar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(200, 100)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.e_confirm = QLabel(self)
        self.boton_aceptar = QPushButton('Aceptar')
        self.layout.addWidget(self.e_confirm)
        self.layout.addWidget(self.boton_aceptar)

        self.boton_aceptar.clicked.connect(self.close)