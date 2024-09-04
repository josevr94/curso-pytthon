class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print(f"El vehiculo {self.marca}, con modelo {self.modelo} ha arrancado")  
    def detener(self):
        print(f"El vehiculo {self.marca}, con modelo {self.modelo} se ha detenido")