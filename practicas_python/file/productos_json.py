import json

# leer archivo
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# escribir en el archivo json
def write_json(filename, jsdata): # aca se pide la dirección del archivo y la informacion que voy a guardar en la direccion que agrege (es para sobreescribir o crear un archivo nuevo si no existe)
    with open(filename, 'w') as file:
        data = json.dump(jsdata, file, indent=4)
        
# agregar productos
def add_productos(data, product):
    data['products'].append(product)

# actualizar la cantidad de productos existentes
def update_productos(data, product_id,new_quantity):   
    for product in data['products']:
        if product['id'] == product_id:
            product['quantity'] = new_quantity
            break
        

#Eliminar un producto
def remover_producto(data, product_id):
    data['products'] = [product for product in data['products'] if product['id']!= product_id]  # este metodo se llama comprension de lista ,que es una forma de escribir todo en una sola linea

# mostrar productos
def mostrar_productos(data):
    print('Lista de productos')
    for product in data['products']:
        print(f"ID: {product['id']}, Nombre: {product['name']}, Cantidad: {product['quantity']}")
        
# main
filename = 'practicas_python/file/json/products.json'        
data = read_json(filename)
mostrar_productos(data)

update_productos(data,2,30)
mostrar_productos(data)

remover_producto(data,1)
mostrar_productos(data)

write_json(filename,data)

nuevo_producto ={'id': 6, 'name': 'taza', 'price' : 5.5, 'quantity': 15}
add_productos(data, nuevo_producto)

write_json(filename,data)
nuevo_producto2 ={'id': 7, 'name': 'pantalla', 'price' : 20, 'quantity': 5}
add_productos(data, nuevo_producto2)

write_json(filename,data)
