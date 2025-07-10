import tkinter as tk
def mostrar_texto():
    texto=entrada_texto.get()
    etiqueta.configure(text=f"Texto ingresado {texto}")

ventana=tk.Tk()
ventana.title("Titulo")

etiqueta=tk.Label(
    ventana,
    text="Ingrese un texto",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)
etiqueta.pack()
entrada_texto=tk.Entry(ventana)
entrada_texto.pack()
boton=tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack()
ventana.mainloop()