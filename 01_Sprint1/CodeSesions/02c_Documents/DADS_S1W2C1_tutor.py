# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 1 - Week 2 - Class 1
# 
# Análisis de Datos del Mercado de Valores
# 
# Supongamos que tienes un conjunto de datos simple que contiene el
# historial de precios de cierre de una acción durante una semana. Los
# precios están en una lista en orden cronológico (de lunes a viernes).
# 
# Lista de precios de cierre de la acción:
# `[150.25, 152.35, 149.75, 153.20, 151.50]`

# %%
lista_precios = [150.25, 152.35, 149.75, 153.20, 151.50]

# %% [markdown]
# # Ejercicio 1 - Acceso a elementos individuales
# 
# -   Imprime el precio de cierre del miércoles.
# -   Imprime el precio de cierre del primer día de la semana (lunes).

# %%
lista_precios[2]
lista_precios[0]

# %% [markdown]
# # Ejercicio 2 - Slicing
# 
# -   Crea una nueva lista llamada `precios_mitad_semana` que contenga los
#     precios de cierre desde el martes hasta el jueves (inclusive).
# -   Crea otra lista llamada `precios_invertidos` que contenga los
#     precios de cierre de la semana en orden inverso.

# %%
precios_mitad_semana = lista_precios[1:4]
precios_invertidos = lista_precios[::-1]

# %% [markdown]
# # Ejercicio 3 - Sublistas y operaciones
# 
# -   Calcula la diferencia entre el precio de cierre del viernes y el
#     lunes, y guárdala en una variable llamada `diferencia_semana`.
# -   Calcula el promedio de los precios de la mitad de la semana (usando
#     la lista `precios_mitad_semana` que creaste en la sección de
#     slicing).

# %%
diferencia_semana = lista_precios[4] - lista_precios[0]

promedio_mitad_semana = sum(precios_mitad_semana) / len(precios_mitad_semana)

# %% [markdown]
# # Ejercicio 4 - Manipulación de cadenas de caracteres
# 
# -   Supón que tienes una lista de días de la semana:
#     `["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]`.
# -   Une esta lista en una única cadena de texto separada por comas, y
#     guárdala en una variable llamada `dias_semana`.
# -   A partir de la cadena `dias_semana`, extrae y almacena en una nueva
#     variable el nombre del día “Miércoles” usando slicing y la posición
#     del índice.

# %%
dias_semana_lista = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

dias_semana = ", ".join(dias_semana_lista)

dia_miercoles = dias_semana[15:24]

# %% [markdown]
# # Ejercicio 5 - Listas anidadas
# 
# Supón que tienes un conjunto de datos que representa los precios de
# cierre de varias acciones durante una semana. Cada acción tiene su
# propio historial de precios para los cinco días de la semana (de lunes a
# viernes), y todos estos precios están almacenados en una lista anidada.
# 
# Lista de precios de cierre de tres acciones:

# %%
precios_acciones = [
    [150.25, 152.35, 149.75, 153.20, 151.50],  # Acción 1
    [120.10, 121.50, 119.80, 122.35, 121.00],  # Acción 2
    [95.75, 97.50, 96.20, 98.10, 97.00]        # Acción 3
]

# %% [markdown]
# ## E5.1 - Acceso a elementos en listas anidadas
# 
# -   Imprime el precio de cierre del miércoles de la Acción 2.
# -   Imprime el precio de cierre del lunes de la Acción 3.

# %%
precio_miercoles_accion2 = precios_acciones[1][2]
precio_lunes_accion3 = precios_acciones[2][0]

# %% [markdown]
# ### E5.2 - Slicing en listas anidadas
# 
# -   Crea una nueva lista llamada `precios_martes_jueves_accion1` que
#     contenga los precios de cierre desde el martes hasta el jueves de la
#     Acción 1.
# -   Crea otra lista llamada `precios_invertidos_accion3` que contenga
#     los precios de cierre de la semana para la Acción 3 en orden
#     inverso.

# %%
precios_martes_jueves_accion1 = precios_acciones[0][1:4]
precios_invertidos_accion3 = precios_acciones[2][::-1]

# %% [markdown]
# ### E5.3 - Operaciones con listas anidadas
# 
# -   Calcula la diferencia entre el precio de cierre del viernes y el
#     lunes para la Acción 2, y guárdala en una variable llamada
#     `diferencia_accion2`.
# -   Calcula el promedio de los precios de cierre del miércoles de todas
#     las acciones (utilizando los datos anidados).

# %%
diferencia_accion2 = precios_acciones[1][4] - precios_acciones[1][0]

precios_miercoles = [accion[2] for accion in precios_acciones]
promedio_miercoles = sum(precios_miercoles) / len(precios_miercoles)


