from comun.funciones_sock import generar_sock_cliente
from comun.producto import Producto
import os
import sys
from PyQt5.QtWidgets import QApplication
from cliente.carrito_interfaz import Carrito_inter, guardar_compra
from cliente.carrito_super import Carrito_contenido
from cliente.confirmacion import Confirmacion_agregar
from comun.constantes import (
    DIRECCION_SERVIDOR_IMAGENES,  
    DIRECCION_SERVIDOR_CATALOGO,
    FINAL_PRODUCTO, SEPARADOR, SEPARADOR_2, SEPARADOR_FINAL_IMAGEN, SEPARADOR_NOMBRE_IMAGEN
)

productos = []
app = QApplication(sys.argv)

def abrir_interfaz(inter):
    interfaz = inter
    interfaz.show()
    app.exec_()

def obtener_catalogo_productos():
    sock = generar_sock_cliente(DIRECCION_SERVIDOR_CATALOGO)
    productos_bytes = b''
    try:
        sock.sendall(b'catalogo')
        while True:
            recivido = sock.recv(10)
            
            if recivido:
                productos_bytes += recivido
            else:
                break

    finally:
        sock.close()

    productos_str = productos_bytes.decode().split(FINAL_PRODUCTO)

    for producto_str in productos_str:
        if producto_str:
            producto = Producto(producto_str)
            productos.append(producto)

    obtener_imagenes(productos)
    
    interfaz = Carrito_inter(productos)
    abrir_interfaz(interfaz)

    enviar_compra()



def enviar_compra():
    compra = guardar_compra('1')
    compra_str = str(compra[0])

    sock = generar_sock_cliente(DIRECCION_SERVIDOR_CATALOGO)

    try:
        sock.sendall(compra_str.encode())

        validacion = sock.recv(1024)

    finally:
        sock.close()

    validacion_compra = validacion.decode().split(SEPARADOR_2)
    print(validacion_compra)

    if validacion_compra[0] == '0': #compra 
        carro = Carrito_contenido(validacion_compra[1], validacion_compra[2], 4)
        carro.setWindowTitle('Ticket')
        carro.e_precio.setText('Precio con promoción')
        abrir_interfaz(carro)
        
    else: #mensaje de error
        agregar = Confirmacion_agregar()
        agregar.e_confirm.setText(validacion_compra[1])
        agregar.show()
        app.exec_()



def obtener_imagenes(productos):
    sock = generar_sock_cliente(DIRECCION_SERVIDOR_IMAGENES)

    imagenes_str = ''
    for producto in productos:
        if producto:
            imagenes = producto.imagen
            imagenes_str += imagenes + SEPARADOR

    sock.sendall(imagenes_str.encode())

    datos_imagenes = b''

    try:
        while True:
            datos = sock.recv(1024)

            if datos:
                datos_imagenes += datos
            else: 
                break

    finally:
        sock.close()

    caperta = 'cliente\\Imagenes'
    if not os.path.exists(caperta):
        os.makedirs(caperta)

    imagenes = datos_imagenes.split(SEPARADOR_FINAL_IMAGEN.encode())

    for imagen in imagenes:
        if imagen:
            dato_imagen = imagen.split(SEPARADOR_NOMBRE_IMAGEN.encode()) 
            with open(caperta + '\\' + dato_imagen[0].decode(), 'wb') as a:
                a.write(dato_imagen[1])
            
    return 'Hecho'

