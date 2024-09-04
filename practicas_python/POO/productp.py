class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        return f"El producto es: {self.nombre} \n-Precio: {self.precio},\n-cantidad: {self.cantidad}"
    def agregar_stock(self,cantidad):
        self.cantidad += cantidad    
        print(f"se han agregado: {cantidad} unidades de {self.nombre}, la cantidad actual es: {self.cantidad}")
    def vender(self,cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficicente stock de {self.nombre} solo hay {self.cantidad}")
        else:
            self.cantidad -= cantidad
            print(f"se han vendido {cantidad} del producto {self.nombre}, y quedan en stock: {self.cantidad}")  
# main
producto1 = Producto("Laptop", 1500, 10)
producto2 = Producto("Mesa", 200, 30)

# mostrammos los datos del producto
print(producto1.mostrar())  
print(producto2.mostrar())
# agregamos 10 unidades y mostramos el producto laptops
producto1.agregar_stock(10) 
print(producto1.mostrar())
# vendemos 15 unidades y mostramos el producto 2   
producto2.vender(15)
print(producto2.mostrar())
# vender 40 unidades y mostrar el producto
producto1.vender(40)
print(producto1.mostrar())