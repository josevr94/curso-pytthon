from coche import Coche #esto seria desde el archivo coche, traer la subclase Coche

def main():
    mi_coche = Coche("Toyota", "Yaris", 4)
    mi_coche.arrancar()
    mi_coche.abrir_puertas()
    mi_coche.detener()
    
if __name__ == "__main__": # esta funcion es para poder combinar todo, es importante ponerla para que funcione 
    main()    