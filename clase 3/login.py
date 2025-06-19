try:
    u = input("Digite el nombre del usuario: ")
    p = input("Digite el password: ")
    if u == "Ana" and p == "07*Pv69Tn" :
        print("Has entrado al sistema.")
    else:
        raise Exception() 
except Exception:
    print("Error")