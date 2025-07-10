import tkinter as tk

ventana=tk.Tk()
ventana.title("Titulo")
etiqueta=tk.Label(ventana, text="Jia Liu")
etiqueta.pack()

def saludar():
    etiqueta.config(text="Hola")

boton = tk.Button(ventana, text="De click aqui", command=saludar)
boton.pack()

ventana.mainloop()