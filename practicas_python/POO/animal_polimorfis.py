class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu!"
def animal_sonido(objeto): #este metodo se crea para que funcione con todas las clases, la gracias es que animal_sonido() entre los parentecis va un objeto, el que yo quiera (que cree abajo) 
    print(objeto.hacer_sonido()) # entonces al poner mi objeto entre esos parentecis va ir a buscar la clase a la que pertenece mi objeto y a buscar la funcion que se llame hacer_sonido() y va a imprimir el return que posee el metodo de la clase que mande a buscar   
    
perro = Perro()
gato = Gato()
vaca = Vaca()
animal_sonido(perro) # aca ya estaria listo y usando el metdo creado para traer el sonido, solo tengo que poner mi objeto, en este caso perro y se ira a buscar a que clase pertenece y buscar el hacer_sonido que tiene esa clase 
animal_sonido(gato)
animal_sonido(vaca)
print(perro.hacer_sonido()) # para acceder a una metodo que esta dentrode una clase tengo que poner al (objeto.metodo)
#esto de abajo es lo mismo que arriba pero con un bucle para que se recorra la lista y no tener q hacerlo uno por uno 
animales = [Perro(), Gato(), Vaca(), Perro()]
for animal in animales:  
    animal_sonido(animal)             