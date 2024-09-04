import json #importamos la libreria json

with open('practicas_python/file/json/data.json', 'r') as file: #ocupamos el with para abrir el archivo
    datos = json.load(file) # aca guardamos el archivo en la variable datos (ocupamos json.load para trabajar con json)
nombre = datos['nombre'] 
edad = datos['edad']
correo = datos['correo'] # en todos estos casos, estamos recorriendo el diccionario del archivo json 
hobbies = datos['hobbies'] #  guardamos en la variable el dato del diccionario
trabajo = datos['trabajo'] # datos es el nombre del archivo y nombre, edad, correo, etc. son las keys del diccionario 
                           # y lo que guardamos en la cariable es el valor de la key
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'correo: {correo}') 
print(f'hobbies: {hobbies}')
print(f'trabajo: {trabajo}')  
print(f'el trabajdor: {nombre} tiene un puesto de: {trabajo['puesto']} y lleva {trabajo['años']} años')
