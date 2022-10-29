
# Ejemplo recorrer una lista de enteros con 'for'
from time import sleep


lista_numeros = [5, 4, 3, 2, 1]
for numero in lista_numeros:
    print(numero)
print("Blast off!! 🚀")

# Modificamos el ejemplo anterior
# Esperamos un segundo
lista_numeros = [5, 4, 3, 2, 1]
for numero in lista_numeros:
    print(numero)
    sleep(1)
print("Blast off!! 🚀")