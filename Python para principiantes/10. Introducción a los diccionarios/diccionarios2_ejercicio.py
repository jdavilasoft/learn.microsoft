lunas_planetas = {
    'mercurio': 0,
    'venus': 0,
    'tierra': 1,
    'marte': 2,
    'jupiter': 79,
    'saturno': 82,
    'urano': 27,
    'neptuno': 14,
    'pluton': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Almacenmos todos los valores en una lista
lunas = lunas_planetas.values()

#Sumamos el total del planeta
total_planetas = len(lunas_planetas.keys())

total_lunas = 0
for moon in lunas:
    total_lunas = total_lunas + moon

promedio = total_lunas / total_planetas

print(promedio)