# 01_DataFramesPandas
import pandas as pd

# df = pd.read_csv("datasets/music.csv")
# df = pd.read_excel('datasets/music.xlsx')

# data_types = df.dtypes
# print(data_types)

# column_names = df.columns
# print(column_names)

# data_shape = df.shape
# print(data_shape)

# df.info()

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
