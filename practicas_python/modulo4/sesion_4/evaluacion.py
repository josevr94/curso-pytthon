class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def movimiento(self):
        return f'La {self.nombre} esta caminando'
    
class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def movimiento(self):
        return f'La maratonista {self.nombre} esta trotando'   
    
class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def movimiento(self):
        return f'La ciclista {self.nombre} esta rodando'    

def llamado(objeto):    
    return print(objeto.movimiento())


# main
persona = Persona('jose')
ciclista = Ciclista('belen')
maratonista = Maratonista('violeta') 

  
lista = [persona, ciclista, maratonista]

for personas in lista:
    llamado(personas)        