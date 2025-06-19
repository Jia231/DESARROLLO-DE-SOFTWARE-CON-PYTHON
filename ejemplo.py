import os
os.system("cls")


cantidad=int(input("Digite la cantidad de estudiantes: "))

nombre=[]
nota1=[]
nota2=[]
nota3=[]
promedio=[]
estado=[]

for i in range(0, cantidad, 1):
    nombre.append(input(f"Nombre del estudiante # {str(i+1)} \n"))
    nota1.append(float(input("Digite la nota 1: ")))
    nota2.append(float(input("Digite la nota 2: ")))
    nota3.append(float(input("Digite la nota 3: ")))

    promedio.append((nota1[i]+nota2[i]+nota3[i])/3)

for i in promedio:
    if(i<70):
        estado.append("Reprobado")
    else:
        estado.append("Aprobado")

for g in range (0,cantidad,1):
    print(f"El estudiante {nombre[g]} {estado[g]} con un promerio de {promedio[g]}")