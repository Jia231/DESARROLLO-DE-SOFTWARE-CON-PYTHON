import tkinter as tk

ventana=tk.Tk()
ventana.title("Titulo")
ventana.geometry("300x150")
ventana.configure(
    bg="black"
)

etiqueta=tk.Label(
    ventana,
    text="Hola",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)

etiqueta.pack(pady=40)
ventana.mainloop()
