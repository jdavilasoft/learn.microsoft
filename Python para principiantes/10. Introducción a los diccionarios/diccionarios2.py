
rainfall = {
    'octubre': 3.5,
    'noviembre': 4.2,
    'diciembre': 2.1
}

# Recorrer un diccionario
for clave in rainfall.keys():
    print(f"{clave} : {rainfall[clave]} cm")

# Verificar si existe una clave
if 'diciembre' in rainfall:
    rainfall['diciembre'] = rainfall['diciembre'] + 1
else:
    rainfall['diciembre'] = 1

# Recorrer el diccionario y sumar valores
total = 0
for valor in rainfall.values():
    total = total + valor

print(f"Total de lluvia de los ultimos meses: {total}")