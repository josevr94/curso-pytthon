import json

with open('practicas_python/file/json/employees.json', 'r') as file:
    data = json.load(file)
    
#operaciones Basica 

#Mostrar la informacion del arcivo json
print('---------Lista de Empleados------------------')
for employee in data['employees']:
    print(f'Nombre: {employee['name']}, Edad: {employee['age']}, Ciudad: {employee['city']}')    

# obtener la edad promedio de los empleados
total_age = sum(employee['age'] for employee in data['employees'])   
promedio_edad = total_age / len(data['employees']) 
print(f'El promedio de la edad de los empleados es: {promedio_edad}')

#Econtrar empleado de una ciudad en especifica
city = 'London'
employees_in_city = [emp['name'] for emp in data['employees'] if emp['city']== city]
print(f'El empleado de la ciudad {city}: es {','.join(employees_in_city)}')

#agregar un nuevo empleado
nuevo_empleado = {'name':'jose', 'age':29, 'city': 'Paine'}
data['employees'].append(nuevo_empleado)

# aguardar los cambios
with open('practicas_python/file/json/employees.json', 'w') as file:
    json.dump(data, file, indent=4)
print('---------Cambios Guardados------------------')


