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