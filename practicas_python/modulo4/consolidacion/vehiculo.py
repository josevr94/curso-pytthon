class Vehiculo:
    def __init__(self,marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas
    
    def mostrar(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas'    