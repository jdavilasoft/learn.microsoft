# Uso del bucle while
user_input = ''

while user_input.lower() != 'done':
    user_input = input("Ingrese un nuevo valor, 'done' para terminar: ")

print("***************************************************************")

# Bucle while usando listas
# --------------------------------------------

# Creamos una variable para ingreso de datos
user_input = ''
# Creamos una lista para guardar los valores
entradas = []

while user_input.lower() != 'done':
    # Comprobamos si hay algun valor en 'user_input'
    if user_input:
        entradas.append(user_input)
    user_input = input("Ingrese un nuevo valor, 'done' para terminar: ")

print(entradas)