import pandas as pd

# Datos ficticios de las propiedades de Roberto y Clara
data_roberto = {
    'ID': [97503, 12345, 67890],
    'Nombre': ['Casa Roberto', 'Otra Casa', 'Otra Casa 2'],
    'Criticas': [15, 8, 12]
}

data_clara = {
    'ID': [90387, 11111, 22222],
    'Nombre': ['Casa Clara', 'Casa Clara Vecina', 'Casa Clara de Verano'],
    'Criticas': [10, 5, 20]
}

# Crear DataFrames para las propiedades de Roberto y Clara
df_roberto = pd.DataFrame(data_roberto)
df_clara = pd.DataFrame(data_clara)

# Filtrar las críticas de la casa de Roberto y Clara
roberto_criticas = df_roberto[df_roberto['ID'] == 97503]['Criticas'].values[0]
clara_criticas = df_clara[df_clara['ID'] == 90387]['Criticas'].values[0]

# Verificar si la casa de Roberto tiene más críticas que la de Clara
roberto_tiene_mas_criticas = roberto_criticas > clara_criticas

# Imprimir el resultado
if roberto_tiene_mas_criticas:
    print("¡La casa de Roberto tiene más críticas que la de Clara!")
else:
    print("La casa de Clara tiene igual o más críticas que la de Roberto.")

df_combined = pd.concat([df_roberto, df_clara], ignore_index=True)

# Guardar el DataFrame combinado como un archivo Excel
df_combined.to_excel("roberto.xls", index=False)
