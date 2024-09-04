class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre #esto seria un atributo de tipo publico
        self._despartamento = None #esto seria un atributo de tipo protegido
        self.__salario = salario #esto seria un atributo de tipo privado
        
    @property
    def salario(self):
        return self.__salario    

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser positivo")   
    
    def _asignar_departamento(self, departamento):
        self._departamento = departamento 
        
    def _calcular_bonus(self):
        return self.__salario * 0.1           
            
            
#main
empleado = Empleado("jose", 200)
print(empleado.nombre) #acceso directo a un atributo publico
empleado.salario = 550 #uso del setter (mediante el metodo setter podemos modificar este valor)
print(empleado.salario) #uso del getter  (mediante el getter podemos imprimir este elemento)
empleado._asignar_departamento("ventas")#uso de metodo protegido
print(empleado._departamento)
print(empleado.__salario) #esto mandaria error porq es un elemento privado y estoy intentando imprimir de forma directa la variable, saltandome el getter, por eso no funciona
         