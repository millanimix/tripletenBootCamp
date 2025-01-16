# Trabajar con valores duplicados y ausentes

import pandas as pd

df_logs = pd.read_csv('03_Sprint3/datasets/visit_log.csv')
print(df_logs.head())

print()
print('Info')
df_logs.info()

print()
print('Isna')
print(df_logs.isna().sum())

print()
print('value counts')
print(df_logs['source'].value_counts(dropna=False))

print()
print('value counts')
print(df_logs['email'].value_counts())
email_values = df_logs['email'].value_counts()
email_values = email_values.sort_index()
print(email_values)

# Filtering DataFrames with NaNs
print()
print('Printing only NaN rows')
print(df_logs[df_logs['source'].isna()])
print('Printing oposite NaN rows')
print(df_logs[~df_logs['source'].isna()])

print('Filtering a DataFrame')
email_values = df_logs[~df_logs['email'].isna()]
only_emails = email_values[email_values['source'] == 'email']
print(only_emails)

print('Comprobando columnas email y source')
df_emails = df_logs[df_logs['email'].isna()]
df_emails = df_emails[df_emails['source'].isna()]
print(df_emails)

# Fill the missing categorical values
print('Fill the miising categorical values')
print()
# Para leer los valores NaN como cadenas vacias
df_logs = pd.read_csv('03_Sprint3/datasets/visit_log.csv', keep_default_na = False)

print(df_logs.head())
print()
df_logs.info()

print()
print()
df_logs = pd.read_csv('03_Sprint3/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
purchases = df_logs.groupby('source')['purchase'].sum()
# Tasa de conversión, proporción de visitis en las que se realizó una compra
print(purchases / visits)

# Fill the missing cuantitative values

print()
print('Fill the missing cuantitative values')
print()

analytics_data = pd.read_csv('03_Sprint3/datasets/web_analytics_data.csv')
print(analytics_data.head(10))
print(analytics_data.isna().sum())

age_avg = analytics_data['age'].mean()
print('Mean age:', age_avg)

analytics_data['age'] = analytics_data['age'].fillna(age_avg)
print(analytics_data.head(10))
print(analytics_data.isna().sum())

print()
print('Device type anilisis')
desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
print(desktop_data.head())
desktop_data.info()

mobile_data = analytics_data[analytics_data['device_type'] == 'mobile']
print(mobile_data.head())
mobile_data.info()

desktop_avg = desktop_data['time'].mean()
mobile_avg = mobile_data['time'].mean()

print(f'Timepo de escritorio promedio: {desktop_avg:.2f} segundos')
print(f'Tiempo móvil primedio: {mobile_avg:.2f} segundos')

# desktop_data['time'] = desktop_data['time'].fillna(desktop_avg)
desktop_data.loc[:, 'time'] = desktop_data['time'].fillna(desktop_avg)
# mobile_data['time'] = mobile_data['time'].fillna(mobile_avg)
mobile_data.loc[:, 'time'] = mobile_data['time'].fillna(mobile_avg)

desktop_data.info()
print()
mobile_data.info()

analytics_data.info()

print()
print('Actividad practica')
print()

data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South', 'North', 'South'],
    'age': [25, 34, 45, None, 38, 50, None, 28, 42, 35],
    'revenue': [120, 80, 130, 95, None, None, 125, 90, None, 110]
}
# Convertir a DataFrame
sales_data = pd.DataFrame(data)

sales_data.info()

north_data = sales_data[sales_data['region'] == 'North']
print(north_data)
north_avg = north_data['revenue'].mean()
print(f'Promedio de ingresos en \'North\': {north_avg}')
north_data.loc[:,'revenue'] = north_data['revenue'].fillna(north_avg)
print(north_data)

south_data = sales_data[sales_data['region'] == 'South']
print(south_data)
south_avg = south_data['revenue'].mean()
print(f'Promedio de ingresos en \'South\': {south_avg}')
south_data.loc[:,'revenue'] = south_data['revenue'].fillna(south_avg)
print(south_data)

# Duplicate values management

print()
print('Duplicate values mangement')
print()

df_stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
print(df_stock.head(10))
df_stock.info()

# Revisión: Encontrar duplicados

# Técnica 1: Método dupicate()
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Así es como se ve el dataset:')
print(df)
print('Así es como se ve una serie booleana devuelta:')
print(df.duplicated())
print('Así se ve el resultado de duplicated() con sum():')
print(df.duplicated().sum())
print('Mostrar duplicados con un filtro')
print(df[df.duplicated()])

# Técnica 2: Método value_counts()

df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Así es como se ve el dataset:')
print(df)
print()
print('Este es el resultado de la llamada al método value_counts() para col_1:')
print(df['col_1'].value_counts())

# Gestión de duplicados

df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})
print('Dataset original:')
print(df)
print()
print('Dataset con duplicados eliminados:')
print(df.drop_duplicates())

df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print(df)
print()
print(df.drop_duplicates(subset='col_1'))


stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
print(stock['item'].value_counts())

df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Col_1 original en el dataset:')
print(df['col_1'])
print()
print('Dataset con valores reducidos en col_1')
print(df['col_1'].str.lower())

# Para reemplazar la columna

df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})
df['col_1'] = df['col_1'].str.lower()
print(df)

# Comprobar total de duplicados
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})
df['col_1'] = df['col_1'].str.lower()
print('Total de duplicados')
print(df['col_1'].duplicated().sum())

# Reemplazar sólo partes de un string
# Usar replace()

stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
print(stock.head())
stock['item'] = stock['item'].str.replace('GB', 'gb')
print(stock.head())

# Conservar la columna original

stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
stock['item_modified'] = stock['item'].str.replace('GB', 'gb')
print(stock.head())

# Ejercicio 2
print('Ejecicio 2')
df_stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()
print(df_stock.head())

apple = df_stock[df_stock['item_lowercase'].str.contains('apple')].sum()['count']
samsung = df_stock[df_stock['item_lowercase'].str.contains('samsung')].sum()['count']

print('Número total de teléfonos Apple:', apple)
print('Número total de teléfonos Samsung:', samsung)

# Ejercicio 3
print('Ejecicio 3')
df_stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()
print(df_stock.head())

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True)
print(df_stock)


# Ejercicio 4
print('Ejecicio 4')
df_stock = pd.read_csv('03_Sprint3/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum()
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True)

df_stock.loc[0, 'count'] = apple
df_stock.loc[3, 'count'] = samsung

print(df_stock)

# Actividad practica 1
print()
print('Practica 1')
print()
df = pd.read_csv('03_Sprint3/datasets/steam-200k.csv')
df.columns = ['user_id', 'game_title', 'behavior_name', 'value']
print(df.head(10))
df.info()

print(f'Número de filas duplicadas (Inicial): {df.duplicated().sum()}')
df_sin_duplicados = df.drop_duplicates().reset_index(drop=True)
print(f'Número de filas duplicadas (Final): {df_sin_duplicados.duplicated().sum()}')
print()
print(df_sin_duplicados['game_title'].value_counts())

df_sin_duplicados.loc[:,'game_title'] = df_sin_duplicados['game_title'].str.lower()
print()
print(df_sin_duplicados)