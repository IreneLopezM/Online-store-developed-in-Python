from concurrent.futures import ThreadPoolExecutor
from servidor.funciones_sock_servidor import (
    levantar_servidor_catalogo, 
    levantar_servidor_imagenes
)

with ThreadPoolExecutor() as e:
    e.submit(levantar_servidor_catalogo)
    e.submit(levantar_servidor_imagenes)