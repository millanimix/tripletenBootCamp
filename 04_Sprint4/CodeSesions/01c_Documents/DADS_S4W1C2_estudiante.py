# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 4 - Week 1 - Class 2
# 
# Lambda, apply, transform, map y datetime
# 
# # E1: Apply partial
# 
# -   Usando una función lambda, crea una columna llamada
#     `Confederation_Length` que contenga la longitud del nombre de cada
#     confederación (el número de caracteres en `Confederation`).
# -   ¿Hay algo raro? Investiga
# -   Si tienes problemas, intenta aplicar la función a un subconjunto de
#     la serie.
# -   Si te es más fácil, usa una función normal primero y luego
#     transfórmala a función lambda
# -   ¿Qué tan necesario es usar una función lambda en este caso?

# %%
# 

# %% [markdown]
# ------------------------------------------------------------------------
# 
# # E2: Escalamiento usando apply y lambda
# 
# -   Convierte los valores de `Points_Old_Version` en una escala de 0 a 1
#     dividiendo cada valor por el máximo de la columna. Usa `apply` para
#     realizar esta transformación y guarda el resultado en una nueva
#     columna llamada `Points_Scaled`.
# -   ¿Cómo te aseguras de no considerar nulos al calcular el máximo?

# %%
# 

# %% [markdown]
# ------------------------------------------------------------------------
# 
# # E3: Uso de Transform con funciones predefinidas
# 
# -   Crea una columna llamada `Confederation_Avg_Points` que contenga el
#     promedio de `Points_Old_Version` para cada confederación usando
#     `transform`. Esto permitirá ver los puntos promedio en función de la
#     confederación de cada país.
# -   Aquí podrías volver a utilizar funciones lambda, pero no lo hagas.
#     Llama a funciones ya creadas de alguna librería de python.

# %%
# 

# %% [markdown]
# ------------------------------------------------------------------------
# 
# # E4: Uso de Map
# 
# -   Crea un diccionario que asigne un número a cada confederación
#     (`UEFA` = 1, `CONMEBOL` = 2, etc.). Usa `map` para convertir los
#     valores de la columna `Confederation` en estos números y guarda el
#     resultado en una nueva columna llamada `Confederation_Code`.

# %%
# 

# %% [markdown]
# ------------------------------------------------------------------------
# 
# # E5: Uso de agg
# 
# -   Usa `agg` para calcular, por cada confederación, el promedio y el
#     valor máximo de las columnas `Points_Old_Version` y
#     `Points_New_Version`. Guarda los resultados en un nuevo DataFrame
#     llamado `confederation_stats`.

# %%
# 

# %% [markdown]
# ------------------------------------------------------------------------
# 
# # E6: Datetime
# 
# -   Convierte la columna `Rank_Date` al formato de fecha `datetime` y
#     extrae el año en una nueva columna llamada `Rank_Year`. Luego,
#     calcula el número de días desde la fecha de clasificación hasta el
#     día de hoy, guardando el resultado en una columna llamada
#     `Days_Since_Rank`.

# %%
# 

# %% [markdown]
# Para más detalles sobre la diferencia entre apply, transform, map y agg,
# puedes revisar estos ertículos:
# 
# -   https://towardsdatascience.com/difference-between-apply-and-transform-in-pandas-242e5cf32705
# -   https://towardsdatascience.com/pandas-apply-map-or-transform-dd931659e9cf

