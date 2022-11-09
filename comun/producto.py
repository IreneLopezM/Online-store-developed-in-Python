import datetime
from comun.constantes import FINAL_PRODUCTO, SEPARADOR

class Producto():
    def __init__(self, str_producto = None):
        self.id = 0
        self.nombre = ''
        self.descripcion = ''
        self.precio = 0
        self.promocion = ''
        self.fecha = datetime.date(1, 1, 1)
        self.existencia = 0
        self.imagen = ''

        if str_producto:
            self.decodificar_str_producto(str_producto)

    def obtener_bytes(self):
        str_bytes = '{}{}{}{}{}{}{}{}{}'.format(
            str(self.id) + SEPARADOR,
            self.nombre + SEPARADOR,
            self.descripcion + SEPARADOR,
            str(self.precio) + SEPARADOR, 
            self.promocion + SEPARADOR,
            self.fecha.strftime("%d/%m/%Y") + SEPARADOR,
            str(self.existencia) + SEPARADOR,
            self.imagen + SEPARADOR,
            FINAL_PRODUCTO
        )

        return str_bytes.encode()

    def decodificar_str_producto(self, str_producto):
        cadena = str_producto.split(SEPARADOR)
        
        self.id = int(cadena[0])
        self.nombre = cadena[1]
        self.descripcion = cadena[2]
        self.precio = float(cadena[3])
        self.promocion = cadena[4]
        if cadena[5]:
            self.fecha = datetime.datetime.strptime(cadena[5], "%d/%m/%Y").date()
        self.existencia = int(cadena[6])
        self.imagen = cadena[7]