from servidor.validacion import validacion_compra
from comun.funciones_sock import generar_sock_servidor
from servidor.catalogos import cargar_catalogo_productos
from comun.constantes import (
    DIRECCION_SERVIDOR_CATALOGO, 
    DIRECCION_SERVIDOR_IMAGENES, 
    FINAL_PRODUCTO, 
    SEPARADOR, 
    SEPARADOR_FINAL_IMAGEN, 
    SEPARADOR_NOMBRE_IMAGEN,
    DIRECTORIO
)

def levantar_servidor_catalogo():
    productos = cargar_catalogo_productos()
    
    sock = generar_sock_servidor(DIRECCION_SERVIDOR_CATALOGO)
    sock.listen()

    while True:
        print('Esperando conexion desde el servidor de catalogos...')
        conexion, direccion_cliente = sock.accept()

        identificador = conexion.recv(1024)

        if identificador.decode() == 'catalogo':
            try:
                for producto in productos:
                    producto_bytes = producto.obtener_bytes()
                    print(producto_bytes)
                    conexion.sendall(producto_bytes)

            finally:
                conexion.close()
        else:
            try:

                compras_productos = identificador.decode().split(FINAL_PRODUCTO)

                val = validacion_compra(productos, compras_productos)
                conexion.sendall(val.encode())
            
            finally:
                conexion.close()

def levantar_servidor_imagenes():
    imagenes = []

    sock_img = generar_sock_servidor(DIRECCION_SERVIDOR_IMAGENES)
    sock_img.listen()

    while True:
        print('Esperando conexion desde el servidor de imagenes...') 
        conexion, direccion_cliente = sock_img.accept()

        try: 
            recivo = conexion.recv(1024)
            nombre_imagenes = recivo.decode().split(SEPARADOR)

            for nombre_imagen in nombre_imagenes:
                if nombre_imagen:
                    imagenes += [DIRECTORIO + nombre_imagen]

            for imagen in imagenes:
                nombre_imagen = imagen.split('\\')
                datos_imagen = open(imagen, 'rb')

                conexion.sendall(str.encode(nombre_imagen[2]))
                conexion.sendall(SEPARADOR_NOMBRE_IMAGEN.encode())

                buffer_imagen = datos_imagen.read(1024)
                while(buffer_imagen):
                    conexion.send(buffer_imagen)
                    buffer_imagen = datos_imagen.read(1024)
                
                conexion.sendall(SEPARADOR_FINAL_IMAGEN.encode())

        finally:
            conexion.close()
