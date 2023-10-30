import pandas as pd

# Datos ficticios de propiedades en Lisboa
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nombre': ['Propiedad 1', 'Propiedad 2', 'Propiedad 3', 'Propiedad 4', 'Propiedad 5',
               'Propiedad 6', 'Propiedad 7', 'Propiedad 8', 'Propiedad 9', 'Propiedad 10'],
    'Precio': [30, 35, 25, 40, 20, 50, 45, 30, 40, 35],
    'Puntuacion': [4.8, 4.5, 4.9, 4.2, 4.7, 4.5, 4.6, 4.8, 4.3, 4.9],
    'TipoHabitacion': ['Shared room', 'Private room', 'Entire home/apt', 'Shared room', 'Entire home/apt',
                       'Shared room', 'Private room', 'Shared room', 'Entire home/apt', 'Private room']
}

# Crear DataFrame con información de propiedades
df = pd.DataFrame(data)

# Filtrar propiedades que cumplen con el presupuesto de Diana
df = df[df['Precio'] <= 50]

# Filtrar habitaciones compartidas y ordenar por precio y puntuación
df_shared_rooms = df[df['TipoHabitacion'] == 'Shared room']
df_shared_rooms = df_shared_rooms.sort_values(by=['Precio', 'Puntuacion'], ascending=[True, False])

# Tomar las 10 propiedades más baratas (compartidas o no)
top_10_properties = pd.concat([df_shared_rooms.head(10), df[df['TipoHabitacion'] != 'Shared room'].head(10)])

# Mostrar las 10 propiedades más baratas
print(top_10_properties[['Nombre', 'Precio', 'Puntuacion', 'TipoHabitacion']])
