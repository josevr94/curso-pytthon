from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas,velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def agregar_objetoss(mensaje): # metodo para crear objetos por consola y agregarlos a una lista
        numero_autos = int(input(mensaje))
        lista_autos = []
        for auto in range(numero_autos):
            print(f'Datos del automovil {auto + 1}')
            marca = input('Inserte la marca del automovil: ')
            modelo = input('Insete el modelo: ')
            n_ruedas = int(input('Inserta el numero de ruedas:'))
            velocidad = float(input('Inserta la velocidad en km/h: '))
            cilindrada = float(input('Ingresa el cilindraje en cc: '))
            lista_autos.append(Automovil(marca,modelo,n_ruedas,velocidad,cilindrada))
        return lista_autos
           
         
    
    def mostrar_objetos(lista): # esta funcion muestra los objetos agregados por consola y con una lista 
        for i, auto in enumerate(lista,1):
            print(f'Datos del automovil {i} = Marca: {auto.marca} Modelo: {auto.modelo}  {auto.n_ruedas} ruedas  {auto.velocidad} km/h  {auto.cilindrada} cc')
        
    def mostrar_1(self): # mustra objetos creador y es un metod que se compartira con las otras clases
        a = Vehiculo.mostrar(self)
        return f'{a}, {self.velocidad} km/h, {self.cilindrada} cc'
           
        
    
    
# objetos = Automovil.agregar_objetoss('Ingresa el numero de autos: ')
# Automovil.mostrar_objetos(objetos)

# objeto = Automovil('toyota','yaris', 4, 120, 800)
# Automovil.mostrar(objeto)