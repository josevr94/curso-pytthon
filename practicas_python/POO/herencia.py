class Persona: #este es mi constructor con este elemento partimos siempre el codigo de clases
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    def description(self):
        return f"El nombre es: {self.nombre} tiene la edad: {self.edad}"   
class Empleado(Persona): # aca tenemos una clase hija de clase persona 
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad) # con el super() heredamos los elementos de la variable padre, que seria nombre y edad
        self.salario = salario # aca agregamos un nuevo elemento a nuestra clase hija 
        
    def description(self):
        return f"{super().description()} y gana {self.salario} dolares al mes" # aca estamos usando un metodo que esta definido en la clase padre 
    
    
    # main
empleado = Empleado("jose", 29, 400) # objeto
print(empleado.description())
        
class Ventas:
    def __init__(self, id):
        self.id = id
        id = 100

val = Ventas(456)
print (val.id)