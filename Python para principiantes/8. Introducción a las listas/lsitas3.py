# Segmentacion de listas
planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# El indice final no incluye al elemento de la lista, solo hasta el anterior
# Antes de la tierra
planetas_antes_de_la_tierra = planetas[0:2]
print(planetas_antes_de_la_tierra)

# En caso el primer indice sea cero, se puede omitir
planetas_antes_de_la_tierra = planetas[:2]
print(planetas_antes_de_la_tierra)

print("************************************************")

# Mostar todos los planetas, despues de la tierra
planetas_despues_de_la_tierra = planetas[3:8]
print(planetas_despues_de_la_tierra)

# En caso el indice final sea ultimo elemento, se puede omitir
planetas_despues_de_la_tierra = planetas[3:]
print(planetas_despues_de_la_tierra)

print("************************************************")

# Combinación de listas
lunas_amalteas = ["Metis", "Adrastea", "Amalthea", "Thebe"]
lunas_galileanas = ["Io", "Europa", "Ganymede", "Callisto"]

lunas_regulares_jupiter = lunas_galileanas + lunas_amalteas
print("Lunas regulares de Jupiter", lunas_regulares_jupiter)

print("************************************************")

# Ordenación de listas
lunas_regulares_jupiter.sort()
print("Lunas regulares ordenadas",lunas_regulares_jupiter)

print("************************************************")

# Ordenación de listas
lunas_regulares_jupiter.sort(reverse=True)
print("Lunas regulares ordenadas",lunas_regulares_jupiter)