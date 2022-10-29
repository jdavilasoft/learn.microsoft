a = 16
b = 25
c = 27

if a > b:
    if b > c:
        print("A es mayor que B y B es mayor que C")
    else:
        print("A es mayor que B y B es menor que C")
elif a == b:
    print("A es igual a B")
else:
    print("A es menor que B")