# Desafío: Implementación de un Carrito de Compras
# Instrucciones
# 1.	Crear una Clase Base Producto:
# o	Debe tener los atributos privados __nombre, __precio y __cantidad_en_stock.
# o	Debe tener propiedades nombre, precio y cantidad_en_stock para obtener y establecer los valores de estos atributos.
# o	La propiedad precio debe asegurar que el precio no sea negativo.
# o	La propiedad cantidad_en_stock debe asegurar que la cantidad en stock no sea negativa.
# 2.	Crear una Clase Carrito:
# o	Debe tener un atributo privado __productos que sea un diccionario donde la clave es el nombre del producto y el valor es una instancia de Producto.
# o	Debe tener un método agregar_producto(producto, cantidad) que agregue un producto al carrito.
# 	Si la cantidad solicitada excede la cantidad en stock, debe lanzar una excepción personalizada StockInsuficienteError.
# o	Debe tener un método eliminar_producto(nombre_producto) que elimine un producto del carrito.
# o	Debe tener un método calcular_total() que calcule y devuelva el costo total de los productos en el carrito.
# o	Debe tener un método mostrar_carrito() que imprima los productos en el carrito con sus cantidades y precios.
# 3.	Crear una Excepción Personalizada StockInsuficienteError:
# o	Esta excepción debe ser lanzada cuando se intente agregar una cantidad de un producto al carrito que exceda la cantidad disponible en stock.
# 4.	Prueba y Verificación:
# o	Crea varios productos, agrégalos al carrito, maneja excepciones si intentas agregar más de lo que hay en stock, calcula el total del carrito y elimina un producto.
class StockInsuficienteError(Exception): # declarando un excepcion personalizada
    pass
class Producto:
    def __init__(self, nombre, precio, cantidad_stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_stock = cantidad_stock
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad_stock(self):
        return self.__cantidad_stock
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor
    @cantidad_stock.setter
    def cantidad_stock(self,cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad en stock no puede ser negativa")
        self.__cantidad_stock = cantidad
    def reducir_stock(self,cantidad):
        if cantidad > self.__cantidad_stock:
            raise StockInsuficienteError(f"Stock insuficiente ")
        self.__cantidad_stock -= cantidad    
       
        
                    