import datetime
from comun.producto import Producto

def cargar_catalogo_productos():
    productos = []
    productos_csv = [] 

    with open('servidor\\productos.csv', 'r') as csv:
        productos_csv = csv.read().splitlines()
    
    for producto_csv in productos_csv:
        aux_producto_csv = producto_csv.split(',')
        
        producto = Producto()
        producto.id = int(aux_producto_csv[0])
        producto.nombre = aux_producto_csv[1]
        producto.descripcion = aux_producto_csv[2]
        producto.precio = float(aux_producto_csv[3])
        producto.promocion = aux_producto_csv[4]
        if aux_producto_csv[5]:
            producto.fecha = datetime.datetime.strptime(aux_producto_csv[5], "%d/%m/%Y").date()
        producto.existencia = int(aux_producto_csv[6])
        producto.imagen = aux_producto_csv[7]

        productos.append(producto)
    
    return productos


