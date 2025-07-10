import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Esto es un mensaje de ejemplo")


ventana=tk.Tk()
ventana.title("Ejemplo 6")
ventana.geometry("400x200")
ventana.configure(bg="black")    

etiqueta=tk.Label(
    ventana,
    text="Presione el boton para ver el mensaje: ",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)
etiqueta.pack()

boton=tk.Button(ventana, text="Mostrar texto",
                fg="black",
                activebackground="red",
                 command=mostrar_mensaje)
boton.pack()

ventana.mainloop()