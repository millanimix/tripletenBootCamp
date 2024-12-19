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

# df = pd.read_excel('03_Sprint3/datasets/music.xlsx')

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

