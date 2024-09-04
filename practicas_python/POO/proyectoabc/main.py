
from auto import Coche
from moto import Moto
#Main 
#invocar las clase coche   
mi_coche =Coche("Toyota","Yaris","2017")#Crear objeto coche

print(mi_coche.arrancar())

mi_moto = Moto("Yamaha","XR","2020")
mi_moto2 = Moto("Ducatti","Multiestraba","2023")
print(mi_moto.mostrar_detalle())
print(mi_moto2.mostrar_detalle())
mi_moto.encender()
mi_moto2.encender()