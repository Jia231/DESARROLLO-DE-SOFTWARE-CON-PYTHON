import tkinter as tk
from tkinter import ttk

def seleccionar_elemento(event):
    seleccion=combobox.get()
    resultado.config(text=f"Elemento seleccionado {seleccion}")


ventana=tk.Tk()
ventana.title("Ejemplo 5")
ventana.geometry("400x200")
ventana.configure(bg="black")    

etiqueta=tk.Label(
    ventana,
    text="Seleccione un elemento: ",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)
etiqueta.pack(pady=40)
style=ttk.Style()
style.theme_use("clam")
style.configure(
    "TCombobox",
    fieldbackground="white",
    background="#cce5ff"
)
elementos=["java","python","C++", "R"]
combobox = ttk.Combobox(ventana,
                        values=elementos,
                        font="Arial" 
                        )
combobox.bind("<<ComboboxSelected>>", seleccionar_elemento)
combobox.pack(pady=5)

resultado=tk.Label(
    ventana,
    text="",
    font=("Arial", 16, "bold"),
)
resultado.pack()
ventana.mainloop()