def hacer_grandioso(magos):
    return ["El gran " + mago for mago in magos]

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

print("Nombres antes de ser modificados:")
imprimir_nombres(nombres)


magos_grandiosos = hacer_grandioso(magos)

print("\nMagos grandiosos:")
imprimir_nombres(magos_grandiosos)

print("\nCientíficos:")
imprimir_nombres(cientificos)

print("\nLos Restantes:")
for nombre in nombres:
    if nombre not in magos and nombre not in cientificos:
        print(nombre)