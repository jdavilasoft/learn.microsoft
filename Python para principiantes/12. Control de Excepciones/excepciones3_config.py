def main():
    try:
        configuracion = open("/tmp/config.txt")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Se encontró config.txt, pero es un directorio, no se puede leer")
    except (BlockingIOError, TimeoutError):
        print("Error en el sistema de archivos, no se puede completar la lectura del archivo")

if __name__ == '__main__':
    main()