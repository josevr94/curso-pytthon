from automovil import Automovil

class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, p_carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.p_carga = p_carga
        
        
    def mostrarAuto_carga(self):
        a = Automovil.mostrar_1(self)
        return f'{a}, {self.p_carga}'    