# Definicion
planet = {
    'name': 'Earth',
    'moons': 1
}

# ********************************************
# LECTURA DE DATOS
# Forma 1
print(planet.get('name'))

# Forma 2
print(planet['name'])

# Errores en lectura
#wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError

# ********************************************
# Modificación de valores
# Forma 1
planet.update({'name': 'Makemake'})

# Forma 2
planet['name'] = 'Makemake'

# Otro ejemplo
# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# ********************************************
# Adición de claves
planet['orbital period'] = 4333

# Eliminación de claves
planet.pop('orbital period')

# ********************************************
# Tipos de datos complejos
planet["diameter (km)"] = {'polar': 133709, 'equatorial':142984}

# Recuperar valores en un diccionario anidado
# Encadenar corchetes
print(f'{planet["name"]} polar diameter {planet["diameter (km)"]["polar"]}')