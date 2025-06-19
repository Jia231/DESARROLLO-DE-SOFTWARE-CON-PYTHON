while True:
    try:
        nom = input("Escriba su nombre: ")
        if nom.isalpha():
            break
        print("Bienvenido, ", nom)
    except ValueError:
        print("Hubo un error")