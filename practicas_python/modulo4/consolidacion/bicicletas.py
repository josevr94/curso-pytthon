from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo_bicicleta = tipo_bicicleta
        
    def mostrarBicicletas(self):
        a = Vehiculo.mostrar(self)
        return f'{a}, {self.tipo_bicicleta}'    