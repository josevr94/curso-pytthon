# el metodo de abstraccion se usa creando una clase abstracta que tendra metodos que tenemos que heredarlos a las sub clases
# la diferencia de esto con lo visto anterior, es que el metodo de abstraccion nos obliga a que todas las sub clases tengan la misma funcion que tiene la clase padre
# esto nos ayuda a evitar cometer errores de no heredar algun metodo impresindible 
# la clase abstract es un tipo de plantilla para guiar a las sub clases , es una forma de programar
from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass
#sub clase de MetodoPago la cual debe tener el metodo procesar_pago para que funcione el codigo    
class Pago_Tarjeta_Credito(MetodoPago):
    def procesar_pago(self, cantidad):  
        print(f"Procesando un pago de la ${cantidad} con tarjeta de credito")
#sub clase de MetodoPago la cual debe tener el metodo procesar_pago para que funcione el codigo            
class Pago_Paypal(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando un pago de la ${cantidad} con PayPal")
#sub clase de MetodoPago la cual debe tener el metodo procesar_pago para que funcione el codigo          
class PagoCriptomonedas(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando un pago de la ${cantidad} con criptomonedas")                  
        
def realizar_pago(metodo_pago, cantidad):
    metodo_pago.procesar_pago(cantidad)        
    
    
# main

pago1 = Pago_Tarjeta_Credito()    
pago2 = Pago_Paypal()
pago3 = PagoCriptomonedas()

realizar_pago(pago1, 100)
realizar_pago(pago2, 200)
realizar_pago(pago3, 300)