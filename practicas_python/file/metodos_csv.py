import csv
#leer un archivo csv, esta en el modo 'r' q es solo de lectura
with open("file/csv/people.csv", mode="r", newline="") as f:
    lector_csv = csv.reader(f)
    for fila in lector_csv:
        print(fila)
#escribe sobre un archivo csv que ya existe , si el archivo csv no existe se crea uno nuevo, esta en el modo 'w'que es para que escriba        
with open("file/csv/people2.csv", mode="w", newline= "") as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerow(["ID", "Nombre", "Edad"]) #la funcion writerow es para que los elementos se escribasn con un estilo ecxel
    escritor_csv.writerow(["1", "Juan", "25"])
    escritor_csv.writerow(["2", "Maria", "30"])

#Agregar un registro  a un archivo csv   
with open("files/csv/people2.csv", mode="a", newline="") as f:
    escritor_csv=csv.writer(f)
    escritor_csv.writerow(["Cristian","Castillo","Concepcion"])           