import math

while True:
    try:
        c1 = float(input("Ingrese el cateto: "))
        c2 = float(input("Ingrese el cateto: "))
        h = math.sqrt(c1**2+c2**2)
        print(f"La hipotenusa es {h}")
    except ValueError:
        print("Error")    