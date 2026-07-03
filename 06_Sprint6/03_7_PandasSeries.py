import pandas as pd

df = pd.read_csv('06_Sprint6/datasets/music_log_chpt_11.csv')
# Parte de la tabla, es un DataFrame
part_df = df[['genre', 'Artist']]
print(type(part_df))
# Tabla completa, es un DataFrame
print(type(df))
# Sólo una columna, es una Serie
part_df = df['Artist']
print(type(part_df))
# Nombre de la Serie
print(part_df.name)
# Longitud de la Serie
print(part_df.size)
# Indexación de la Serie
artist = df['Artist']
print(artist[0])
# Usando el atributo loc
print(artist.loc[0])
# Miltiples elementos
print(artist.loc[[5, 7, 10]])
# Elementos consecutivos, slice
print(artist.loc[5:10])
# No incluye el último elemento
print(artist[5:10])
# Todos los elementos a partir de un índice
print(artist.loc[5:])
# Todos los elementos hasta un índice
print(artist.loc[:3])

# Ejercicio: Extraer la columna 'track'
tracks = df['track']
top20 = tracks.loc[:19]

print(top20)

