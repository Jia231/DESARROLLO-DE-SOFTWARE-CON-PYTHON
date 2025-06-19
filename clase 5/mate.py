import math

try:
    numero = int(input("Digite un numero: "))
    print(f"La raiz cuadrado es {math.sqrt(numero)}")
    print(f"El seno es {math.sin(numero)}")
except ValueError:
    print("Digite un numero valido")    


