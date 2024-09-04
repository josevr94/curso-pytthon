#Metodo
def sin_retorno():
    print("Esta funcion no tiene retorno")#metodo sin retorno
def retorno_unico(a,b):
    return a + b #retorno unico
def retorno_multiple(a,b,c):
    return a,b,c

#Main
sin_retorno()

#invocar retorno unico
x=5
y=20
retorno2=retorno_unico(x,y)
print(f"el retono unico: {retorno2}")
retorno3=retorno_unico(90,100)
print(f"el retono unico: {retorno3}")

#invocar retorno multiple
x,y,z = retorno_multiple(90,821,921)
print(f"el retono multiple es: {x},{y},{z}")