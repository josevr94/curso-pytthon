from vehiculo import Vehiculo
from automovil import Automovil
from automovil_particular import AutomovilParticular
from automovil_carga import AutomovilCarga
from bicicletas import Bicicleta
from motocicletas import Motocicletas
import csv

class Vehiculoscsv: 
    def __init__(self,nombre_archivo = 'practicas_python/modulo4/consolidacion/csv/archivo.csv'):
        self.nombre_archivo = nombre_archivo
        self.vehiculo_particular = []
        self.vehiculo_carga = []
        self.bicicletas = []
        self.motocicletas = []
    
       
    def guardar_datos_csv(self,objeto):
        try:
            with open(self.nombre_archivo, mode = 'a', newline= '') as file:
                dato = [objeto.__class__, objeto.__dict__]
                archivo_csv = csv.writer(file)
                archivo_csv.writerow(dato)
                return print('Archivo guardado')
        
        except FileNotFoundError:
            print('Archivo no encontrado')       
        
   
         
    def leer_datos_csv(self):
        vehiculos = []
        try:
            with open(self.nombre_archivo, mode="r", newline="") as file:
                lector = csv.reader(file)
                for vehiculo in lector: 
                    vehiculos.append(vehiculo)
                                            
        except FileNotFoundError:
            print('El archivo no fue encontrado')
        return vehiculos
    
    def mostrar_datos(self,vehiculos):
        print('Vehículos Particulares:')
        for vehiculo in vehiculos:
            if vehiculo[0] == "<class 'automovil_particular.AutomovilParticular'>":
                print(vehiculo[1])
        print('Vehículos de carga:') 
        for vehiculo in vehiculos:   
            if vehiculo[0] == "<class 'automovil_carga.AutomovilCarga'>":
                print(vehiculo[1])
        print('Bicicletas:') 
        for vehiculo in vehiculos:   
            if vehiculo[0] == "<class 'bicicletas.Bicicleta'>":
                print(vehiculo[1])
        print('Motocicletas:') 
        for vehiculo in vehiculos:   
            if vehiculo[0] == "<class 'motocicletas.Motocicletas'>":
                print(vehiculo[1])       

gestor = Vehiculoscsv()    
      
particular = AutomovilParticular('Ford', 'Fiesta', 4, 180, 500, 5)
carga = AutomovilCarga('Daft Trucks', 'G 38', 10, 120, 1000, 20000)
bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
motocicleta = Motocicletas('BMW', 'F800s', 2, 'Deportiva', '2T','Doble Viga', 21)
bicicleta2 = Bicicleta('p3','pistera', 2, 'carrera')
lista_objeto = [particular,carga,bicicleta,motocicleta, bicicleta2]

for lista in lista_objeto:
    gestor.guardar_datos_csv(lista)
# gestor.guardar_datos_csv(lis)
vehiculos = gestor.leer_datos_csv()
# for vehiculo in vehiculos:
#     print(vehiculo)

gestor.mostrar_datos(vehiculos) 