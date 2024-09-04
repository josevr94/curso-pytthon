class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    def information(self):
        return f"Informacion del animal:\nNombre: {self.nombre}\nRaza: {self.raza}\nEdad: {self.edad}\nPeso: {self.peso}"    
#main
# objeto 1
caballo = Animal("Zeus", 5, "Pura Sangre", 450)
#objeto 2
leon = Animal("Boulder", 10, "Atlas", 130)

print(caballo.information()) 
print(leon.information())          