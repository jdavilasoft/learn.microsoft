#program.py
sum = 1 + 2
print(sum)

# Imprimir en consola
print("Este texto se mostrara en consola")

# Operaciones
sum = 1 + 2 # 3
product = sum * 2.2
print(product)

#muestra el tipo de dato
print(type(sum))
print(type(product))


# Condicional, para saber el tipo de dato
if (type(sum) == int):
    print("Entero")
else:
    print("Otro")

# Uso de fechas
from datetime import date
print(date.today())
print("la fecha de hoy es: " + str(date.today()))