while True:
    try:
        f = float(input("Escriba los grados en F ")
                  )
        c = ((f-32)*5)/9
        print("Grados en c ", c)
    except ValueError:
        print("Hubo un error")
        break    