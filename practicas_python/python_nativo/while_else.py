# passwords = ["abc12345","paswordSegur1","12332342324","hola3223432","holamundo"]
passwords = {"roberto":"abc32232","cristian":"abc12345","jose":"abc5"}
for nombre,password in passwords.items():
    if len(password) < 8:
        print(f"el password: {nombre} es demasiado corto")
        break
    
else:
    print("Todas los password tiene la longitud requerida")
   

# contador = 0
# elements = len(passwords)
# while contador < elements:
#     if len(passwords[contador]) < 8:
#         print(f"El password: {passwords[contador]} es demasiado corto")
#         break
#     contador += 1
# else:
#     print("Todos los passwords tienen la longitud requerida")