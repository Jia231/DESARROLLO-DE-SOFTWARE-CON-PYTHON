import random
from colorama import Style

def adivinar_numero():
    numero_secreto = random.randint(0,100)
    intentos = 10
    print("Bievenidos al juego: Adivinar un numero")
    print("Tienes 10 intentos")
    while intentos > 0:
        try:
            numero = int(input(f"{Style.BRIGHT}Adivina un numero "))
            if numero > numero_secreto:
                print("El numero secreto es menor")
            elif numero < numero_secreto:    
                print("El numero secreto es mayor")
            else:
                print("Adivinaste el numero!")
                break    
        except:
            print("Numero no es valido") 

        intentos = intentos - 1

    if intentos == 0:
        print(f"Alcanzaste el maximo numero de intentos, el numero secreto es {numero_secreto}")


adivinar_numero()
