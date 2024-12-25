# 02_LeerVisualizarDatos

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '03_Sprint3/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)
print(data.head())


# Alternativa para leer archivo CSV

# column_names = ['nombre', 'deporte', 'edad', 'salario']
# df = pd.read_csv("/datasets/sports.csv", sep = ';', header = None, names = column_names, decimal = ',')
# print(df.head())

df = pd.read_csv('03_Sprint3/datasets/letters_colors_decimals.csv', header=0, sep='$', decimal='a')

print(df.head())

print()
print('Leer archivos en excel')
print()

df = pd.read_excel('03_Sprint3/datasets/product_reviews.xlsx')
print(df.head())

# Cargar otras hojas de un excel
df = pd.read_excel('03_Sprint3/datasets/product_reviews.xlsx', sheet_name='reviewers')
print(df.head())

# Ordenar una columna descendente
df_categories = pd.read_excel('03_Sprint3/datasets/product_reviews.xlsx', sheet_name='product_categories')
df_categories = df_categories.sort_values(by='category', ascending=False)
print(df_categories)

# Observación de los datos
print()
print('Observación de los datos')
print()
column_names = [
    'country',
    'name',
    'latitude',
    'capacity_mw',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '03_Sprint3/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=','
)
data.info()

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '03_Sprint3/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)
print(data.sample(5, random_state=1369))

print()
print('Descripciones numéricas y describe()')
print()

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '03_Sprint3/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=','
)

print(data.describe())
print()
print(data.describe(include='object'))
print()
print(data.describe(include='all'))
print()
print(data['country'].describe())

print()
print()

data = pd.read_csv('03_Sprint3/datasets/Driver_Details.csv')
print(data.sample(5))
print()
print(data.describe(include='object'))
print()
print(data['nationality'].describe())
nacionalidad = 'British' 
n_nacionalidades = 42