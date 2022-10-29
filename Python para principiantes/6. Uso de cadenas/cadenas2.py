
# Pone la primera letra de cada palabra a mayuscula
print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading.title()

# Separa las palabras por cada espacio
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
temperatures.split()

# Separa las palabras por cada salto de linea
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
temperatures.split('\n')

# Busca de cadena dentro de otra cadena
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

# Busca una cadena dentro de otra cadena, devuelve la posicion (indice) y -1 si no lo encuentra
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
print(temperatures.find("Mars"))

# Contar el numero de palabras
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

# Convierte en minuscula
print("The Moon And The Earth".lower())

# Convierte a mayuscula
print("The Moon And The Earth".upper())

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts[-1]) # Devuelve el último elemento

# Recorre cada palabra separada por espacio y verifica si es un numero (solo enteros)
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# Una cadena, empieza con, termina con
"-60".startswith('-')
if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# Reemplazar texto dentro de una cadena
"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")

# join une cadenas
# En este ejemplo usa un salto de linea para unir dos cadenas
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)