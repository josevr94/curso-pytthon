from bicicletas import Bicicleta

class Motocicletas(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, n_ruedas, tipo_bicicleta)
        self.nro_radio = nro_radios
        self.cuadro = cuadro
        self.motor = motor
        
    def mostrarMoto(self):
        a = Bicicleta.mostrarBicicletas(self)
        return f'{a}, {self.nro_radio}, {self.cuadro}, {self.motor}'  
      
    
        


    