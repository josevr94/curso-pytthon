#clase libro
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#clase periodico
class Newspaper:
    def __init__(self,title):
        self.title = title
#clase revista
class Revista:
    def __init__(self,title,author):
        self.title=title
        self.author=author    
    


#main (traer a la clase) 
#creando objetos
book1= Book("100 años de soledad", "Garcia MArquez")
book2= Book("codigo limpio","Juan Peresz")  
periodico = Newspaper("el universo")   
periodico2 = Newspaper("times")
revista1= Revista("vogue","Arthur Baldwin Turnure")  
revista2= Revista("National  Geographic","Gardiner Green Hubbard")




#invocando objetos de la clase book
print(book1)
print(book2)
print(book2.title)   
print(book1.author) 
print(book2.author)

#invocando objetos de la clase newspaper
print(periodico.title)
print(periodico2.title)

#imprimiendo la clase revista
print(revista1.title)
print(revista2.title)
print(revista1.author)
print(revista2.author)