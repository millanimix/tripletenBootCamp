# 01_DataFramesPandas
import pandas as pd
import os

# allEntries = os.listdir('./')
# print(allEntries)

df = pd.read_csv("03_Sprint3/datasets/music.csv")
data_types = df.dtypes
print(data_types)
column_names = df.columns
print(column_names)
data_shape = df.shape
print(data_shape)
df.info()

print()
print('DataFrame with Dictionary')
print()

data = {'product_id': [101, 102, 103],
        'product_name': ['Laptop', 'Smartphone', 'Tablet'],
        'price': [1500, 800, 300],
        'category': ['Electronics', 'Electronics', 'Electronics']}

df = pd.DataFrame(data)

data_types = df.dtypes
column_names = df.columns
data_shape = df.shape

print(data_types)
print(column_names)
print(data_shape)
df.info()
print(df)

print()
print('DataFrame with array')
print()

atlas = [
    ['France', 'Paris'],
    ['Russia', 'Moscow'],
    ['China', 'Beijing'],
    ['Mexico', 'Mexico City'],
    ['Egypt', 'Cairo']
]

geography = ['country', 'capital']

world_map = pd.DataFrame(data=atlas, columns=geography)
print(world_map)

# Pandas con archivos de excel y csv

print()
print('Read CSV and Excel files')
print()

print('Opening excel file')
df_01 = pd.read_excel('03_Sprint3/datasets/product_reviews.xlsx')
df_01.describe

df_02 = pd.read_excel('03_Sprint3/datasets/product_reviews.xlsx', sheet_name=['reviews', 'reviewers'])
print(df_02['reviews'])


df = pd.read_csv('03_Sprint3/datasets/music.csv')
df.info()
print(df.head(3))
print(df.tail(3))

print()
print('Indexación de un Dataframe')
print()

# Filtrado con indexación lógica

print()
print('Filtrado con indexación lógica')
print()

print(df['genre'] == 'pop')

print(df.loc[df['genre'] == 'pop'])

df = df[df['total play'] >= 80]
df = df[df['total play'] <= 130]
df = df[df['genre'] == 'jazz']


print(df)

print()
print()

data = {
    'sucursal': ['Centro', 'Norte', 'Sur', 'Centro', 'Norte'],
    'producto': ['Camiseta roja', 'Zapatillas azules', 'Camisa blanca', 'Jeans negro', 'Camiseta roja'],
    'cliente': ['Ana Garcia', 'Luis Rodriguez', 'Pedro Hernandez', 'Maria Lopez', 'Juan Perez'],
    'cantidad': [2, 1, 3, 1, 4],
    'precio_unitario': [15.99, 49.99, 29.99, 39.99, 15.99],
    'venta_total': [31.98, 49.99, 89.97, 39.99, 63.96]
}

df = pd.DataFrame(data)
filtered_data = df.loc[((df.loc[:,'sucursal'] == 'Centro') | (df.loc[:,'sucursal'] == 'Norte')) & (df.loc[:,'precio_unitario'] > 25)]
print(filtered_data)

print()
print()

df = pd.read_csv('03_Sprint3/datasets/music.csv')
pop_df = df[df['genre'] == 'pop']
pop_duration = pop_df['total play']
print(pop_duration)

mean_duration = pop_duration.mean()
print(mean_duration)

# Ejemplo mean()
mean_duration = df[df['genre'] == 'pop']['total play'].mean()
print(mean_duration)

# Ejemplo count()
duration_thershold = 180
long_songs = df[df['total play'] > duration_thershold]['total play'].count()
print(long_songs)

# Ejemplo sum()
user_sum_dur = df[df['user_id'] == '174C0ED6']['total play'].sum()
print(user_sum_dur)
