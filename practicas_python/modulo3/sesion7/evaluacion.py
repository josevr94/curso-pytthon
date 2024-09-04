
estudiantes = [
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 != 0:
        return True
    else:
        return False     
  


# Calcular el promedio de las calificaciones de cada estudiante
for estudiante in estudiantes:
    suma = sum(estudiante['calificaciones'])
    promedio = suma / len(estudiante['calificaciones'])
    estudiante['promedio'] = promedio
    
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and estudiante['promedio'] > 85:
        print(f"El estudiante de nombre {estudiante['nombre']} tiene {estudiante['edad']} años y un promedio de {estudiante['promedio']}")
# calculando los promedios de los estudiantes mayores de 18 y con edad en numeros primos

for estudiante in estudiantes:
    if estudiante['edad'] > 18 and is_prime(estudiante['edad']) and estudiante['promedio'] > 85:
        print(f"El estudiante de nombre {estudiante['nombre']} tiene {estudiante['edad']} años (número primo) y un promedio de {estudiante['promedio']}")