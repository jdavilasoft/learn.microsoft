
# Argumentos opcionales
# o 'argumentos de la palabra clave'

from datetime import timedelta,datetime

def hora_llegada_luna(horas = 51):
    ahora = datetime.now()
    llegada = ahora + timedelta(hours=horas)
    return llegada.strftime("Llegada: %A %H:%M")

print(hora_llegada_luna())
print(hora_llegada_luna(0))

# Ejemplo con argumentos y
# argumentos de palabra clave

def hora_llegada(destino, horas=51):
    ahora = datetime.now()
    llegada = ahora + timedelta(hours=horas)
    return llegada.strftime(f"{destino} Arrival: %A %H:%M")

print(hora_llegada("Luna"))
print(hora_llegada("Orbita", horas=0.13))