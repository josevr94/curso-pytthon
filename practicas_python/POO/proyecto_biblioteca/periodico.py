from material_biblioteca import MaterialBiblioteca
class Periodico(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, fecha_publicacion):
        super().__init__(titulo, autor, año_publicacion)
        self._fecha_publicacion = fecha_publicacion
    @property
    def fecha_publicacion(self):
        return self._fecha_publicacion
    @fecha_publicacion.setter
    def fecha_publicacion(self, fecha_publicacion):
        if fecha_publicacion > "00/00/0000":
            print("El numero de edicion no puede ser inferior a 00/00/0000")
        else:
            self._fecha_publicacion = fecha_publicacion
    
    
    
    def informacion(self):
        return print(f"El Periodico: {self.titulo}\nFue escrito por  {self.autor}\nFue publicado en: {self.fecha_publicacion}")   