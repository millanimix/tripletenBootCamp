# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 2 - Week 1 - Class 2
# 
# Bucles y condicionales
# 
# # Temas a tratar
# 
# -   Bucles
#     -   Bucles for
#     -   Bucles while
# -   Condicionales
#     -   Operadores lógicos
#     -   Sentencias if, else y elif
#     -   Filtrado de tablas
# 
# # Contexto:
# 
# Trabajas para una empresa ficticia llamada *DataInsight Co.*, que se
# dedica a la consultoría de análisis de datos para mejorar la eficiencia
# de los equipos de ventas. La empresa recopila información sobre las
# ventas de productos en varias sucursales y, como analista de datos,
# debes realizar varias tareas para ayudar a identificar tendencias y
# mejorar el rendimiento.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 1: Revisión de ventas por sucursal (Bucles `for` sobre listas anidadas)
# 
# *Descripción:*  
# Tienes un conjunto de datos anidado con el formato `ventas_sucursales`,
# donde cada sublista contiene las ventas (en dólares) de cada día de la
# semana (lunes a viernes) en diferentes sucursales. Debes escribir un
# programa que recorra todas las sucursales e imprima el total de ventas
# de cada una.

# %%
ventas_sucursales = [
    [500, 700, 800, 600, 400],  # Sucursal 1
    [450, 650, 850, 700, 300],  # Sucursal 2
    [700, 900, 950, 800, 600]   # Sucursal 3
]

# Recorre las listas anidadas para calcular el total de ventas de cada sucursal


# %%
for i, sucursal in enumerate(ventas_sucursales, start=1):
    total_ventas = sum(sucursal)
    print(f"El total de ventas de la sucursal {i} es: {total_ventas}")

# %% [markdown]
# *Objetivo:*  
# Usar un bucle `for` para recorrer las listas anidadas y calcular el
# total de ventas por sucursal.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 2: Evaluación de la tendencia de ventas (Bucles `while`)
# 
# *Descripción:*  
# Se quiere analizar si las ventas diarias de una sucursal específica
# están mejorando, manteniéndose o empeorando. Tienes los datos de las
# ventas diarias en una lista y debes usar un bucle `while` para recorrer
# los datos hasta que encuentres una caída en las ventas o hasta que todas
# las ventas hayan sido revisadas.

# %%
ventas_diarias = [500, 550, 600, 620, 580, 590, 620, 610]

# Utiliza un bucle while para detectar si hay una caída en las ventas diarias


# %%
# Inicializamos los índices
i = 1  # Comenzamos en el segundo día para comparar con el primero

# Bucle while para recorrer las ventas diarias
while i < len(ventas_diarias):
    if ventas_diarias[i] < ventas_diarias[i - 1]:
        print(f"Caída en las ventas detectada el día {i + 1}.")
        break
    else:
        print("No se detectaron caídas en las ventas.")
    i += 1

# %% [markdown]
# *Objetivo:*  
# Implementar un bucle `while` que verifique día a día si las ventas son
# mayores o iguales que el día anterior, imprimiendo un mensaje cuando
# haya una caída.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 3: Filtro de ventas exitosas (Operadores lógicos)
# 
# *Descripción:*  
# La empresa considera que una venta es exitosa si supera los \$600 y se
# realizó entre miércoles y viernes. Debes crear un programa que
# identifique todas las ventas exitosas en una sucursal y muestre los días
# en los que ocurrieron. Toma datos de una sola sucursal y llámalos
# `ventas_sucursal = ventas_sucursales[0]`

# %%
ventas_sucursal = ventas_sucursales[0]  # Lunes a Viernes

# Filtra las ventas que fueron superiores a $600 y ocurrieron de miércoles a viernes (índices 2 a 4)


# %%
# Definir los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Filtrar las ventas que fueron superiores a $600 y ocurrieron de miércoles a viernes (índices 2 a 4)
for i in range(2, 5):  # Miércoles (índice 2), Jueves (índice 3) y Viernes (índice 4)
    if ventas_sucursal[i] > 600:
        print(f"Venta exitosa de ${ventas_sucursal[i]} ocurrió el {dias_semana[i]}")

# %% [markdown]
# *Objetivo:*  
# Utilizar operadores lógicos para filtrar ventas que cumplan ambas
# condiciones.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 4: Clasificación de sucursales (Sentencias `if`, `else`, `elif`)
# 
# *Descripción:*  
# Las sucursales de *DataInsight Co.* se clasifican en “Bajo rendimiento”,
# “Rendimiento promedio” y “Alto rendimiento” según sus ventas semanales.
# Si el total de ventas de la semana es menor a \$2500, se considera “Bajo
# rendimiento”. Si está entre \$2500 y \$3500, es “Rendimiento promedio”.
# Por encima de \$3500 es “Alto rendimiento”. Debes escribir un programa
# que reciba las ventas semanales de una sucursal y clasifique su
# rendimiento. Usa la sucursal en `ventas_sucursal`.

# %%
# Calcula el total de ventas y clasifica la sucursal usando if, elif, else


# %%
# Calcula el total de ventas semanales
total_ventas = sum(ventas_sucursal)

# Clasificación de la sucursal según su rendimiento
if total_ventas < 2500:
    clasificacion = "Bajo rendimiento"
elif 2500 <= total_ventas <= 3500:
    clasificacion = "Rendimiento promedio"
else:
    clasificacion = "Alto rendimiento"

print(f"El total de ventas de la sucursal es: ${total_ventas}. Clasificación: {clasificacion}")

# %% [markdown]
# *Objetivo:*  
# Aplicar sentencias condicionales para clasificar una sucursal según el
# total de sus ventas.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 5: Filtrado de ventas por productos (Filtrado en tablas con listas anidadas)
# 
# *Descripción:*  
# Cada sucursal vende tres productos: A, B y C. Tienes una tabla que
# representa las ventas diarias de cada producto en la sucursal. Tu tarea
# es escribir un programa que filtre y muestre solo las ventas del
# producto B, que corresponde a la segunda columna de cada sublista.

# %%
ventas_por_producto = [
    [100, 200, 300],  # Día 1 (A, B, C)
    [150, 250, 400],  # Día 2
    [200, 300, 500],  # Día 3
    [130, 270, 330],  # Día 4
    [170, 290, 380]   # Día 5
]

# Filtra y muestra solo las ventas del producto B (columna 2)


# %%
for dia, ventas in enumerate(ventas_por_producto, start=1):
    print(f"Ventas del producto B el día {dia}: ${ventas[1]}")

# %% [markdown]
# *Objetivo:*  
# Filtrar y extraer datos de una lista anidada usando un bucle `for`.
# 
# ------------------------------------------------------------------------
# 
# # Ejercicio 6: Generalización de la solución (pregunta bonus usando funciones)
# 
# Toma los ejercicios del 1 al 5. Estos sirves para una sola sucursal.
# ¿Cómo crearías una función a partir de esto y la aplicarías a múltiples
# sucursales en `ventas_sucursales`? Hazlo de tarea para cada ejercicio.
# 
# *Objetivo:* Abstraer los problemas anteriores y generalizarlos con una
# función. Así, evitaremos duplicar código y ganaremos consistencia.
# 
# ------------------------------------------------------------------------

