from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton
from comun.constantes import SEPARADOR

class Carrito_contenido(QDialog):
    def __init__(self, carrito, precio_total, columnas):

        QDialog.__init__(self)
        self.resize(500, 400)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.sublayout_titulo = QtWidgets.QHBoxLayout(self)
        self.e_cantidad = QLabel('Cantidad')
        self.e_producto = QLabel('Producto')
        self.e_precio = QLabel(self)
        self.sublayout_titulo.addWidget(self.e_cantidad)
        self.sublayout_titulo.addWidget(self.e_producto)
        self.sublayout_titulo.addWidget(self.e_precio)

        if columnas == 4:
            self.e_promocion = QLabel('Promocion')
            self.sublayout_titulo.addWidget(self.e_promocion)

        self.layout.addLayout(self.sublayout_titulo)
        self.layout.addWidget(self.scrollArea)

        carrito_lista = carrito
        carrito_lista = carrito_lista.split(SEPARADOR)

        filas = (len(carrito_lista)-1)//columnas
        recorrido_lista = 0
        for i in range(filas):
            for j in range(columnas):
                self.gridLayout.addWidget(QtWidgets.QLabel(carrito_lista[recorrido_lista]), i, j)
                recorrido_lista += 1

        self.sublayout_total = QtWidgets.QHBoxLayout(self)
        self.e_total = QLabel('Total')
        self.e_cantidad = QLabel(str(precio_total))
        self.e_espacio = QLabel(self)
        self.sublayout_total.addWidget(self.e_total)
        self.sublayout_total.addWidget(self.e_espacio)
        self.sublayout_total.addWidget(self.e_cantidad)
        self.layout.addLayout(self.sublayout_total)

        if columnas == 3:
            self.e_nota = QLabel(self)
            self.layout.addWidget(self.e_nota)

        self.boton_aceptar = QPushButton('Aceptar')
        self.layout.addWidget(self.boton_aceptar)

        self.boton_aceptar.clicked.connect(lambda: self.close())

    def mostrar_ventana(self):
        self.show()