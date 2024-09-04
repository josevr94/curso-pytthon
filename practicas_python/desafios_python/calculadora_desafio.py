# Crea una función llamada calcular_precio_final que reciba dos parámetros:
 
# precio_inicial: el precio original del producto.
# descuento: el porcentaje de descuento a aplicar (un número entre 0 y 100).
# La función debe devolver el precio final del producto después de aplicar el descuento.
 
# Asegúrate de que la función maneje correctamente los siguientes casos:
 
# Si el descuento es 0, el precio final debe ser igual al precio inicial.
# Si el descuento es 100, el precio final debe ser 0.
# El descuento no puede ser negativo ni mayor que 100; en esos casos, la función debe devolver el mensaje "Descuento inválido".
# Escribe un código que solicite al usuario que ingrese el precio inicial y el descuento, y luego muestre el precio final utilizando la función calcular_precio_final
# # tiene menú contextual

def calculadora_precio_final(a,b):
    a = int(input("ingresa el precio original del producto: "))
    b = float(input("ingresa el porcentaje del descuento"))
    return a,b
def con_descuento(a,b):
    return  a*((100-b)/100)


    