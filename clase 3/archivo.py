try:
    p = input("Escriba el nombre del archivo: ")
    with open(p+".txt", "r") as ar:
        cont = ar.read()
        print(cont)
except FileNotFoundError:
    with open(p+".txt", "w") as ar:
        ar.write("Hola")
        ar.close()
    print("No se encontro el archivo")        