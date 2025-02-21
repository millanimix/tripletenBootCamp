# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 4 - Week 1 - Class 1
# 
# Apply y datetime
# 
# # Ejercicios
# 
# ## E1
# 
# Supongamos que tienes un DataFrame que contiene las calificaciones de
# tres exámenes para varios estudiantes. Quieres calcular el promedio de
# cada estudiante sumando las tres calificaciones y dividiendo por tres.
# Usa apply() para calcular el promedio de los exámenes para cada fila (es
# decir, para cada estudiante) y crea una nueva columna llamada promedio.

# %%
import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
    'nombre': ['Ana', 'Carlos', 'Marta', 'Luis'],
    'examen_1': [85, 90, 78, 92],
    'examen_2': [88, 85, 84, 95],
    'examen_3': [90, 87, 80, 88]
})

# %% [markdown]
# ## E2
# 
# Tienes un DataFrame con precios de productos y quieres aplicar un
# descuento del 10% solo a los productos cuyo precio sea mayor a 180. Usa
# apply() para reducir el valor de la columna precio en un 10% solo si el
# precio es mayor a 180, y crea una nueva columna llamada
# precio_con_descuento

# %%
import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({
    'producto': ['A', 'B', 'C', 'D'],
    'precio': [100, 150, 200, 250]
})

# %% [markdown]
# ## E3
# 
# Tienes un string que representa una fecha y hora. Transforma ese string
# a datetime con los siguientes formatos:
# 
# -   Año/Mes/Dia Hora:Minuto:Segundo
# -   Dia-Mes-Año Hora:Minuto

# %%
from datetime import datetime

# String de fecha-hora
fecha_hora_str = "2024/09/25 14:30:00"

# %% [markdown]
# ## E4
# 
# Convierte la columna “fecha_hora” del dataframe en datetime,
# especificando el formato *Dia-Mes-Año Hora:Minuto* y extrae la fecha,
# hora, mes y año como nuevas columnas del dataframe

# %%
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'fecha_hora': ['25-09-2024 14:30', '15-08-2024 09:15', '05-07-2024 22:45']
}
df = pd.DataFrame(data)

# %% [markdown]
# ## E5
# 
# Resuelve el mismo ejercicio anterior, pero utilizando el método apply
# para extraer la información

# %%
# 


