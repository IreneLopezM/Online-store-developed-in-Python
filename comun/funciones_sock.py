import socket

def generar_sock_cliente(direccion_servidor):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(direccion_servidor)

    return sock

def generar_sock_servidor(direccion_servidor):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(direccion_servidor)

    return sock