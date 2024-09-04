from producto import Producto
from carrito import Carrito

try:
    p1 = Producto("Laptop", 100, 5)
    p2 = Producto("Smartphone", 500, 10)
    p3 = Producto("Diadema", 150, 2)
    carrito = Carrito()
    carrito.agregar_productos(p1, 2)
    carrito.agregar_productos(p2, 2)
    carrito.agregar_productos(p3, 2)
    carrito.mostrar_carrito()
    
    
except ValueError as e:
    print(f"Error: {e}")    