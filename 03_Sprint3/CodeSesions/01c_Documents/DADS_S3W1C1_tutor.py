# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 3 - Week 1 - Class 1
# 
# Lectura, Visualización y Preprocesamiento
# 
# # Ejercicio 1: Lectura y Visualización de Datos
# 
# ## E1.1: ¿Cómo se leen archivos en formato CSV y Excel?
# 
# Podemos usar las bibliotecas `pandas` para leer archivos CSV y Excel.
# Lee ambos datasets,
# 
# -   `music.csv`
# -   `music.xlsx`

# %%
#


# %%
# Importamos pandas
import pandas as pd

# Lectura de archivo CSV
csv_data = pd.read_csv("music.csv")
print("Datos leídos del archivo CSV:")
print(csv_data.head())

# Lectura de archivo Excel
excel_data = pd.read_excel("music.xlsx")
print("\nDatos leídos del archivo Excel:")
print(excel_data.head())

# %% [markdown]
# ## E1.2 ¿Cómo podemos visualizar información general del dataset?
# 
# Imprimir:
# 
# -   Información del dataset
# -   Primeras 5 filas
# -   Últimas 5 filas
# -   Estadísticas descriptivas

# %%
#


# %%
# Información del dataset
print("Información general del archivo CSV:")
csv_data.info()

# Primeras 5 filas
print("\nPrimeras 5 filas:")
print(csv_data.head())

# Últimas 5 filas
print("\nÚltimas 5 filas:")
print(csv_data.tail())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(csv_data.describe())

# %% [markdown]
# # Ejercicio 2: Preprocesamiento y Análisis Inicial
# 
# ## E2.1: ¿Cómo tratamos valores duplicados, ausentes, y columnas irrelevantes?
# 
# Utiliza pandas para
# 
# -   Eliminar duplicados
# -   Manejar valores ausentes
# -   Quitar columnas innecesarias. Asume que necesitamos hacer un
#     análisis anonimizado

# %%
#


# %%
# Eliminar valores duplicados
csv_data_sin_duplicados = csv_data.drop_duplicates()
print("Datos después de eliminar duplicados:")
print(csv_data_sin_duplicados.head())

# Manejar valores ausentes (rellenar con un valor o eliminar)
# En este caso, vamos a rellenar los valores ausentes en la columna 'Artist' con 'Desconocido'
csv_data_sin_duplicados.loc[:,'Artist'] = csv_data_sin_duplicados.loc[:,'Artist'].fillna('Desconocido')
print("\nDatos después de tratar valores ausentes:")
print(csv_data_sin_duplicados.head())

# Eliminar una columna innecesaria, si es necesario 
csv_data_sin_duplicados = csv_data_sin_duplicados.drop(columns=['user_id'])

# Algunas alternativas podrian dar warnings por formatos deprecados (ya no soportados) u otros problemas
# csv_data_sin_duplicados.drop(columns=['user_id'], inplace=True)

# %% [markdown]
# ## E2.2: ¿Cómo agrupamos y ordenamos los datos?
# 
# Podemos agrupar los datos por columna(s) y calcular métricas como la
# suma, media, etc. También podemos ordenarlos.
# 
# -   Agrupar por género y sumar las reproducciones totales
# -   Ordenar los datos por el total de reproducciones

# %%
#


# %%
# Agrupar por género y sumar las reproducciones totales
agrupacion_genero = csv_data_sin_duplicados.groupby('genre')['total play'].sum()
print("\nSuma de reproducciones por género:")
print(agrupacion_genero)

# Ordenar los datos por el total de reproducciones
ordenado_por_reproducciones = csv_data_sin_duplicados.sort_values(by='total play', ascending=False)
print("\nDatos ordenados por el total de reproducciones:")
print(ordenado_por_reproducciones.head())

# Ordenar descendientemente la tabla agrupada por género según la cantidad de reproducciones de cada grupo
agrupacion_genero.sort_values(ascending=False)

# Error comun: Usar by para especificar columna, cuando no existen las columnas
# agrupacion_genero.sort_values(by='total play', ascending=False)

# %% [markdown]
# ------------------------------------------------------------------------
# 
# ## Notas:
# 
# -   Asegúrate de tener instaladas las bibliotecas necesarias para leer
#     archivos usando el comando: `pip install pandas` en la termina.
# -   Cambia las rutas de los archivos si no están en el mismo directorio.

