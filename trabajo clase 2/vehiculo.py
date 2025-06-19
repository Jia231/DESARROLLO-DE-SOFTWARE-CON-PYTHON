class Vehiculo:
    def __init__(self):
        self.marca = ""

    def definir_marca(self, marca):
        self.marca = marca

    def arrancar_vehiculo(self):
        print(f"Su vehiculo marca {self.marca} esta encendido!!!")