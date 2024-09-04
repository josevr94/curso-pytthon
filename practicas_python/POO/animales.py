class Dog:
    def __init__(self,name,raza):
        self.name = name
        self.raza = raza
    def ladrar(self):
        print(f"El perro {self.name} dice woof! y es de raza {self.raza}")
    def salir(self):
        print(f"Al perro {self.name} le gusta mucho salir a correr  ")  
    def comer(self):
        print(f"Al perro {self.name} le gusta comer comida de casas y no su pellet")      

#principal o main 

perro=Dog("Dune","Quiltro")   
perro.ladrar()         
perro.comer() 
perro.salir() 