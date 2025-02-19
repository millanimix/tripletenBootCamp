# Tipos de datos
import pandas as pd

df = pd.read_csv('04_Sprint4/datasets/OnlineRetail.csv')
print(df.head())

print(f'Min: {df['StockCode'].min()}, Max: {df['StockCode'].max()}')
print('\n Info')
df.info()