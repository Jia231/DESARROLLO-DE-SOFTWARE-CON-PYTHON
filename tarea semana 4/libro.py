class Libro:
    def __init__(self, titulo, autor, publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion

    def getLibro(self):
        print(f"""
            Este libro se llama {self.titulo} 
            y fue escrito por {self.autor} en 
            el año {self.publicacion}
        """)