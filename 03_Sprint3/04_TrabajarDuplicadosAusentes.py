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