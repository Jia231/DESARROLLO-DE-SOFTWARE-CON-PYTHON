while True:
    try:
        b=float(input("Escriba la base"))
        a=float(input("Escriba la altura"))
        p=b**2+a**2
        area=b*a
        print(f"El perimetro es {p}")
        print(f"El area es {a}")
        break
    except ValueError:
        print("Hubo un error")    