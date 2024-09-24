class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
    
    def get_edad(self):
        return self.edad
    def get_apellido(self):
        return self.apellido
    def set_edad(self, edad):
        self.edad = edad
    def set_apellido(self, apellido):
        self.apellido = apellido
        
# main 
# objeto 1
persona_1 = Persona("Pedro", "vivas", "Mascilino", "20 años", "1.78 mts", "68 kg")
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, "1.8 mts", "75 kg")

print(persona_1.get_edad())
persona_1.set_edad("21 años")
print(persona_1.get_edad())  
print(persona_2.get_apellido())  
persona_2.set_apellido("Santiago")
print(persona_2.get_apellido())           