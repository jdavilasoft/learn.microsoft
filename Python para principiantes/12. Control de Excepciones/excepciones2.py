try:
    open("config.txt")
except FileNotFoundError:
    print("No se pudo encontrar el archivo confi.txt")