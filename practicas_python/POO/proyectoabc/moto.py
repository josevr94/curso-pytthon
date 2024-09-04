from vehiculos import Vehiculos
class Moto(Vehiculos):
    def __init__(self, marca, modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio= anio
    def mostrar_detalle(self): 
        return f"La moto: {self.marca} , Modeloe{self.modelo}, anio:{self.anio}"
    def encender(self):
        return print(f"La moto es: {self.marca},{self.modelo} esta arrancando")   