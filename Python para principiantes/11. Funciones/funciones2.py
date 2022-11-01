
# Ejemplo de funcion con un argumento
def distancia_desde_tierra(destino):
    if destino.lower() == 'luna':
        return "238855"
    else:
        return "No se puede calcular el destino"

print(distancia_desde_tierra("Luna"))

# Sin argumentos, sale error
#print(distancia_desde_tierra())

# Ejemplo de funcion con varios argumentos
def dias_para_completar(distancia, velocidad):
    horas = distancia / velocidad
    return horas / 24

dias = dias_para_completar(238855, 75)
print(round(dias))
