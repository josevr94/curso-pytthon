class Libro:
    def __init__(self, autor, titulo ):
        self.autor = autor
        self.titulo = titulo
    def _dict_(self):
        return {'autor': self.autor, 'titulo': self.titulo }    
    
class Libro_ann_publicacion(Libro):
    def __init__(self, autor, titulo, ann_public):
        super().__init__(autor,titulo)
        self.ann_public = ann_public 
    
    def _dict_(self):
        return {'autor': self.autor, 'titulo': self.titulo, 'año_publicacion': self.ann_public } 
    
# main

libro1 = Libro('Dan Brown', 'Inferno')
libro2 = Libro_ann_publicacion('Dan Brown', 'El Codigo Da Vinci', 2003)   

print(libro1._dict_())
print(libro2._dict_())