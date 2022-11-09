from comun.constantes import SEPARADOR, FINAL_PRODUCTO, SEPARADOR_2
from datetime import date


def validacion_compra(productos, compras_productos):
    num_validacion = 0

    for producto in compras_productos:
        compra_producto = producto.split(SEPARADOR)

        if compra_producto != ['']:
            id = int(compra_producto[0]) - 1 

            if int(compra_producto[1]) > productos[id].existencia:
                num_validacion = 1
                break

        else:
            break


    if num_validacion == 0:
        carrito_lista = ''
        carro = ''
        precio = 0

        for producto in compras_productos:
            compra_producto = producto.split(SEPARADOR)

            if compra_producto != ['']:
                id = int(compra_producto[0]) - 1 

                productos[id].existencia = productos[id].existencia - int(compra_producto[1])

                carrito_lista, precio_total = validacion_promo(id, productos, compra_producto[1])
                carro += carrito_lista
                precio += precio_total

            else:
                break
        
        carrito_lista = carro + SEPARADOR_2 + str(precio)

        return ('0' + SEPARADOR_2 + carrito_lista)

    else:
        print('Error en la compra, sobrepaso los productos en exixtencia')
        error = (
            '1' + 
            SEPARADOR_2 + 
            'Error en la compra, sobrepaso los productos en existencia'
        )

        return error

def validacion_promo(id, productos, cantidad):
    carro_lista = ''
    if productos[id].promocion == 'Ninguna':
        carro_lista, precio_total = total_compra(productos[id].precio, cantidad, id, productos)

    else:
        hoy = date.today()

        if hoy <= productos[id].fecha:
            if '% de descuento' in productos[id].promocion:
                porcentaje = ''

                for x in range(0, 2):
                    porcentaje += productos[id].promocion[x]

                porcentaje_float = float(porcentaje)/100
                desceunto = productos[id].precio * porcentaje_float
                precio = productos[id].precio - desceunto
                carro_lista, precio_total = total_compra(precio, cantidad, id, productos)
            else:
                par = int(cantidad) % 2
                if par == 0:
                    precio = productos[id].precio * 0.5
                    carro_lista, precio_total = total_compra(precio, cantidad, id, productos)
                else:
                    precio = productos[id].precio * 0.5
                    total_producto = precio * (int(cantidad) - 1) + productos[id].precio
                    carro_lista, precio_total = realizar_compra(id, productos, cantidad, total_producto)
        else:
            carro_lista, precio_total = total_compra(productos[id].precio, cantidad, id, productos)

    return carro_lista, precio_total


def total_compra(precio, cantidad, id, productos):
    total_producto = precio * int(cantidad)
    carro_lista, total_producto = realizar_compra(id, productos, cantidad, total_producto)

    return carro_lista, total_producto


def realizar_compra(id, productos, cantidad, total_producto):
    str_carrito = (
        cantidad + SEPARADOR + 
        productos[id].nombre + SEPARADOR + 
        str(total_producto) + SEPARADOR +
        productos[id].promocion + SEPARADOR
        )

    return str_carrito, total_producto