from material_biblioteca import MaterialBiblioteca
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self._numero_edicion = numero_edicion
    @property
    def numero_edicion(self):
        return self._numero_edicion
    @numero_edicion.setter
    def numero_edicion(self, numero_edicion):
        if numero_edicion > 0:
            print("El numero de edicion no puede ser inferior a 0")
        else:
            self._numero_edicion = numero_edicion
    
    
    
    def informacion(self):
        return print(f"La revista: {self.titulo}\nFue escrito por el autor: {self.autor}\nEl numero de la edicion es: {self.numero_edicion}\nFue escrita en el año {self.año_publicacion}")           