class StockInsuficienteError(Exception): # declarando un excepcion personalizada
    pass
class Carrito:
    def __init__(self):
        self.productos = {}
    def agregar_productos(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:    
            self.productos[producto.nombre] = {"producto": producto, "cantidad": cantidad}
        try:
            producto.reducir_stock(cantidad)
        except StockInsuficienteError as e:
            print(f"Error al agregar_producto: {producto.nombre} al carrito: {e}")
            self.productos[producto.nombre]["cantidad"]   
    def eliminar_producto(self, nombre_producto):       
        if nombre_producto in self.productos:
            del self.productos[nombre_producto] 
        else:
            print("no existe el producto a eliminar")    
    
    def calcular_total(self):
        total = 0
        for item in self.productos.values():
            total += item["producto"].precio * item["cantidad"]
        return total
    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío")  
            return
        print("carrito de compras")
        for item in self.productos.values():
            producto = item["producto"]                 
            cantidad = item["cantidad"]
            print(f"{producto.nombre} - Cantidad: {cantidad}, Precio: ${producto.precio}")
        print(f"Total: ${self.calcular_total()}")    