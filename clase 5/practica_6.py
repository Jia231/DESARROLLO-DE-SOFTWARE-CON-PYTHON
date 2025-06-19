# Practica 6: Clasificación de pulsaciones

# Solicitar los datos al usuario
edad = int(input("Ingrese su edad: "))
pulsaciones = int(input("Ingrese su número de pulsaciones por minuto: "))

# Determinar la categoría
if pulsaciones < 60:
    categoria = "Bradicardia (Frecuencia cardíaca baja)"
elif 60 <= pulsaciones <= 100:
    categoria = "Normal"
else:
    categoria = "Taquicardia (Frecuencia cardíaca alta)"

# Mostrar los resultados
print(f"\nPulsaciones ingresadas: {pulsaciones}")
print(f"Clasificación: {categoria}")