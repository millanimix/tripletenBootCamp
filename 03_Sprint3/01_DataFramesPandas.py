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

