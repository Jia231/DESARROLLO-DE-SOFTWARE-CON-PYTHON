boleto_general = 5000
boleto_vip = 15000
boleto_platino = 25000

def calcular_precio_boleto(tipo_boleto, cantidad):
    if tipo_boleto == "general":
        precio = boleto_general * cantidad
    elif tipo_boleto == "vip":
        precio = boleto_vip * cantidad
    elif tipo_boleto == "platino":
        precio = boleto_platino * cantidad
    else:
        print("Tipo de boleto no valido.")
        return None

    print(f"El precio total por {cantidad} boletos {tipo_boleto} es: {precio}")
    return precio

while True:
    tipo = input("Introduce el tipo de boleto (general, vip, platino): ").strip().lower()
    if tipo in ("general", "vip", "platino"):
        try:
            cantidad = int(input("Introduce la cantidad de boletos: "))
            calcular_precio_boleto(tipo, cantidad)
        except ValueError:
            print("Entrada no valida. Por favor, introduce el valor correcto")
        break
    else:
        print("Tipo de boleto no valido. Intenta de nuevo.")

