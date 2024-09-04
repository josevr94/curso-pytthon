class Cuenta:
    def __init__(self, titular, saldo = 0):
        self._titular = titular # el gion bajo antes del nombre titular indica que es un atributo protegido
        self._saldo = saldo #atributo protegido
        
    @property     #este es el getter el cual es una propiedad para poder ver los elementos portegidos
    def titular(self):
        return self._titular # la gracias del property es que me regrese el atributo protegido y poder usarlar en los metodos posteriores
    @property
    def saldo(self):
        return self._saldo #hay que hacer un property para cada atributo portegido
    @saldo.setter  # este es el setter el cual nos permite modificar los atributos protegidos 
    def saldo(self, cantidad):
        if cantidad < 0:
            print("El saldo no puede ser negativo")
        else:
            self._saldo = cantidad
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad    
            print(f"Se ha depositado ${cantidad}. Su nuevo saldo: ${self._saldo}")     
        else:
            print("Debe ingresar una cantidad positiva")       
    def retirar(self, cantidad): 
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Se ha retirado ${cantidad}. Su nuevo saldo: ${self._saldo}")
        else:
            print("Fondos insuficientes")    
