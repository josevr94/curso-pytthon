class EdadinvalidadError(Exception): # para personalisar un error hay que primero crear esta clase exception, la cual permite usar el raise posteriormente
    pass
def verificarEdad(edad):
    if edad < 18:
        raise ValueError("Debe ser mayor de 18 años para registrarse") # el raise es para generar un mensaje personalisado de error 
    return "Registro Completo"    
try:
    mensaje = verificarEdad(15)
    print(mensaje)
except ValueError as e:   
    print(f"Error: {e}")