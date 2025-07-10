import tkinter as tk

def iniciar_cuenta():
     global segundos_restantes
     segundos_restantes = int(entrada_texto.get())
     entrada_texto.config(state=tk.DISABLED)
     boton.config(state=tk.DISABLED)    
     actualizar_contador()

def actualizar_contador():
     global segundos_restantes
     if segundos_restantes > 0: 
          segundos_restantes = segundos_restantes - 1
          etiqueta_resultado.configure(text=f"Segundos restantes {segundos_restantes}")
          ventana.after(1000, actualizar_contador)
     else:
          etiqueta_resultado.configure(text=f"Se acabo el tiempo")     
          entrada_texto.config(state=tk.NORMAL)
          boton.config(state=tk.NORMAL)
          entrada_texto.delete(0, tk.END)   

ventana=tk.Tk()
ventana.title("Contador de segundos")
ventana.geometry("400x200")
ventana.configure(bg="black")

entrada_texto=tk.Entry(ventana)
entrada_texto.pack()
boton=tk.Button(ventana, text="Iniciar temporizador", command=iniciar_cuenta)
boton.pack()

etiqueta_resultado=tk.Label(
    ventana,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f1f2f6",
    fg="#5772df"
)
etiqueta_resultado.pack(pady=10)
ventana.mainloop()
