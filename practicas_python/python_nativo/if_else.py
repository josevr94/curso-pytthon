#ejemplo if else
x=int(input("ingresa un numero X:"))
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5") 

#ejemplo elif
y= int(input("ingresa otro numero Y:"))  
if y <10:
    print("Y es menor que 10")
elif y == 10:
    print("y es igual a 10")  
elif y < 20:   
    print("y es mayor que 10, pero menor 20 ")   
else:
    print("y 20 o mayor")   
  
 #ejemplo con edad   
edad= int(input("ingresa su edad"))  
if edad <18:
    print("Debe tener al menos 18  para registrarse")
elif 18 <= edad <= 120:
    print("Registro Existoso. Bienvenido")
else:
  print("Edad no valida. Por favor ingresa una edad correcta")   
  
     