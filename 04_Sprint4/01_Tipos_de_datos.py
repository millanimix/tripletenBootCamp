# Tipos de datos
import pandas as pd
import numpy as np

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

print('\nProblemas inesperados\n')

d = d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)
print(df)
# Comprobar si es seguro convertir 'col1'
print('\n¿es suguro convertir col1?')
print(np.array_equal(df['col1'], df['col1'].astype('int')))
#True, Es seguro convertir col1, no se pierden datos
print('\n¿es suguro convertir col2?')
print(np.array_equal(df['col2'], df['col2'].astype('int')))
#False, No es seguro convertir, se perderían datos

print('\nStrings a valores numéricos\n')
d = {'col1': ['1.0', '2.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)
# convertir col2 a int
df['col2'] = df['col2'].astype('int')
print(df.dtypes)
# No se puede convertir a entero
# df['col1'] = df['col1'].astype('int')
df['col1'] = pd.to_numeric(df['col1'])
print(df.dtypes)

print('\n Parametro errors= en to_numeric')
d = {'col1': ['1.0', 'B.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

df['col2'] = df['col2'].astype('int')
df['col1'] = pd.to_numeric(df['col1'], errors='coerce')

print(df.dtypes)
print(df)

print('Ejercicios')
print('1/3')
df = pd.read_csv('04_Sprint4/datasets/OnlineRetail.csv')
print(df.dtypes)
can_convert = np.array_equal(df['Quantity'], df['Quantity'].astype('int'))
print(can_convert)
# Es seguro cambiar de float64 to int
print('2/3')
df['Quantity'] = df['Quantity'].astype('int')
df.info()

print('3/3')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df.info()

print('\nTrabajar con fechas y horas\n')
df = pd.read_csv('04_Sprint4/datasets/OnlineRetail.csv')
print(df.head())
print(df['InvoiceDate'].dtype)

string_date = '2010-12-17T12:38:00Z'
datetime_date = pd.to_datetime(string_date, format='%Y-%m-%dT%H:%M:%SZ')
print(type(string_date))
print(type(datetime_date))
print(datetime_date)

print('\nEjercicios')
print('E01\n')
position = pd.read_csv('04_Sprint4/datasets/position.csv')
print(position.head(15))
print('E02\n')
position.info()
print('E03\n')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
print(position.head())