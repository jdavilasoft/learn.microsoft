gravedad_tierra = 1.0
gravedad_luna = 0.166

gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# Peso de un autobus
# En la tierra en kg
peso_bus = 12650

print("En la Tierra, un bus pesa", peso_bus, "kg")
print("En Mercurio, el bus pesa", peso_bus * gravedad_planetas[0], "kg")

print()
print("************************************************************")
print()
# Uso de MIN y MAX
print("El peso mas ligero en el sistema solar", peso_bus * min(gravedad_planetas), "kg")
print("El mas pesado en el sistema solar sería", peso_bus * max(gravedad_planetas), "kg")