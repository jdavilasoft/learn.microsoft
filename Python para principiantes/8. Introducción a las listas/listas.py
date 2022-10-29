# Crea una lista
planetas = ["mercurio", "venus", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno"]

# Acceder a los elementos de la lista
print("El primer planeta es: ", planetas[0])
print("El sengundo planeta es: ", planetas[1])
print("El tercer planeta es: ", planetas[2])

planetas[3] = "Planeta Rojo"

# Cambiar el valor de un elemento
print("Mars is also known as", planetas[3])

# Saber el numero de elementos de una lista
numero_planetas = len(planetas)
print("Hay", numero_planetas, "planetas en el sistema solar")

# Agregar elementos a a lista
planetas.append("Plutón")

numero_planetas = len(planetas)
print("Hay", numero_planetas, "planetas en el sistema solar")

# Eliminar el último elemento de la lista
planetas.pop()
numero_planetas = len(planetas)
print("Hay", numero_planetas, "planetas en el sistema solar")

# Uso de indices negativos
print("The first planet is", planetas[0])
# El -1 devuelve el ultimo elemento de la lista
print("The last planet is", planetas[-1])
# El -2 devuelve el penultimo elemento de la lista
print("The penultimate planet is", planetas[-2])

# Busca un valor y devuelve el indice
indice_jupiter = planetas.index("jupiter")
print("Jupiter is the", indice_jupiter + 1, "planet from the sun")
