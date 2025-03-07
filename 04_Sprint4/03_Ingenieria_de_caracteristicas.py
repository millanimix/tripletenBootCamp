# Ingenieria_de_caracteristicas

import pandas as pd

df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
print(df.head())

# Crear una nueva columna que sea la suma de todas las ventas
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
print(df['total_sales'].head())

# Crear la columna eu_sales_share y rellenarla
df['eu_sales_share'] = df['eu_sales'] / df['total_sales']
print(df['eu_sales_share'].head())

print('Generar columnas booleanas')
# Crear una columna que comprueba si la empresa distribuidaora es Nintendo
df['is_nintendo'] = df['publisher'] == 'Nintendo'
print(df['is_nintendo'].head())

print(df['platform'].str.lower().isin(['gb', 'wii']).head())

print('Columnas categoricas')
# Mirar los valores únicos de la columna platform
print(df['platform'].unique())
# Convertir la columna platform a tipo category
print()
df['platform'] = df['platform'].astype('category')
print(df['platform'].head())

print('Ejercicio')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
# Comprobar cuál es el juego más vendido (en promedio) en todos los mercados
# df['average_sales'] = df[['na_sales', 'eu_sales', 'jp_sales']].mean(axis=1)
df['average_sales'] = (df['na_sales'] + df['eu_sales'] + df['jp_sales']) / 3
df = df.sort_values(by='average_sales', ascending=False)
print(df.head())
