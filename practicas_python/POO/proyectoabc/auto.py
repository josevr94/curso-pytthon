from vehiculos import Vehiculos
class Coche(Vehiculos):
    def __init__(self, marca, modelo,anio):
        self.marca =marca
        self.modelo = modelo
        self.anio = anio
    def encender(self):
        return print(f"El coche {self.marca}, {self.modelo} del año {self.anio} esta encendido")
    def arrancar(self):
        return f"El {self.marca},{self.modelo} esta arrancando"  