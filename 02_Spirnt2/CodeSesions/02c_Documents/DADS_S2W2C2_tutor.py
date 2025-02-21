# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 2 - Week 2 - Class 2
# 
# Diccionarios y funciones
# 
# # Objetivo
# 
# Comprender el uso de diccionarios y funciones mediante su aplicación a
# un caso práctico, para ejecutar scripts complejos.
# 
# # Diccionarios
# 
# ## Ejemplo 1.1
# 
# La empresa Aleph ha revisado la información que digitalizó y le menciona
# que si bien los datos de clientes son correctos, quisiera que se trabaje
# con una estructura de datos tipo diccionario para garantizar la
# inmutabilidad de los registros históricos.
# 
# Visto esto, cree un diccionario que contenga la información de nombre y
# edad según lo descrito en la siguiente lista. Utilice el nombre como
# clave para su diccionario al que llamara `cli_edad_dicc`.

# %%
cli_registro = [
     ['Juan Araujo', 'M', 46],
     ['Pedro Paez', 'M', 46],
     ['Nicole Srolis', 'F', 45],
     ['Cayetana Araujo', 'F', 30],
     ['Diego Araujo', 'M', 72],
     ['Pilar Paez', 'F', 70]
]


# %%
cli_edad_dicc = {}
for registro in cli_registro:
    cli_edad_dicc[registro[0]] = [registro[1]]

print(cli_edad_dicc)

# %% [markdown]
# ## Ejemplo 1.2
# 
# Para no perder la información ya levantada cree otro diccionario
# `cli_info_dicc` que contenga la información del sexo y la edad de cada
# cliente.

# %%
# 


# %%
cli_info_dicc = {}
for registro in cli_registro:
    cli_info_dicc[registro[0]] = [registro[1], registro[2]]

print(cli_info_dicc)

# %% [markdown]
# Realice una consulta para conocer la información demográfica de Pilar
# Paez.

# %%
# 


# %%
#Forma 1
cli_info_dicc['Pilar Paez']


# %%
#Forma 2
cli_info_dicc.get('Pilar Paez')

# %% [markdown]
# ## Ejemplo 1.3
# 
# El director de ventas de la empresa le indica que olvidó pasarle
# información de un cliente adicional con la siguiente información:
# 
# -   Nombre: Sofia
# -   Apellido: Pozo
# -   Edad: 29
# 
# Ingrese este nuevo cliente en el diccionario.

# %%
# 


# %%
cli_info_dicc['Sofia Pozo'] = ['F',29]

print(cli_info_dicc)

# %% [markdown]
# ## Ejemplo 1.4
# 
# Por otra parte, el director le menciona que el cliente Juan Araujo
# prefiere ser tratado con su segundo nombre “Sebastian”, por lo que le
# pide hacer este ajuste en el diccionario

# %%
# 


# %%
cli_info_dicc_2 = cli_info_dicc.copy()

# Forma 1
del cli_info_dicc['Juan Araujo']

print(cli_info_dicc)

cli_info_dicc['Sebastian Araujo'] = ['M',46]

print(cli_info_dicc)


# %%
# Forma 2
cli_info_dicc_2.pop('Juan Araujo') # No funciona si ya se ejecutó la celda anterior

cli_info_dicc_2['Sebastian Araujo'] = ['M',46]

print(cli_info_dicc_2)

# %% [markdown]
# # Funciones
# 
# ## Ejemplo 2.1
# 
# El director de ventas cree que es conveniente saber el año de nacimiento
# de cada uno de los clientes, puesto que de esa forma se podrá tener un
# mejor control del grupo etareo de clientes en el futuro.
# 
# Cree una función que devuelva el año de nacimiento de cada cliente. No
# importa en qué año estemos, establezca el año actual como un parámetro
# adicional `y_actual` de su función.

# %%
#


# %%
def year_birth (edad, y_actual = 2024):
  y_nacim = y_actual - edad
  y_nacim = int(y_nacim)
  return y_nacim

# %% [markdown]
# Mediante un bucle for aplique a cada edad de cada cliente la función
# construida y adicione la edad por el año de nacimiento.

# %%
#


# %%
for val in cli_info_dicc.values():
  y_nac = year_birth(val[1])
  val.append(y_nac)

cli_info_dicc

# %% [markdown]
# ## Ejemplo 2.2
# 
# Haz una función que tome un diccionario como el anterior y entregue una
# lista de listas de esta forma `[Sexo,Edad_Promedio]` (cada sublista debe
# tener un sexo y el promedio de edades para ese sexo).

# %%
#


# %%
def prom_edad(diccionario):

    mujeres = []
    hombres = []

    for val in diccionario.values():
        if val[0] == "F":
            mujeres.append(val[1])
        else:
            hombres.append(val[1])

    mujeres_prom = sum(mujeres)/len(mujeres)
    hombres_prom = sum(hombres)/len(hombres)

    lista_final = [["F", int(mujeres_prom)], ["M", int(hombres_prom)]]

    return lista_final
  
prom_edad(cli_info_dicc)


