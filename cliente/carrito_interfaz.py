from comun.constantes import FINAL_PRODUCTO, SEPARADOR
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from cliente.carrito_super import Carrito_contenido
from cliente.confirmacion import Confirmacion_agregar

carrito = {}
productos_comprados = ''

class Carrito_inter(QMainWindow):

    def __init__(self, productos):
        super().__init__()
        uic.loadUi('prueba_i.ui', self)
        self.setWindowTitle('Tienda')

        for x in range(1, 6):
            e_producto = getattr(self, 'e_producto_' + str(x))
            e_precio = getattr(self, 'e_precio_' + str(x))
            e_descripcion = getattr(self, 'e_descripcion_' + str(x))
            e_promocion = getattr(self, 'e_promocion_' + str(x))
            e_vigencia = getattr(self, 'e_vigencia_' + str(x))
            combo_existencias = getattr(self, 'combo_existencias_' + str(x))
            e_imagen = getattr(self, 'e_imagen_' + str(x))

            e_producto.setText(productos[x - 1].nombre)
            e_precio.setText(str(productos[x - 1].precio))
            e_descripcion.setText(productos[x - 1].descripcion)
            e_promocion.setText(productos[x - 1].promocion)
            e_vigencia.setText((productos[x - 1].fecha).strftime("%d/%m/%Y"))

            for y in range (1, productos[x - 1].existencia + 1):
                combo_existencias.addItem(str(y))
            
            pixmap = QPixmap('cliente\\Imagenes\\'+productos[x - 1].imagen)
            e_imagen.setPixmap(pixmap)
        
        self.boton_agregar_carrito_1.clicked.connect(lambda: self.agregar_carrito(1, productos))
        self.boton_agregar_carrito_2.clicked.connect(lambda: self.agregar_carrito(2, productos))
        self.boton_agregar_carrito_3.clicked.connect(lambda: self.agregar_carrito(3, productos))
        self.boton_agregar_carrito_4.clicked.connect(lambda: self.agregar_carrito(4, productos))
        self.boton_agregar_carrito_5.clicked.connect(lambda: self.agregar_carrito(5, productos))
        
        self.Boton_carrito.clicked.connect(lambda: self.ver_carrito(productos))
        self.boton_comprar.clicked.connect(lambda: self.comprar(productos, productos_comprados))
        print(productos_comprados)


    def agregar_carrito(self, id_boton, productos):
        combo_existencias = getattr(self, 'combo_existencias_' + str(id_boton))
        id_producto = productos[id_boton - 1].id
        carrito[id_producto] = int(combo_existencias.currentText()) + carrito.get(id_producto, 0)
        
        self.ventana_comfir('Producto agregado al carrito')


    def ver_carrito(self, productos):
        if not carrito:
            self.ventana_comfir('Carrito vacio')

        else:
            carrito_lista = ''
            precio_total = 0
            columnas = 3

            for key in carrito.keys():
                str_carrito = (
                    str(carrito[key]) + SEPARADOR + 
                    productos[key - 1].nombre + SEPARADOR + 
                    str(productos[key - 1].precio * carrito[key]) + SEPARADOR
                )
                carrito_lista = carrito_lista + str_carrito
                precio_total += productos[key - 1].precio * carrito[key]

            self.carro = Carrito_contenido(carrito_lista, precio_total, columnas)
            self.carro.setWindowTitle('Carrito de compras')
            self.carro.e_precio.setText('Precio sin promoción')
            self.carro.e_nota.setText('NOTA: no se aplicara la promocion hasta que la valide el servidor')
            self.carro.mostrar_ventana()


    def comprar(self, productos, productos_comprados):
        if not carrito:
            self.ventana_comfir('Carrito vacio')

        else:
            for key in carrito.keys():
                str_carrito = (
                    str(productos[key - 1].id) + SEPARADOR + 
                    str(carrito[key]) + FINAL_PRODUCTO
                )
                productos_comprados = productos_comprados + str_carrito
            guardar_compra(productos_comprados)
            self.close()


    def ventana_comfir(self, texto):
        self.agregar = Confirmacion_agregar()
        self.agregar.e_confirm.setText(texto)
        self.agregar.show()


compra = []
def guardar_compra(productos_comprados):
    if productos_comprados == '1':
        return compra
    else:
        compra.append(productos_comprados)