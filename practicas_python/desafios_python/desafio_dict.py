# Vas a crear un programa para obter informacion de un contacto. El programa debe:

# Obtener información del contacto desde la consola.
# Almacenar la información en un diccionario.
# Realizar algunas operaciones básicas con los datos almacenados.
# Imprimir los resultados.
# Requisitos:

# Obtener Datos de Consola:

# Usa input() para obtener el nombre,  el correo electrónico y 
# el número de teléfono del contacto.
# Almacenar Datos:

# Almacena la información en un diccionario.
# Operaciones Básicas:

# Calcula el número total de caracteres en el nombre del contacto.
# Imprime la información completa del contacto.
















# Inicializar Diccionario de Contacto
contacto = {}

# Obtener Datos de Consola
nombre_contacto = input("Ingrese el nombre del contacto: ")
correo_contacto = input("Ingrese el correo electrónico del contacto: ")
telefono_contacto = input("Ingrese el número de teléfono del contacto: ")

# Almacenar Información en el Diccionario
contacto['nombre'] = nombre_contacto
contacto['correo'] = correo_contacto
contacto['telefono'] = telefono_contacto

# Realizar Operaciones Básicas
# Calcular el número total de caracteres en el nombre
total_caracteres_nombre = len(nombre_contacto)

# Imprimir Información del Contacto
print("\nInformación del Contacto:")
print("Total de caracteres en el nombre:", total_caracteres_nombre)
print(f"Nombre: {contacto['nombre']}")
print(f"Correo: {contacto['correo']}")
print(f"Teléfono: {contacto['telefono']}")

