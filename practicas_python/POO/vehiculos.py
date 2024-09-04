class Auto:
    def __init__(self,marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def describir(self):
        return f"Auto: {self.marca},\nModelo {self.modelo} \naño: {self.año}" 
    def arrancar(self):
        return f"El {self.marca}, {self.modelo} esta arrancando"
class Moto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar_detalles(self):
        return f"Moto: {self.marca},\nModelo: {self.modelo} \naño: {self.año}"
    def encender(self):
        return f"La {self.marca}, {self.modelo} esta encendida"        
    
# main    
mi_auto = Auto("Mazda","cx-5","2020")
print(mi_auto.describir())
print(mi_auto.arrancar())

mi_moto = Moto("Yamaha","XR","2023")
mi_moto2 = Moto("Ducatti","Multistraba","2023")
print(mi_moto.mostrar_detalles())
print(mi_moto.encender())
print(mi_moto2.mostrar_detalles())
print(mi_moto2.encender())