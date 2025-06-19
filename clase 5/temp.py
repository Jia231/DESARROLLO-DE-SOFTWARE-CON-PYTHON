def calcular_promedio():
    try:
        cantidad_temp = int(input("Digite la cantidad de temperaturas: "))
    except ValueError:
        print("Digite un numero valido")
    arr = []

    for i in range(0, cantidad_temp):
        try:
            t = float(input("Digite la temperatura: "))
        except ValueError:
            print("Digite un numero valido")    

        arr.append(t)

    print(f"El promedio de temperatura es {sum(arr)/len(arr)}")        


calcular_promedio()       