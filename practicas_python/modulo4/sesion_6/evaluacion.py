usuarios = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
id_usuario = '004'

try:
    print(usuarios['004'])

except KeyError:
    print('La clave 004 no esta en el diccionario. Añadiendo clave...')
    usuarios[id_usuario] = 'Ninguno'
print(usuarios)    
