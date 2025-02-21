# Tipos de datos
import pandas as pd

df = pd.read_csv('04_Sprint4/datasets/OnlineRetail.csv')
print(df.head())

print(f'Min: {df['StockCode'].min()}, Max: {df['StockCode'].max()}')
print('\n Info')
df.info()

print('\nWorking with Numeric and string data types\n')

d = {'col1': [1.0, 2.0], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)
print()
print('Output of df.info():')
df.info()
print()
df_str_dtype = df.astype('str')
print(df_str_dtype)
print()
df_str_dtype.info()

df['col1'] = df['col1'].astype('int')
print(df)
print()
print(df.dtypes)