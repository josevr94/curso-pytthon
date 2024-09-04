from vehiculo import Vehiculo
from automovil import Automovil
from automovil_particular import AutomovilParticular
from automovil_carga import AutomovilCarga
from bicicletas import Bicicleta
from motocicletas import Motocicletas
from vehiculos_cvs import Vehiculoscsv
particular = AutomovilParticular('Ford', 'Fiesta', 4, 180, 500, 5)
carga = AutomovilCarga('Daft Trucks', 'G 38', 10, 120, 1000, 20000)
bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
motocicleta = Motocicletas('BMW', 'F800s', 2, 'Deportiva', '2T','Doble Viga', 21)

lista_objeto = [particular,carga,bicicleta,motocicleta]

def relacion_instancias():
        print(f'Motocicleta es instancia con relacion a Automovil: {isinstance(motocicleta,Automovil)}') 
        print(f'Motocicleta es instancia con relacion a Automovil de Carga: {isinstance(motocicleta,AutomovilCarga)}') 
        print(f'Motocicleta es instancia con relacion a Automovil Particular: {isinstance(motocicleta,AutomovilParticular)}') 
        print(f'Motocicleta es instancia con relacion a Bicicleta: {isinstance(motocicleta,Bicicleta)}') 
        print(f'Motocicleta es instancia con relacion a Vehiculo: {isinstance(motocicleta,Vehiculo)}') 
        print(f'Motocicleta es instancia con relacion a Motocicleta: {isinstance(motocicleta,Motocicletas)}') 

def imprimir_objetos():
    AutomovilParticular.mostrarAuto_particular(particular)
    AutomovilCarga.mostrarAuto_carga(carga)
    Bicicleta.mostrarBicicletas(bicicleta)
    Motocicletas.mostrarMoto(motocicleta)
      
def main():
    gestor = Vehiculoscsv()
    while True:
        respuesta = int(input('------Menu Practica Consolidacion------\n1.- Parte 1: Crear objetos mediante la consola\n2.- Mostrar los objetos creados\n3.-Parte 2: Usar los objetos previamente creados y mostralos en terminal\n4.-Verificar la relacion de las instancias\n5.-Guardar objetos en archivo csv\n6.-Mostrar archivo csv\n7.-Salir\nIngresa tu opcion:   '))
        if respuesta == 1:
            objetos_creadosConsola = Automovil.agregar_objetoss('Ingresa el numero de autos: ')
            print('Objetos agregados')
        if respuesta == 2:
            Automovil.mostrar_objetos(objetos_creadosConsola)    
        if respuesta == 3:
           print(imprimir_objetos())
        if respuesta == 4:
            relacion_instancias()  
        if respuesta == 5:
            for lista in lista_objeto:
                gestor.guardar_datos_csv(lista)
        if respuesta == 6:
            gestor.leer_archivo()
        if respuesta == 7:
            break    
    
if __name__ == '__main__':
    main()    