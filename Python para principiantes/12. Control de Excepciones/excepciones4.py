try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Un problema para leer el archivo:", err)

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("No se puede encontrar el archivo")
    elif err.errno == 13:
        print("Se encontró el archivo config.txt, pero no se puede leer")