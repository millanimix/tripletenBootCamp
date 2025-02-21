# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 3 - Week 1 - Class 2
# 
# Lectura, Visualización y Preprocesamiento
# 
# En este caso de estudio, vamos a analizar el comportamiento del ranking
# FIFA desde que inició su medición en el año 1993, a fin de presentar al
# público la situación y el rendimiento de las distintas selecciones
# nacionales afiliadas.
# 
# En este contexto, nos interesa contestar entre otras las siguientes
# preguntas:
# 
# -   ¿Cómo es el rendimiento histórico por confederación?
# -   ¿Cómo ha sido el rendimiento histórico de su país comparado con el
#     promedio de la confederación a la cual pertenece?
# -   ¿Cuáles han sido históricamente los mejores países?
# -   ¿Quienes han sido los top 5 países previo al inicio de cada mundial?
#     ¿Entre estos países han estado los campeones del mundo
#     correspondientes?
# -   Según esta puntuación, ¿las selecciones son cada vez más
#     competitivas o cada vez parece existir más diferencia a través del
#     tiempo?
# 
# Con este propósito usted cuenta con un conjunto de datos en el archivo
# `fifa_rank.csv` cuya metadata se detalla a continuación:
# 
# -   Fuente: FIFA Site 2018
# -   Dimensiones:
#     -   `Country`: Nombre del pais afiliado a la FIFA cuya selección de
#         fútbol es puntuada
#     -   `Confederation`: Confederación a la que pertenece de acuerdo a
#         la división de la FIFA
#     -   `Rank_Date`: Fecha de publicación del ranking FIFA entre marzo
#         de 1993 y junio de 2018 (previo al mundial de Rusia)
#     -   `Points_Old_Version`: Puntos obtenidos conforme el sistema
#         antiguo de la FIFA (previo al año 2011)
#     -   `Ponts_New_Version`: Puntos obtenidos conforme el sistema nuevo
#         de la FIFA (a partir del años 2011)
#     -   `rank`: Posición en el ranking oficial de la FIFA dados los
#         puntos calculados
# 
# ## CARGAR LIBRERIAS Y DATOS

# %%
#Cargar librerias
import pandas as pd
import numpy as np

# %% [markdown]
# ### E1: Ajustar ruta relativa según contexto

# %%
#Cargar datos
df_fifa = pd.read_csv("fifa_rank.csv", sep = ",")

# %% [markdown]
# ## DIAGNÓSTICO INICIAL

# %%
#Visualizar información general de los datos
df_fifa.info()


# %%
#Visualizar cabecera de los datos
df_fifa.head(n = 10)


# %%
#Visualizar una muestra aleatoria de los datos
df_fifa.sample(n = 10)

# %% [markdown]
# ## PROCESAMIENTO
# 
# ### E2: Ajustar nombres de columnas
# 
# -   Poner todos los nombres de columnas en minusculas
# 
# ### E3: Visualizar datos en confederation
# 
# -   Visualizar cuantos casos hay por confederation
# %% [markdown]
# ### E4: Ajustar formato de columna rank_date
# 
# -   Cambiar a formato fecha
# 
# ### E5: Adicionar columnas de año y mes
# 
# -   Crear campo `year`
# -   Crear campo `month`
# -   Cuantos casos hay por cada mes y año
# -   Hacer un primer grafico considerando que existen demasiados casos
# %% [markdown]
# ### E6: Visualizar datos en Points_Old_Version
# 
# -   Visualizar cuantos casos hay para cada valor posibles
# -   Visualizar cuantos NA hay por año - mes
# %% [markdown]
# ### E7: Visualizar datos en Points_New_Version
# 
# -   Visualizar cuantos casos hay para cada valor posibles
# -   Visualizar cuantos “no definidos” (ND) hay por año

