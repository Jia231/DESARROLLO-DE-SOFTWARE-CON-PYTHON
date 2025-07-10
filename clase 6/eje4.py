import tkinter as tk
def mostrar_texto():
    texto=entrada_texto.get()
    etiquet_resultado.configure(text=f"Texto ingresado {texto}")

ventana=tk.Tk()
ventana.title("Titulo")
ventana.geometry("400x200")
ventana.configure(bg="black")

entrada_texto=tk.Entry(ventana)
entrada_texto.pack()
boton=tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack()

etiquet_resultado=tk.Label(
    ventana,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)
etiquet_resultado.pack(pady=10)
ventana.mainloop()