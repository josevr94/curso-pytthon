# Cargar el archivo Excel
excel_file = 'inventario.xlsx'
excel_sheets = pd.read_excel(excel_file, sheet_name=None)
 
# Crear un nuevo archivo Excel consolidado
with pd.ExcelWriter('consolidado.xlsx') as writer:
    for sheet_name, df in excel_sheets.items():
        # Escribe cada hoja en el nuevo archivo
        df.to_excel(writer, sheet_name=sheet_name)
 
print("Consolidación completada.")
 
 
# """ import pandas as pd
 
# # Cargar el archivo Excel
# file_path = 'inventario.xlsx'  # Reemplaza con la ruta a tu archivo
# excel_file = pd.ExcelFile(file_path)
 
# # Crear una lista para almacenar los DataFrames de cada hoja
# all_sheets = []
 
# # Recorrer todas las hojas del archivo
# for sheet_name in excel_file.sheet_names:
#     df = pd.read_excel(excel_file, sheet_name=sheet_name)
#     df['Sheet Name'] = sheet_name  # Añadir una columna para identificar de qué hoja provienen los datos
#     all_sheets.append(df)
 
# # Concatenar todos los DataFrames en uno solo
# consolidated_df = pd.concat(all_sheets, ignore_index=True)
 
# # Guardar el DataFrame consolidado en una nueva hoja de un archivo Excel
# consolidated_df.to_excel('consolidado.xlsx', index=False) """