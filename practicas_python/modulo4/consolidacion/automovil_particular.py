from automovil import Automovil

class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puestos = n_puestos
    
    def mostrarAuto_particular(self):
        a = Automovil.mostrar_1(self)
        return f'{a}, Puestos: {self.n_puestos}'    
    
# objeto = AutomovilParticular('toyota','yaris', 4, 120, 800, 5)
# print(AutomovilParticular.mostrarAuto_particular(objeto) )  