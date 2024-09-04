class GestorTareas:
    def __init__(self,archivo_tareas="file/ejemplos_textos/tareas.txt"):    
        self.archivo_tareas = archivo_tareas
        
    def anadir_tareas(self,tarea):
        with  open(self.archivo_tareas,'a') as archivo:
            archivo.write(tarea + '\n')
        print("Tarea agregada con exito")    
    def mostrar_tareas(self,archivo_tareas):
        try:        
            with open(self.archivo_tareas, 'r') as f:           
                contenido = f.read()
                        
        except FileNotFoundError:
            print(f"El archivo {archivo_tareas} no se encuentra.")            
        return contenido 
    def contar_lineas(self, archivo_tareas):           
        with open(archivo_tareas, 'r') as f:
            tareas = f.readlines()
        print(f"Número total de tareas: {len(tareas)}")
        return len(tareas) 
    def buscar_remplazar(self,archivo_tareas,tarea_cambiar,tare):
        try:
            with open(self.archivo_tareas, "r") as f:
                contenido = f.read()
                
            
            
        except FileNotFoundError:
            print(f"El archivo {archivo_tareas} no se encuentra.")               
def main():
    gestor = GestorTareas()
    while True:
        print("\n--------Menu-----------")
        print("1.Anadir Tarea")
        print("2.Mostrar Tarea")
        print("3.Contar numero de Tareas")
        print("4.Buscar y remplanzar")
        print("5.Hacer Respaldo")
        print("6.Salir")
        opcion = int(input("Elige una opcion: "))
        if (opcion == 1):
            tarea = input("Ingresa una nueva tarea")
            gestor.anadir_tareas(tarea)
        elif (opcion == 2):
            contenido = gestor.mostrar_tareas(gestor.archivo_tareas)
            if contenido == " ":
                print("No hay tareas en la lista.")
            print(contenido)    
        elif (opcion == 6):
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida")    

if __name__ == '__main__':
    main()