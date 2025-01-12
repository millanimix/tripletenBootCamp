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