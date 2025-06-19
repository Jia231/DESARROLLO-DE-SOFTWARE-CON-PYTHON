while True:
    try:
        n1 = float(input("Ingrese un numero"))
        n2 = float(input("Ingrese un numero"))
        print("La suma es ", n1+n2)
        print("La multiplcacion es ", n1*n2)
        print("La division es ", n1/n2)
        print("La resta es ", n1-n2)

    except ZeroDivisionError:
        print("Hubo un error")
        break
    except ValueError:
        print("Hubo un error")