class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    def description(self):
        return f"{self.nombre} es de raza {self.raza} tiene {self.edad} años y pesa {self.peso}"    
    def comer(self):
        return f"{self.nombre} esta comiendo"
    def caminar(self):
        return f"{self.nombre} esta caminando"
    def dormir(self):
        return f"{self.nombre} esta durmiendo"
    
# objetos

perro = Animal("Brando","San Bernardo", 3, 30)
gato = Animal("Roll", "Persa", 4, 3)

# llamar   

print(perro.description())
print(gato.description())

# instancias perro
print(perro.comer())
print(perro.caminar())
print(perro.dormir())

#  instancias gato
print(gato.comer())
print(gato.caminar())
print(gato.dormir())