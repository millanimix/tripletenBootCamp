# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 6 - Week 1 - Class 1
# 
# Tratamiento de datos de juegos
# 
# # Librerías y datos a utilizar

# %%
#Importar librerias relevantes
import pandas as pd
pd.options.display.max_columns = None
import numpy as np
from scipy import stats as st

#Leer archivo de trabajo
df_games = pd.read_csv("games.csv", sep = ",")

# %% [markdown]
# # Diagnóstico inicial
# 
# ## E1: Info, head y conteo de nulos
# 
# Obtén:
# 
# -   Informacion general
# -   Cabecera
# -   Conteo de valores perdidos

# %%
# Informacion general
df_games.info()

# Cabecera
df_games.head(10)

# Conteo de valores perdidos
df_games.isna().sum()

# %% [markdown]
# # Preparación de datos
# 
# ## E2: Nombres de columnas
# 
# -   Poner los nombres de las columnas en minusculas

# %%
#Poner los nombres de las columnas en minusculas
nombres = list(df_games.columns)
nombres_new = [nombre.lower() for nombre in nombres]
df_games.columns = nombres_new
df_games.columns

# %% [markdown]
# ## E3: Columna names
# 
# -   Imprime una tabla con nombre del juego y un conteo de veces que se
#     repite ese nombre, ordenado de mayor a menor
# -   Poner todos los nombres en minúsculas
# -   Quitar espacios al inicio o al final
# -   Borrar todos los “:”
# -   Verifica cómo quedó esa columna luego de las modificaciones

# %%
#Visualizar casos
df_games['name'].value_counts(dropna=False).sort_values(ascending=False)

df_games['name'] = df_games['name'].str.lower().str.strip().str.replace(":","")

df_games['name'].value_counts(dropna=False).sort_values(ascending=False)

# %% [markdown]
# ## E4: Missing values - columna name
# 
# -   Identificar los casos perdidos para columna “name”
# -   Reemplazar los missing values por algún valor que te parezca
#     razonable (si es que reemplazar te parece razonable)

# %%
#Identificar los casos perdidos
df_games[df_games['name'].isna()]

#Reemplazar datos perdidos
df_games['name'] = df_games['name'].fillna("not_defined")
df_games[df_games['name'] == "not_defined"]

# %% [markdown]
# ## E5: Columna platform_group
# 
# -   Crear grupos de plataformas y guardalos en una nueva columna llamada
#     platform_group.

# %%
#Visualizar casos
df_games['platform'].value_counts(dropna=False).sort_index(ascending=True)

#Crear grupo de Plataformas
def GrupoPlat (x):
    if x in ['3DS','DS','GB','GBA','GC','N64','NES','SNES','Wii','WiiU']:
        return "Nintendo"
    elif x in ['PC','PCFX']:
        return "PC"
    elif x in ['PS','PS2','PS3','PS4','PSP','PSV']:
        return "PlayStation"
    elif x in ['X360','XB','XOne']:
        return "XBox"
    else:
        return "Other"
        
df_games['platform_group'] = df_games['platform'].apply(GrupoPlat)
df_games.sample(10)

df_games['platform_group'].value_counts()

# %% [markdown]
# ## E6: Columna Year of Release
# 
# -   Visualizar casos
# -   Identificar los casos perdidos
# -   SIN imputar, extrae estadísticas básicas respecto a esta columna.
#     Hay muchas formas de hacerlo. Para una de ellas, te puede servir
#     usar `.notnull()` dentro de un `query`.

# %%
#Visualizar casos
df_games['year_of_release'].describe()

#Identificar los casos perdidos
df_games[df_games['year_of_release'].isna()]

df_games.query("year_of_release.notnull()")['year_of_release'].describe()


