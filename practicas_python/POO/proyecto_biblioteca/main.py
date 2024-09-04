from libro import Libro
from periodico import Periodico    # si tengo varias sub clases tengo que importarlas todas 
from revista import Revista
def main():
    libro1 =Libro ("Asi hablo zaratustra","Nietzsche",1883, 443)
    print(libro1.informacion()) # para poder traer el metodo q hice antes, tengo que poner el objeto.metodo()
    periodico1= Periodico("La Tercera", "tercera", 1994, "24/10/2022")    
    print(periodico1.informacion()) 
    revista1 = Revista("Vogue","juanito perez",2000,200)
    print(revista1.informacion())
    
    
if __name__ == "__main__":
    main()    