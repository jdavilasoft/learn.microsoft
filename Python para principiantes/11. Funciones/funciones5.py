
# Argumentos de variable
def variable_lenght(*args):
    print(args)

variable_lenght()
variable_lenght("one", "two")
variable_lenght(None)

# Otro ejemplo
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Tiempo total de lanzamiento {total_minutes} minutos"
    else:
        return f"Tiempo total de lanzamiento {total_minutes/60} horas"

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))


# Argumentos de palabra clave variable
def variable_lenght(**kwargs):
    print(kwargs)

variable_lenght(tanks=1, day="Miercoles", pilots=3)

# Otro ejemplo
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronautas asignados a la mision")
    for titulo, nombre in kwargs.items():
        print(f"{titulo} : {nombre}")

crew_members(capitan = "Neil Armstrong", piloto = "Buzz Aldrin", piloto_comando = "Michael Collins")