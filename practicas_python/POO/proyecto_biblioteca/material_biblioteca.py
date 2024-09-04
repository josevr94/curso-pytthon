
# Objetivo
# Crea un sistema simple de gestión de libros en una biblioteca. Este sistema debe incluir diferentes tipos de materiales (libros, revistas, y periódicos), cada uno con sus características y comportamiento específicos.utilizando conceptos de programación orientada a objetos como clases, herencia, atributos, propiedades y métodos.
# Estructura del Desafío
# 1.	Clase Base - MaterialBiblioteca
# o	Atributos de Instancia:
# 	titulo: El título del material (ej., "El Hobbit").
# 	autor: El autor del material (ej., "J.R.R. Tolkien").
# 	año_publicacion: El año en que el material fue publicado (ej., 1937).
# o	Propiedad año_publicacion:
# 	Utiliza un método getter para obtener el año de publicación.
# 	Utiliza un método setter para asegurar que el año de publicación no sea un valor futuro. Si se intenta establecer un año en el futuro, se lanza una excepción ValueError.
# o	Método informacion:
# 	Devuelve una cadena con la información básica del material: título, autor y año de publicación.
# 2.	Clase Derivada - Libro
# o	Hereda de MaterialBiblioteca.
# o	Atributos Adicionales:
# 	numero_paginas: El número de páginas del libro (ej., 310).
# o	Método informacion:
# 	Sobreescribe el método de la clase base para incluir también el número de páginas en la descripción del libro.
# 3.	Clase Derivada - Revista
# o	Hereda de MaterialBiblioteca.
# o	Atributos Adicionales:
# 	numero_edicion: El número de edición de la revista (ej., 800).
# o	Método informacion:
# 	Sobreescribe el método de la clase base para incluir también el número de edición en la descripción de la revista.
# 4.	Clase Derivada - Periodico
# o	Hereda de MaterialBiblioteca.
# o	Atributos Adicionales:
# 	fecha: La fecha específica de la publicación del periódico (ej., "15-08-2024").
# o	Método informacion:
# 	Sobreescribe el método de la clase base para incluir también la fecha de publicación en la descripción del periódico.
# 5.	Instanciación y Uso
# o	Crea instancias de las clases Libro, Revista, y Periodico con datos de ejemplo.
# o	Ajusta y accede a los atributos utilizando propiedades.
# o	Imprime la información de cada material utilizando el método informacion.
# Ejemplo de Funcionamiento
# 1.	Definición de Clases:
# o	Se definen las clases base y derivadas, cada una con sus atributos y métodos específicos.
# 2.	Método main:
# o	Se crean objetos de las clases Libro, Revista, y Periodico.
# o	Se imprime la información de cada objeto, demostrando el uso de herencia y métodos sobreescritos.
# 3.	Salida Esperada:
# o	La salida muestra la información completa de cada material, incluyendo los atributos adicionales específicos de cada tipo de material.
# Este desafío te ayudará a comprender cómo utilizar la herencia y las propiedades en Python, además de cómo extender el comportamiento de una clase base en clases derivadas.
# Título: El Hobbit, Autor: J.R.R. Tolkien, Año de Publicación: 1937, Número de Páginas: 310
# Título: National Geographic, Autor: Varios, Año de Publicación: 2023, Número de Edición: 800
# Título: El País, Autor: Varios, Año de Publicación: 2024, Fecha: 15-08-2024

class MaterialBiblioteca:
    def __init__(self, titulo, autor, año_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._año_publicacion = año_publicacion 
    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def año_publicacion(self):
        return self._año_publicacion
    @año_publicacion.setter
    def año_publicacion(self, fecha):
        if fecha > 2023:
            return ValueError
        else:
            print(f"El año del publicacion es {self.año_publicacion}")
    def informacion(self):
        return print(f"El libro: {self.titulo} fue escrito por el autor {self.autor} en el año {self.año_publicacion}")    