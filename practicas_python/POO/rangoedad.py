class EdadFueradeRangoError(Exception):
    def __init__(self,edad, mensaje = "La edad no se encuentra en el rango de 18 a 65"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(f"{mensaje} Edad recibida: {edad}")
        
def verificar_edad(edad):
    if edad < 18 or edad > 65:
        raise EdadFueradeRangoError(edad)
    else:
        print(f"Edad Valida: {edad}")        

#main
try:
    edad = 70
    verificar_edad(edad)
    
except EdadFueradeRangoError as e:   
    print(e)        