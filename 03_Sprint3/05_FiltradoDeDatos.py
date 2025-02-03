# Filtrado de datos
import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'])
print(oceans)
# Atributo index
print(oceans.index)
print(type(oceans.index))
print('\nIndice personalizado')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'])
oceans.index = [1, 2, 3, 4, 5]
print(oceans)
print(oceans.index)
print(type(oceans.index))
print('\nOtra forma de estableces indices')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'],
                   index=[1, 2, 3, 4, 5])
print(oceans)
print(oceans.index)
print(type(oceans.index))
print('\nIndices como cadenas')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'],
                   index=['A', 'B', 'C', 'D', 'E'])
print(oceans)
print(oceans.index)
print(type(oceans.index))


print('\nIndexación mediante loc[]\n')
states = ['Alabma', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camelia', 'Foget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-Spotted skimmer dragonfly', 'Two-tailed swallowtail', 'Europen honey bee']
index = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
print(df)
print('\nArkansas insect is:')
print(df.loc['state 4', 'insect'])
print(df.loc['state 1':'state 3','flower'])
print(df.loc['state 1':'state 3', 'flower':'insect'])

print('\nIndexación mediante iloc[]')
print(df.iloc[3,2])
print(df.iloc[[0,2],1:])

print('\nIndexación negativa con iloc[]')
print(df.iloc[[0,2], -1])

print('\nMétodo set_index()')
states = ['Alabma', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camelia', 'Foget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-Spotted skimmer dragonfly', 'Two-tailed swallowtail', 'Europen honey bee']
index = ['state 1', 'state 2', 'state 3', 'state 4']
print('DataFrame Original')
df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
print(df)
print('DataFrame con nuevo indice')
df = df.set_index('state')
print(df)
print()
print(df.index)

print('\nEliminando el nombre del indice')
df.index.name = None
print(df)
print()
print(df.index)

print('\nFiltrado personalizado de mediante query()')
df = pd.read_csv('03_Sprint3/datasets/vg_sales.csv')
print(df.head())
print()
print(df.info())

print('\nFiltrado con strings de consulta y el método query()')
print(df.query("publisher == 'Nintendo'")[['name', 'publisher']].head())

print('\nFiltrado mediante el método isin()')
handhelds = ['3DS', 'DS', 'GB', 'GBA', 'PSP']
print(df[~df['platform'].isin(handhelds)][['name', 'platform']])
print('\nFiltrado con query y parametro in')
print(df.query("platform in @handhelds")[['name', 'platform']])

print('\nFiltrado ventas de Japón superior a un millón')
print(df.query("jp_sales > 1.00")[['name', 'jp_sales']])

print('\nEjercicio 2')
print(df.head(5)[['name','publisher','developer']])
cols = ['name', 'publisher', 'developer']
df_filtered = df.query("publisher == developer")[cols]
print(df_filtered.head(5))

print('\nEjercicio 3')
print(df.query("platform not in @handhelds")[['name', 'platform']])

print('\nActividad Practica')
print('Ejercicio 1')
print(df['genre'].unique())

print('\nEjercicio 2')
cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

df_filtered = df[~df['genre'].isin(s_genres)][cols]
print(df_filtered)

print('\nEjercicio 3')
df_filtered = df.query("genre not in @s_genres")[cols]
print(df_filtered)

print('\nUso de estructura de datos externas para filtrar DataFrames')
our_list = [2, 5, 10]
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
    }
)
print(df)
print()
print(our_list)
print()
print(df.query("a in @our_list"))

print('\nFiltrado con un diccionario')
our_dict = {0: 10, 3: 11, 12: 12}
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z']
    }
)
print(df)
print()
print(our_dict)
print()
# Query con los valores
print(df.query("a in @our_dict.values()"))
# Query con la llaves
print(df.query("a in @our_dict"))

print('\nFiltrado con Series')
our_series = pd.Series([10, 11, 12])
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z']
    }
)
print(df)
print()
print(our_series)
print()
print(df.query("a in @our_series"))
print(df.query("a in @our_series.index"))

print('\nFiltrado con un DataFrame')
our_df = pd.DataFrame(
    {
        'A': [10, 11, 12]
    }
)
df = pd.DataFrame(
    {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z']
    }
)
print(df)
print()
print(our_df)
print()
# Filtrar con valores
print(df.query("a in @our_df.A"))
# Filtrar con indices
print(df.query("a in @our_df.index"))

print('\nActividad práctica')
print('\nEjercicio 1')
import pandas as pd

# Crear DataFrame de productos
datos = {
    'nombre': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet'],
    'categoría': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Oficina', 'Electrónica'],
    'precio': [1000, 25, 50, 300, 150, 400]
}
productos = pd.DataFrame(datos)
print("Datos de productos:\n", productos)
categorias_deseadas = ['Electrónica', 'Oficina']
productos_filtrados = productos.query("categoría in @categorias_deseadas")
print("\nProductos filtrados por categoría:\n", productos_filtrados)

print('\nEjercicio 2')
datos_ventas = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet'],
    'ventas': [150, 500, 300, 120, 80, 200]
}
ventas = pd.DataFrame(datos_ventas)
datos_stock = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet', 'Cargador'],
    'stock': [50, 200, 150, 75, 30, 100, 60]
}
stock = pd.DataFrame(datos_stock)
print("Datos de ventas:\n", ventas)
print("\nDatos de stock:\n", stock)
productos_más_vendidos = pd.Series(['Mouse', 'Tablet', 'Teclado'])
# ventas_filtradas = ventas.query("producto in @productos_más_vendidos")
ventas_filtradas = ventas[ventas['producto'].isin(productos_más_vendidos)]
print("\nVentas filtradas (productos más vendidos):\n", ventas_filtradas)

print('\nFiltering with multiple logic conditions')
df = pd.read_csv('03_Sprint3/datasets/vg_sales.csv')
print(df)
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
print(df)
# Ver todos los juegos de Wii que no son deportes
print(df[(df['platform'] == 'Wii') & ~(df['genre'] == 'Sports')].head())
# Todos los juegos que superaron el millon en al menos una de tres regiones
print(df[(df['na_sales'] >= 1) | (df['eu_sales'] >= 1) | (df['jp_sales'] >= 1)].head())

print('\nCondiciones múltiples con query()')
print(df.query("platform == 'Wii' and genre != 'Sports'").head())

print('\nEjercicio 1')
df_filtered = df.query("year_of_release >= 1980 and year_of_release <= 1989")
print(df_filtered)

print('\nEjercicio 2')
q_string = "na_sales >= 1 or eu_sales >= 1 or jp_sales >= 1"
print(df.query(q_string).head(5)) 

print('\nActividad practica')
print('Ejercicio 1')

df = pd.read_csv('03_Sprint3/datasets/vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

developers = ['SquareSoft', 'Enix Corporation', 'Square Enix']
cols = ['name', 'developer', 'na_sales', 'eu_sales', 'jp_sales']

q_string = "(na_sales > 0 and eu_sales > 0 and jp_sales > 0) and (jp_sales > na_sales + eu_sales) and (developer == @developers)"
df_filtered = df.query(q_string)[cols]
print(df_filtered)