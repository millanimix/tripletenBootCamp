# Procesamiento de datos y análisis inicial
import pandas as pd


print()
print('Problemas con los datos: Entra basura, sale basura')


df = pd.read_csv('03_Sprint3/datasets/music_log_raw.csv')
print(df.head(10))

# Error por espacios
# print(df[' user_id'])

print()
print('Renombrar columnas')

measurements = [['Sun', 146, 152],
                ['Moon', 0.36, 0.41], 
                ['Mercury', 82, 217], 
                ['Venus', 38, 261],
                ['Mars', 56, 401],
                ['Jupiter', 588, 968],
                ['Saturn', 1195, 1660],
                ['Uranus', 2750, 3150],
                ['Neptune', 4300, 4700],
                ['Halley\'s comet', 6, 5400]]

header = ['Celestial bodies ', 'MIN', 'MAX']
celestial = pd.DataFrame(data=measurements, columns=header)
print(celestial.info())
print(celestial.columns)

columns_new = {
    'Celestial bodies ': 'celestial_bodies',
    'MIN': 'min_distance',
    'MAX': 'max_distance'
}

# celestial = celestial.rename(columns=columns_new)
# print(celestial.columns)

# celestial.rename(columns=columns_new, inplace=True)
# print(celestial.columns)

new_col_names = []
for old_name in celestial.columns:
    name_stripped = old_name.strip()
    name_lowered = name_stripped.lower()
    name_no_spaces = name_lowered.replace(' ', '_')
    new_col_names.append(name_no_spaces)

celestial.columns = new_col_names
print(celestial.columns)

print()
print('Ejercicios')

df = pd.read_csv('03_Sprint3/datasets/music_log_raw.csv')
print(df.columns)

df_new_cols = df.rename(columns={
    '  user_id': 'user_id', 
    'total play': 'total_play',
    'Artist': 'artist'
})

print(df_new_cols.columns)

print()
print('Procesar valores ausentes')

cholera = pd.read_csv('03_Sprint3/datasets/cholera_short.csv')
print(cholera)
print('info')
print(cholera.info())
print('Suma de nulos')
print(cholera.isna().sum())
print('Sustituir valores')
cholera['imported_cases'] = cholera['imported_cases'].fillna(0)
# cholera['imported_cases'].fillna(0, inplace=True)
# Para varias columnas
# columns_to_replace = ['imported_cases']
# for col in columns_to_replace:
#     cholera[col].fillna(0, inplace=True)
print(cholera)

print('Eliminar filas sin datos en columnas definidas en subset')
cholera = cholera.dropna(subset=['total_cases', 'deaths', 'fatality_rate'])
print(cholera)

print('Eliminar columnas')
# Eliminación de columnas con muchos nulos
# cholera = cholera.dropna(axis='columns')
# Eliminación de una columna en especifico 
# cholera = cholera.drop(labels=['notes'], axis='columns')
cholera.drop(labels=['notes'], axis='columns', inplace=True)
print(cholera)



print()
print('Ejercicio 1')
print()

# DataFrame de la producción de petróleo
data = {
    'well_id': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6'],
    'production_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02'],
    'oil_volume': [100, None, 200, 300, None, None],
    'gas_volume': [1000, 800, 950, 1100, 850, 900],
    'region': ['North', 'North', 'South', 'South', 'West', 'West'],
    'status': ['active', None, 'active', 'inactive', None, 'active']
}

df = pd.DataFrame(data)

# df['oil_volume'].fillna(0, inplace=True)
# Pandas 3.0
df.fillna({'oil_volume': 0}, inplace=True)
# Pandas 3.0
df.fillna({'status': 'unknown'}, inplace=True)

print(df.isna().sum())


print('Ejercicio 2')
print()
print()

# DataFrame de la producción de petróleo
data = {
    'well_id': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6'],
    'production_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02'],
    'oil_volume': [100, None, 200, 300, None, None],
    'gas_volume': [1000, 800, 950, 1100, 850, 900],
    'region': ['North', 'North', 'South', 'South', 'West', 'West'],
    'status': ['active', None, 'active', 'inactive', None, 'active']
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Eliminar filas con valores ausentes en la columna 'oil_volume'
df.dropna(subset=['oil_volume'], inplace=True)

# Eliminar la columna 'status' del DataFrame
# df.drop(labels=['status'], axis='columns', inplace=True)
df.drop(columns='status', inplace=True)

# Mostrar la cantidad de valores ausentes en cada columna después de la eliminación
print("Valores ausentes después de la eliminación:")
print(df.isna().sum())

# Mostrar las columnas restantes del DataFrame
print("Columnas restantes:")
print(df.columns)

print()
print('Valores duplicados')
print()

df = pd.read_csv('03_Sprint3/datasets/music_log_raw.csv')

print(df.duplicated())
print(df.duplicated().sum())

# Para eliminar duplicados
# df = df.drop_duplicates()
# df.drop_duplicates(inplace=True)
# print(df.duplicated().sum())

# Analizar indices
# print(df.head(10))
# print(df.duplicated().sum())

# df = df.drop_duplicates().reset_index()
# Eliminar duplicados y reindexar sin conservar la columna original de indices
df = df.drop_duplicates().reset_index(drop=True)
print(df.duplicated().sum())
print(df.head(10))

print()
print('Detectar duplicados implicitos')
print()

rating = ['date', 'name', 'points']
players = [
        ['2018.01.01',  'Rafael Nadal', 10645],
                ['2018.01.08',  'Rafael Nadal', 10600],
                ['2018.01.29',  'Rafael Nadal', 9760],
                ['2018.02.19',  'Roger Federer', 10105], 
                ['2018.03.05',  'Roger Federer', 10060],
                ['2018.03.19',  'Roger Federerr', 9660],
                ['2018.04.02',  'Rafael Nadal Parera', 8770],
                ['2018.06.18',  'Roger Fedrer', 8920],
                ['2018.06.25',  'Rafael Nadal Parera', 8770],
                ['2018.07.16',  'Rafael Nadal Parera', 9310],
                ['2018.08.13',  'Rafael Nadal Parera', 10220],
                ['2018.08.20',  'Rafael Nadal Parera', 10040],
                ['2018.09.10',  'Rafael Nadal Parera', 8760],
                ['2018.10.08',  'Rafael Nadal Parera', 8260],
                ['2018.10.15',  'Rafael Nadal Parera', 7660],
                ['2018.11.05',  'Novak Djokovic', 8045],
                ['2018.11.19',  'Novak Djokovic', 9045]
]
tennis = pd.DataFrame(data=players, columns=rating)
print(tennis)
print(tennis['name'].unique())
print(tennis['name'].nunique())

# tennis['name'] = tennis['name'].replace('Roger Federerr', 'Roger Federer')
# # Using inplace parameter older version
# # tennis['name'].replace('Roger Fedrer', 'Roger Federer', inplace=True)
# tennis.replace({'name': 'Roger Fedrer'}, 'Roger Federer', inplace=True)
# # tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera', inplace=True)
tennis.replace({'name': 'Rafael Nadal'}, 'Rafael Nadal Parera', inplace=True)
# print(tennis['name'].unique())
# print(tennis['name'].nunique())
# print(tennis)

# Using a function
def replace_wrong_values(df, column, wrong_values, correct_value):
    for wrong_value in wrong_values:
        df[column] = df[column].replace(wrong_value, correct_value)
    return df

duplicates = ['Roger Federerr', 'Roger Fedrer']
name = 'Roger Federer'
tennis = replace_wrong_values(tennis, 'name', duplicates, name)
print(tennis)
print(tennis['name'].unique())
print(tennis['name'].nunique())

print()
print('Exercise 2')

df = pd.read_csv('03_Sprint3/datasets/music_log_raw.csv')

print(df.columns)
print(df.info())
print(df.isna().sum())
unique_genres = df['genre'].unique()
print(unique_genres)
ammount_genres = df['genre'].nunique()
print(ammount_genres)

# Estandarización de categorías
# Tu código va aquí (ejecuta el código para visualizar el problema)
df.replace({'genre': 'hard-n-heavy'}, 'hard\'n\'heavy', inplace=True)
df.replace({'genre': 'ranchera'}, 'rancheras', inplace=True)

# Validación
# Elimina vacios dropna y obtiene unicos unique
generos_unicos = df['genre'].dropna().unique()
print(generos_unicos)
filtros = [g for g in generos_unicos if g.startswith('har') or g.startswith('ran')]

# Imprimir el resultado
print(filtros)

print()
print('Ejercicio 3')

df = pd.read_csv('03_Sprint3/datasets/music_log_raw.csv')

# Definir una función para corregir duplicados implícitos
# def corregir_duplicados_implícitos(df, columna, correcciones):
#     wrong_values = correcciones.keys()
#     for wrong_value in wrong_values:
#         print(correcciones.get(wrong_value))
#         df[columna].replace(wrong_value, correcciones.get('wrong_value'), inplace=True)
#     return df

def corregir_duplicados_implícitos(df, columna, correcciones):
    df[columna] = df[columna].replace(correcciones)
    return df

# Diccionario con correcciones para la columna 'genre'
correcciones_artistas = {
    "hard-n-heavy": "hard'n'heavy",
    "ranchera": "rancheras"
}

# Aplicar la función para corregir los duplicados en la columna 'Artist'
df_corregido = corregir_duplicados_implícitos(df, 'genre', correcciones_artistas)

# Validación
géneros_únicos = df['genre'].dropna().unique()
filtros = [g for g in géneros_únicos if g.startswith('har') or g.startswith('ran')]

# Imprimir el resultado
print(filtros)

print()
print('Ejercicio 1')

# Cargar los datos 
df = pd.read_csv('03_Sprint3/datasets/steam-200k.csv')
df.columns = ['user_id', 'game_title', 'behavior_name', 'value']

print('Número de filas duplicadas (Inicial): ', str(df.duplicated().sum()))
# 1. Eliminar filas duplicadas
# Reiniciar los índices
df = df.drop_duplicates().reset_index(drop=True)
# 2. Mostrar el DataFrame sin duplicados
print('Número de filas duplicadas (Final): ', str(df.duplicated().sum()))
# 3. Mostrar valores únicos en la columna 'game-title'
print('Valores únicos: ', df['game_title'].unique())
print('Cantidad de valores únicos: ', df['game_title'].nunique())
# 4. Función para manejar duplicados implícitos
def corregir_duplicados(df):
    # Hacer una copia del DataFrame
    df = df.copy()
    # Mapeo de números romanos a números arábigos
    conversion_roman_to_arabic = {'II': '2',
                                  'III': '3',
                                  'IV': '4',
                                  'V': '5'}#tu diccionario
   
    for romano, arabico in conversion_roman_to_arabic.items():
        #itera sobre cada elemento del diccionario y reemplaza dicho elemento	
        df['game_title'] = df['game_title'].str.replace(romano, arabico)
        df['game_title'] = df['game_title'].str.lower()
    # Convertir títulos de juegos a minúsculas
    return df
	
# Validación resultados
print()
df_corregido = corregir_duplicados(df)
print(df_corregido.head(10))

print()
print('Agrupación de datos')

exoplanet = pd.read_csv('03_Sprint3/datasets/exoplanet.csv')
print(exoplanet.head(10))
print(exoplanet.groupby(by='\tdiscovered'))
# Without by= argument
# print(exoplanet.groupby('\tdiscovered'))
print()
print(exoplanet.groupby('\tdiscovered').count())
# Indicando la columna en cuestion
exo_number = exoplanet.groupby('\tdiscovered')['\tradius'].count()
print(exo_number)
# Calculando la suma de los radios
exo_radius_sum = exoplanet.groupby('\tdiscovered')['\tradius'].sum()
print(exo_radius_sum)
# Calculando el promedio con las consultas anteriores
exo_radius_mean = exo_radius_sum / exo_number
print(exo_radius_mean)

print()
print('Practica guiada')

df = pd.read_csv('03_Sprint3/datasets/music_log_processed.csv')
print(df.head())
genre_groups = df.groupby('genre')['genre'].count()
print(genre_groups)

genre_groups = df.groupby('genre')['total_play'].sum()
print(genre_groups)

print()
print('Actividad práctica')

digimon_data = pd.read_csv('03_Sprint3/datasets/DigiDB_digimonlist.csv')
print(digimon_data.head(10))

grouped_stage_count = digimon_data.groupby('Stage')['Stage'].count()
print('Distribución total de los Digimons', '\n', grouped_stage_count)
grouped_stage_sum = digimon_data.groupby('Stage')['Lv 50 HP'].sum()
print('Total de salud', '\n',grouped_stage_sum)
grouped_stage_mean = digimon_data.groupby('Stage')['Lv50 Spd'].mean()
print('Promedio Nivel de Ataque', '\n',grouped_stage_mean)

# Odenar datos

print()
print('Ordenar Datos')

exoplanet = pd.read_csv('03_Sprint3/datasets/exoplanet.csv')
# Order the whole dataset
print(exoplanet.sort_values(by='\tradius').head(10))
# Order only a column
print(exoplanet['\tradius'].sort_values().head(10))
# Only smaller than earth
print(exoplanet[exoplanet['\tradius'] < 9])
# Only 2014 year
print(exoplanet[exoplanet['\tdiscovered'] == 2010])

exo_small_14 = exoplanet[exoplanet['\tradius'] < 12]
exo_small_14 = exo_small_14[exo_small_14['\tdiscovered'] == 2010]
print(exo_small_14)

print(exo_small_14.sort_values(by='\tradius', ascending=False))

exo_small_14 = exo_small_14.sort_values(by='\tradius', ascending=False)

df = pd.DataFrame(['b', 'c', 'a'], columns=['alphabet'])
print(df)
df = df.sort_values(by='alphabet')
print(df)

print()
print('Ejercicios')
df = pd.read_csv('03_Sprint3/datasets/music_log_processed.csv')
print(df.head(10))
metal_ordenado = df[df['genre'] == 'metal'].sort_values(by='total_play', ascending=False)
print(metal_ordenado.head(10))

ordenado = df.sort_values(by='total_play', ascending=False)
print('Por generos')
print(ordenado['genre'].head(10))

print('Actividad práctica')
time_by_genre = df.groupby('genre')['total_play'].sum()
# Aquí no lleva nombre de columna
time_by_genre_sort = time_by_genre.sort_values(ascending=False)
print(time_by_genre_sort)

