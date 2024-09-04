from material_biblioteca import MaterialBiblioteca
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_paginas ):
        super().__init__(titulo, autor, año_publicacion)
        self._numero_paginas = numero_paginas
    @property
    def numero_paginas(self):
        return self._numero_paginas
    @numero_paginas.setter
    def numero_paginas(self, numero_paginas):
        if numero_paginas > 0:
            print("El numero de paginas no puede ser inferior a 0")
        else:
            self._numero_paginas = numero_paginas
    def informacion(self):
        return print(f"El libro: {self.titulo}\nFue escrito por el autor: {self.autor}\nTiene {self.numero_paginas} pag.\nFue publicado en el año {self.año_publicacion}")       
        