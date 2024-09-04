from vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    def abrir_puertas(self):
        print(f"El coche {self.marca} {self.modelo} con {self.num_puertas} puertas abrio las puertas")    