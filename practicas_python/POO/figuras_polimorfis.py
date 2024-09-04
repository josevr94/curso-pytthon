class Figuras:
    def __init__(self,lado,n_lados):
        self.lado = lado
        self.n_lados = n_lados
    def calcular_perimetro(self):
        return self.lado * self.n_lados
class Cuadrado(Figuras):
    def __init__(self,lado, n_lado):
        super().__init__(lado, n_lado)   
    
class Pentagono(Figuras):
    def __init__(self,lado, n_lado):
        super().__init__(lado, n_lado)   
    
class Exagono(Figuras): 
    def __init__(self,lado, n_lado):
        super().__init__(lado, n_lado)  
      
class Octagono(Figuras):
    def __init__(self,lado, n_lado):
        super().__init__(lado, n_lado)
        

cuadrado = Cuadrado(4, 4)    
octagono = Octagono(5, 8)
pentagono= Pentagono(3, 5)
exagono = Exagono(7, 6)

print(cuadrado.calcular_perimetro())
print(octagono.calcular_perimetro())
print(pentagono.calcular_perimetro())
print(exagono.calcular_perimetro())
    
    