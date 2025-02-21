# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 2 - Week 1 - Class 1
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
# # Objetivo
# 
# Comprender el uso de bucles y condicionales mediante su aplicación a un
# caso práctico, para optimizar el procesamiento de datos.
# 
# # Contexto
# 
# La empresa Aleph, se encuentra en proceso de digitalización de su
# información, que ha sido manejada de forma desordenada en cuadernos
# físicos.
# 
# Tu trabajo es crear un registro de clientes.
# 
# # Ejercicios
# 
# ## Ejercicio 1 - Bucles for
# 
# ### E1.1
# 
# La empresa cuenta con 6 clientes: Juan, Pedro, Nicole, Cayetana, Diego y
# Pilar. Crea una lista que contenga todos los clientes y otra donde esté
# especificado su sexo con “M” o “F” según corresponda. Pon como nombres
# de estas listas `cli_nombre` y `cli_sexo`.

# %%
cli_nombre = ["Juan", "Pedro", "Nicole", "Cayetana", "Diego", "Pilar"]
cli_sexo = ["M", "M", "F", "F", "M", "F"]

# %% [markdown]
# ### E1.2
# 
# Usando un for, imprime el nombre y sexo de cada cliente en lineas
# diferentes.

# %%
#Forma 1
for i in range(len(cli_nombre)):
    print(cli_nombre[i], cli_sexo[i])


# %%
#Forma 2
for nombre, sexo in zip(cli_nombre, cli_sexo):
    print(nombre, sexo)

# %% [markdown]
# ## Ejercicio 2 - Bucles for anidados
# 
# ### E2.1
# 
# Crea una lista anidada llamada `cli_registro` que contenga la
# información del nombre, sexo y edad de los 6 clientes.
# 
# Para conocer la edad de los clientes considera: - Diego tiene 72 años -
# Diego es dos años mayor que Pilar - Cayetana tiene 40 años menos que
# Pilar - Nicole es 15 años mayor que Cayetana - Juan tiene la misma edad
# que Pedro - Pedro tiene 1 año más que Nicole

# %%
edad_diego = 72
edad_pilar = edad_diego - 2
edad_cayetana = edad_pilar - 40
edad_nicole = edad_cayetana + 15
edad_pedro = edad_nicole + 1
edad_juan = edad_pedro

cli_registro = [
    ['Juan', 'M', edad_juan],
    ['Pedro', 'M', edad_pedro],
    ['Nicole', 'F', edad_nicole],
    ['Cayetana', 'F', edad_cayetana],
    ['Diego', 'M', edad_diego],
    ['Pilar', 'F', edad_pilar]
]

# %% [markdown]
# Usando `cli_registro` y un usando un bucle `for`, imprime la información
# de cada linea en este formato:
# 
# *El nombre del cliente es **, su sexo es*** , y tiene \_\_\_ años

# %%
for row in cli_registro:
    print(f"El nombre del cliente es {row[0]}, su sexo es {row[1]}, y tiene {row[2]} años")

# %% [markdown]
# ### E2.2
# 
# Imprime el nombre con la edad de cada cliente entre parentesis (solo la
# edad entre paréntesis).

# %%
for row in cli_registro:
    print(f"{row[0]} ({row[2]})")

# %% [markdown]
# ## Ejercicio 3 - Bucles while
# 
# ### E3.1
# 
# La empresa quiere crear una lista que contenga a cada cliente 12 veces
# para, posteriormente, agregar la información de ventas mensuales para el
# año que culminó.
# 
# Usando un bucle while crea la lista deseada con el nombre
# `cli_repeticion`, e imprimela para ver si funcionó lo que se hizo.

# %%
repeticiones_por_cliente = 12
indice_de_repeticion = 1
cli_repeticion = cli_registro.copy()

while indice_de_repeticion < repeticiones_por_cliente:
    cli_repeticion += cli_registro
    indice_de_repeticion += 1

print(cli_repeticion)

# %% [markdown]
# Por qué usamos `copy`? Qué pasa si no usamos copy? Inténtalo. Investiga
# qué hace copy y entiende qué son y cómo se ocupan los punteros a la
# memoria.
# 
# ### E3.2
# 
# Hay una forma mucho más simple de creer esta lista anidada. Cuál es,
# hazlo en 1 línea

# %%
cli_registro*12

# %% [markdown]
# ## Ejercicio 4 - Sentencias condicionales
# 
# ### E4.1
# 
# Usando bucles y sentencias condicionales verifica que en la lista
# `cli_repeticion`, el cliente “Cayetana” este repetida las 12 veces
# deseadas

# %%
contador = 0

for cliente in cli_repeticion:
    if cliente[0] == "Cayetana":
        contador += 1

print("Cayetana se repite", contador, "veces")

# %% [markdown]
# ### E4.2
# 
# Vuelva a la lista anidada `cli_registro` y usando bucles y sentencias
# condicionales imprime únicamente las líneas que contengan a clientes que
# sean mujeres.

# %%
print(cli_registro)


# %%
for row in cli_registro:
    if row[1] == 'F':
        print(row)

# %% [markdown]
# ### E4.3
# 
# Ahora modifica el código anterior para que si el cliente es hombre
# imprima su edad únicamente.

# %%
for row in cli_registro:
    if row[1] == 'F':
        print(row)
    else:
        print(row[2])

# %% [markdown]
# ### E4.4
# 
# A partir del código ya escrito, imprime un resumen que indique cuántos
# hombres y cuantas mujeres hay en la lista de clientes, y en cada caso
# indica cual es la edad promedio (redondeado sin decimales).

# %%
hombres = []
mujeres = []
for row in cli_registro:
    if row[1] == 'F':
        mujeres.append(row[2])
    else:
        hombres.append(row[2])

print(f"""
Cantidad de hombres: {len(hombres)} 
Edad promedio: {int(sum(hombres)/len(hombres))}
""")
print(f"""
Cantidad de mujeres: {len(mujeres)} 
Edad promedio: {int(sum(mujeres)/len(mujeres))}
""")

# %% [markdown]
# ### E4.5
# 
# La empresa considera que su mercado relevante son las mujeres mayores a
# 55 y los hombres menores a 50.
# 
# A partir de este criterio, imprime la información de todos los clientes
# que son parte del mercado relevante. En caso que no sean parte del
# mercado, imprime un mensaje que indique “Cliente \_\_\_ no es parte del
# mercado relevante”.

# %%
for row in cli_registro:
    if row[1] == 'F' and row[2] > 55:
        print(row)
    elif row[1] == 'M' and row[2] < 50:
        print(row)
    else:
        print(f'Cliente {row[0]} no es parte de mercado relevante')

# %% [markdown]
# ### E4.6
# 
# Ha llegado nueva información donde se especifica que los nombres
# completos de los clientes son:
# 
# -   Juan Araujo
# -   Pedro Paez
# -   Nicole Srolis
# -   Cayetana Araujo
# -   Diego Araujo
# -   Pilar Paez
# 
# Mediante bucles y condicionales has la modificación correspondiente en
# `cli_registro`.

# %%
# Nombres completos de los clientes
nombres_completos = [
    "Juan Araujo", "Pedro Paez", "Nicole Srolis",
    "Cayetana Araujo", "Diego Araujo", "Pilar Paez"
]

cli_registro_actualizado = cli_registro.copy()

for indice_registro in range(len(cli_registro_actualizado)):
  cli_registro_actualizado[indice_registro][0] = nombres_completos[indice_registro]

for registro in cli_registro_actualizado:
    print(registro)


