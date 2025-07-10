import tkinter as tk
from tkinter import filedialog
 
# Función para guardar el contenido del área de texto
def guardar_archivo():
    contenido = area_texto.get("1.0", tk.END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if archivo:
        archivo.write(contenido)
        archivo.close()
 
# Crear ventana principal
ventana = tk.Tk()
ventana.title("📝 Editor de Texto Simple")
ventana.geometry("600x400")
ventana.configure(bg="#f3e5f5")  # Fondo lila claro
 
# Área de texto con estilo
area_texto = tk.Text(
    ventana,
    wrap="word",
    font=("Consolas", 12),
    bg="#ffffff",
    fg="#4a148c",
    insertbackground="#6a1b9a"  # Color del cursor
)
area_texto.pack(padx=10, pady=10, expand=True, fill="both")
 
# Botón para guardar el contenido
boton_guardar = tk.Button(
    ventana,
    text="💾 Guardar",
    command=guardar_archivo,
    font=("Arial", 11, "bold"),
    bg="#7b1fa2",      # Morado oscuro
    fg="white",
    activebackground="#4a0072",
    padx=10,
    pady=5
)
boton_guardar.pack(pady=10)
 
# Iniciar la aplicación
ventana.mainloop()
 