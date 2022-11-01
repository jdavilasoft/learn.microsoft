
# Ejemplo de funcion no devuelve nada
def rocket_parts1():
    print("payload, propellant, structura")

rocket_parts1()

# Ejemplo de funcion, devuelve valor
def rocket_parts2():
    return "payload, propellant, structura"

output = rocket_parts2()
print(output)

# Ejemplo de funcion, con parametros
tmp = any([True, False, False])
print(tmp)

tmp = any([False, False, False])
print(tmp)

# Ejemplo de funcion de parametro opcional
print(str(15))
print(str())