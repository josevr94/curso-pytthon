class A:
    def __init__(self):
        print('Pertenezco a la clase A')
    def metodo_a(self):
        print('Metodo heredado de A')
      
class B:
    def __init__(self):
        print('Clase B')
    def metodo_b(self):
        print('Metodo heredado de B')  
        
class C(B, A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)    
        
    def metod_c(self):
        A.metodo_a(self)
        B.metodo_b(self)       
        print('Metodo es de C')    
        

      
# main

c = C()          
c.metod_c()                    