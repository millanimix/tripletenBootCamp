# Ingenieria_de_caracteristicas

import pandas as pd
import numpy as np

df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
print(df.head())

# Crear una nueva columna que sea la suma de todas las ventas
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
print(df['total_sales'].head())

# Crear la columna eu_sales_share y rellenarla
df['eu_sales_share'] = df['eu_sales'] / df['total_sales']
print(df['eu_sales_share'].head())

print('Generar columnas booleanas')
# Crear una columna que comprueba si la empresa distribuidaora es Nintendo
df['is_nintendo'] = df['publisher'] == 'Nintendo'
print(df['is_nintendo'].head())

print(df['platform'].str.lower().isin(['gb', 'wii']).head())

print('Columnas categoricas')
# Mirar los valores únicos de la columna platform
print(df['platform'].unique())
# Convertir la columna platform a tipo category
print()
df['platform'] = df['platform'].astype('category')
print(df['platform'].head())

print('Ejercicio')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
# Comprobar cuál es el juego más vendido (en promedio) en todos los mercados
# df['average_sales'] = df[['na_sales', 'eu_sales', 'jp_sales']].mean(axis=1)
df['average_sales'] = (df['na_sales'] + df['eu_sales'] + df['jp_sales']) / 3
df = df.sort_values(by='average_sales', ascending=False)
print(df.head())

print('Create categorical columns with apply')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
print(df['year_of_release'].min(), df['year_of_release'].max())
# Games by year
df_year_of_release = df['year_of_release'].value_counts().sort_index()
print(df_year_of_release)

def era_group(year):
    """
    Returns the era of the gieven year
    -'retro' < 2000
    -'modern' >= 2000 year < 2010
    -'recent' >= 2010
    -'unknown' if year is NaN
    """

    if year < 2000:
        return 'retro'
    elif year < 2010:
        return 'modern'
    elif year >= 2010:
        return 'recent'
    else:
        return 'unknown'
    
print(era_group(1983))
print(era_group(2009))
print(era_group(2021))
print(era_group(np.nan))

print('Aply() method')
df['era_group'] = df['year_of_release'].apply(era_group)
print(df.head())

print(df['era_group'].value_counts())

print('Ejercicio')
print('1/3')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')

def score_group(score):
    """
    Returns the score group of the given score
    -'low' < 60
    -'medium' >= 60 score < 79
    -'high' >= 80
    -'no score' if score is NaN
    """
    if score < 60:
        return 'low'
    elif score < 80:
        return 'medium'
    elif score >= 80:
        return 'high'
    else:
        return 'no score'
    
print(score_group(10))
print(score_group(65))
print(score_group(99))
print(score_group(np.nan))

df['score_categorized'] = df['critic_score'].apply(score_group)
print(df.head())

df_grouped = df.groupby('score_categorized')
df_sum = df_grouped['na_sales'].sum()
print(df_sum)

print('\nCreate new categories with row functions')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)
df.info()

def era_sales_group(row):
    """
    Returns the category of the game according the year of release and total sales using the following rules:
    - 'retro' if year_of_release < 2000 and total_sales < $1 million
    - 'modern' if 2000 <= year_of_release < 2010 and total_sales < $1 milion
    - 'recent' if year_of_release >= 2010 and total_sales >= $1 million
    - 'big hit' if year_of_release >= 2010 and total_sales >= $1 million
    """
    year = row['year_of_release']
    na_sales = row['na_sales']
    eu_sales = row['eu_sales']
    jp_sales = row['jp_sales']
    
    total_sales = na_sales + eu_sales + jp_sales
    
    if year < 2000:
        if total_sales < 1:
            return 'retro'
        else:
            return 'classic'
    if year < 2010:
        if total_sales < 1:
            return 'modern'
        else:
            return 'classic'
    if year >= 2010:
        if total_sales < 1:
            return 'recent'
        else:
            return 'big hit'
        
row = df.iloc[0]
print(row)
print()
print('This game is', era_sales_group(row))

# Creating your own rows
column_names = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']
row_values = [2000, 0.1, 0.25, 0]
row = pd.Series(row_values, index=column_names)
print(row)
print()
print('This game is', era_sales_group(row))

cols = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']

row_1 = pd.Series([1989, 0, 0, 0.6], index=cols) # expect 'retro'
row_2 = pd.Series([1989, 1, 2, 0], index=cols)   # expect 'classic'
row_3 = pd.Series([2006, 0.3, 0, 0], index=cols) # expect 'modern'
row_4 = pd.Series([2020, 0, 0.4, 0], index=cols) # expect 'recent'
row_5 = pd.Series([2020, 1, 1, 1], index=cols)   # expect 'big hit'

print(row_1, row_2, row_3, row_4, row_5, sep='\n\n')
print()

rows = [row_1, row_2, row_3, row_4, row_5]

for row in rows:
    print('This game is', era_sales_group(row))

df['game_category'] = df.apply(era_sales_group, axis=1)
print(df.sample(5, random_state=321))

print(df['game_category'].value_counts())

print('Ejercicios')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row):
    critic_score = row['critic_score']
    user_score = row['user_score']
    avg_score = (critic_score + user_score * 10) / 2

    if avg_score < 60:
        return 'low'
    if avg_score < 80:
        return 'medium'
    if avg_score >= 80:
        return 'high'
    
col_names = ['critic_score', 'user_score']
test_low = pd.Series([10, 1.0], index=col_names)
test_med = pd.Series([65, 6.5], index=col_names)
test_high = pd.Series([99, 9.9], index=col_names)

rows = [test_low, test_med, test_high]

for row in rows:
    print(avg_score_group(row))

row_1 = pd.Series([66, 3.6], index=col_names)
row_2 = pd.Series([72, 8.1], index=col_names)
row_3 = pd.Series([99, 9.4], index=col_names)

print(avg_score_group(row_1))
print(avg_score_group(row_2))
print(avg_score_group(row_3))