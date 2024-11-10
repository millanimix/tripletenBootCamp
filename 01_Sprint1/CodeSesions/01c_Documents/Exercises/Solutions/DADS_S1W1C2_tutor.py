# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sprint 1 - Week 1 - Class 2
# 
# Introducción a Python para Análisis de Datos Empresariales
# 
# # Contexto:
# 
# Trabajas en el departamento de análisis de datos de una empresa ficticia
# llamada DataCorp. Tu tarea es realizar algunas operaciones básicas con
# datos de la empresa utilizando Python.
# 
# # Módulo 1: Variables, Impresión, Tipos de Datos y Operaciones Aritméticas
# 
# ## Objetivos del Módulo:
# 
# -   Entender cómo definir y usar variables en Python en un contexto
#     empresarial.
# -   Utilizar el comando print para mostrar resultados relevantes.
# -   Realizar operaciones aritméticas con datos financieros.
# -   Comprender los diferentes tipos de datos utilizados en análisis de
#     datos empresariales y cómo convertirlos entre ellos.
# -   Identificar y resolver mensajes de error comunes.
# 
# ## Ejercicio 1 - Definición y Uso de Variables
# 
# -   Define una variable `nombre_empresa` y asígnale el valor “DataCorp”.
# -   Crea una variable `ingresos_anuales` y asígnale el valor de los
#     ingresos anuales de la empresa, por ejemplo, $1,500,000$ dólares.
# -   Define una variable `num_empleados` con el número de empleados en la
#     empresa, digamos $250$.
# -   Imprime una oración que combine estas variables para que diga algo
#     como:
#     `"La empresa {nombre_empresa} tiene un ingreso anual de {ingresos_anuales} dólares y emplea a {num_empleados} personas."`
#     Te puede servir algo llamado F-String. Si no lo conoces, búscalo en
#     internet.

# %%
nombre_empresa = "DataCorp"
ingresos_anuales = 1500000 # USD
num_empleados = 250
print(f"La empresa {nombre_empresa} tiene un ingreso anual de {ingresos_anuales*2} dólares y emplea a {num_empleados} personas.")

# %% [markdown]
# ## Ejercicio 2 - Operaciones Aritméticas Básicas
# 
# -   Define una variable `costos_operativos` con el valor de $800,000$
#     dólares.
# -   Calcula el beneficio bruto de la empresa restando los
#     `costos_operativos` de los `ingresos_anuales`.
# -   Calcula el beneficio por empleado dividiendo el beneficio bruto por
#     el número de empleados (`num_empleados`).
# -   Imprime los resultados, asegurándose de usar variables descriptivas
#     para cada valor y especificar qué valor correspónde a qué variable
#     en la impresión.

# %%
costos_operativos = 800000 # USD
beneficio_bruto = ingresos_anuales - costos_operativos 
beneficio_bruto_por_empleado = beneficio_bruto/num_empleados
print(f"""
Tenemos {ingresos_anuales} USD ingresos y {costos_operativos} USD costos.
El beneficio bruto es {beneficio_bruto}, que distribuido entre {num_empleados} empleados, nos da un beneficio bruto por empleado de {beneficio_bruto_por_empleado} USD
""")

# %% [markdown]
# ## Ejercicio 3 - Tipos de Datos y Conversión
# 
# -   Define una variable `tasa_crecimiento` y asígnale el valor $0.05$,
#     que representa un 5% de crecimiento anual.
# -   Convierte `tasa_crecimiento` a un porcentaje (multiplicando por 100)
#     y asígnalo a una nueva variable `tasa_crecimiento_pct`. Imprime
#     ambos valores.
# -   Define qué variable `es_rentable` y asígnale el valor `True` si el
#     beneficio bruto es mayor que 0, o False en caso contrario. Imprime
#     un mensaje que diga: “¿La empresa es rentable? {`es_rentable`}”
# -   Convierte num_empleados en una cadena y guardalo en una variable
# -   Imprime una oración que diga: “La empresa emplea a {`num_empleados`}
#     personas.”

# %%



tasa_crecimiento = 0.05
tasa_crecimiento_pct = tasa_crecimiento*100
es_rentable = beneficio_bruto > 0
num_empleados_str = str(num_empleados)
print("La empresa emplea a {num_empleados} personas.")

# %% [markdown]
# ## Ejercicio 4 - Identificación de Errores
# 
# -   Intenta ejecutar el siguiente código y corrige los errores:

# %%
print("La empresa " + nombre_empresa + " generó " + ingresos_anuales + " dólares en ingresos.")


# %%
print(f"La empresa {nombre_empresa} generó {ingresos_anuales} dólares en ingresos.")

# %% [markdown]
# # Módulo 2: Strings
# 
# ## Objetivos del Módulo:
# 
# -   Trabajar con strings en reportes y análisis empresariales.
# -   Acceder a caracteres específicos y subcadenas para manipular
#     información.
# -   Formatear strings para reportes claros y precisos.
# -   Utilizar métodos de strings para procesar datos textuales.
# 
# ## Ejercicio 1 - Propiedades Básicas de los Strings
# 
# -   Define una variable descripcion con el valor: “DataCorp es una
#     empresa líder en análisis de datos.”
# -   Imprime el número de caracteres en descripcion.
# -   Cambia el valor de descripcion a todas las mayúsculas usando un
#     método de string e imprímela.

# %%
descripcion = "DataCorp es una empresa líder en análisis de datos."
print(len(descripcion))
print(descripcion.upper())



# %% [markdown]
# ## Ejercicio 2 - Índices y Slices
# 
# -   Accede al primer carácter de descripcion e imprímelo.
# -   Accede a los primeros $15$ caracteres de descripcion usando slicing.
# -   Extrae la palabra “líder” de la descripción usando índices y
#     slicing, y asígnala a una nueva variable `calidad_empresa`.

# %%
descripcion[0]
descripcion[0:15]
calidad_empresa = descripcion[24:29]
calidad_empresa

# %% [markdown]
# ## Ejercicio 3 - Strings Formateados
# 
# -   Usa una f-string para crear un mensaje que diga: “DataCorp ha
#     crecido un {`tasa_crecimiento_pct`}% este año” (asegúrate de usar la
#     variable creada anteriormente).
# -   Repite el ejercicio usando el método format.

# %%
f"DataCorp ha crecido un {tasa_crecimiento_pct}% este año"
"DataCorp ha crecido un {}% este año".format(tasa_crecimiento_pct)

# %% [markdown]
# ## Ejercicio 4 - Métodos de String
# 
# -   Divide la descripción en palabras individuales y asígnalas a una
#     lista `palabras_descripcion`.
# -   Une las palabras de `palabras_descripcion` en una sola cadena,
#     separada por guiones (-).
# -   Reemplaza la palabra “líder” por “pionera” en descripcion.

# %%
palabras_descripcion = descripcion.split(sep=" ")
palabras_descripcion_unidas = "-".join(palabras_descripcion)
descripcion_modificada = descripcion.replace("líder", "pionera")

# %% [markdown]
# # Módulo 3: Listas
# 
# ## Objetivos del Módulo:
# 
# -   Comprender cómo crear y manipular listas de datos en Python,
#     específicamente listas de datos empresariales.
# -   Acceder y modificar elementos dentro de una lista utilizando índices
#     y slicing.
# 
# ## Ejercicio 1 - Propiedades Básicas de las Listas
# 
# -   Crea una lista `ingresos_mensuales` que contenga los ingresos de la
#     empresa para cada mes del año (puedes inventar 12 valores).
# -   Añade los ingresos de un 13er mes, que representa un ingreso
#     adicional de un proyecto especial, a la lista.
# -   Imprime la lista resultante.

# %%
ingresos_mensuales = [10000, 12000, 9500, 11000, 10500, 13000, 11500, 12500, 14000, 13500, 15000, 16000]

ingreso_especial = 18000
ingresos_mensuales.append(ingreso_especial)

print(ingresos_mensuales)

# %% [markdown]
# ## Ejercicio 2 - Índices y Slices
# 
# -   Accede al ingreso del tercer mes y asígnalo a una variable
#     `ingreso_marzo`.
# -   Modifica el ingreso del último mes en la lista para reflejar una
#     bonificación del 10% sobre el valor original.
# -   Usa slicing para crear una nueva lista `ingresos_primer_trimestre`
#     que contenga los ingresos de los primeros tres meses.

# %%
ingreso_marzo = ingresos_mensuales[2]

ingresos_mensuales[-1] = ingresos_mensuales[-1] * 1.10

ingresos_primer_trimestre = ingresos_mensuales[:3]


