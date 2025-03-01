# # Sprint 5 - Week 2 - Class 1
# 
# Test de Hipótesis
# 
# # Introducción
# 
# En este set de ejercicios, investigaremos el impacto de un programa de
# tutorías en el rendimiento académico de los estudiantes. Generaremos
# datos de rendimiento antes y después de un programa y aplicaremos
# pruebas de hipótesis para responder preguntas clave.
# 
# # E1: Igualdad de medias de dos poblaciones (Prueba independiente)
# 
# Genera dos conjuntos de datos que representen los puntajes de los
# estudiantes de dos grupos diferentes (control y tratamiento) y realiza
# una prueba de hipótesis para determinar si sus medias son iguales.
# Recuerda que con `np.random` puedes generar varios tipos de
# distribuciones


#


import numpy as np
from scipy import stats

# Generar datos simulados
np.random.seed(42)
grupo_control = np.random.normal(loc=70, scale=10, size=100)  # Promedio 70, desviación estándar 10
grupo_tratamiento = np.random.normal(loc=75, scale=10, size=100)  # Promedio 75, desviación estándar 10

# Prueba t de dos muestras independientes
t_stat, p_value = stats.ttest_ind(grupo_control, grupo_tratamiento)

print("Estadístico t:", t_stat)
print("Valor p:", p_value)


# ## Pregunta
# 
# -   ¿Puedes rechazar la hipótesis nula de que las medias de ambos grupos
#     son iguales al nivel de significancia del 5%?


# Respuesta: La prueba ttest_ind evalúa si las medias de dos grupos independientes son significativamente diferentes. En este ejercicio, el valor p obtenido debe compararse con el nivel de significancia (0.05).

# Estadístico t: Puede variar en función de los datos generados. Supongamos que el resultado es alrededor de 2.5.
# Valor p: Si el valor p es menor que 0.05 (por ejemplo, 0.013), se puede rechazar la hipótesis nula de que las medias de ambos grupos son iguales.
# Conclusión: Si el valor p < 0.05, hay evidencia suficiente para afirmar que hay una diferencia significativa entre los grupos de control y tratamiento.


# # E2: Igualdad de medias de dos poblaciones relacionadas (Prueba dependiente)
# 
# Genera un conjunto de datos que represente los puntajes de los
# estudiantes antes y después del programa de tutorías y realiza una
# prueba de hipótesis para evaluar si hubo un cambio significativo.


#


# Generar datos simulados
rendimiento_antes = np.random.normal(loc=70, scale=8, size=100)  # Promedio 70
rendimiento_despues = rendimiento_antes + np.random.normal(loc=5, scale=5, size=100)  # Incremento promedio de 5 puntos

# Prueba t de muestras relacionadas
t_stat_rel, p_value_rel = stats.ttest_rel(rendimiento_antes, rendimiento_despues)

print("Estadístico t (relacionada):", t_stat_rel)
print("Valor p (relacionada):", p_value_rel)


# ## Pregunta
# 
# -   ¿Puedes afirmar que el programa de tutorías tuvo un impacto
#     significativo en el rendimiento de los estudiantes?


# Respuesta: La prueba ttest_rel evalúa si las medias de dos muestras emparejadas (antes y después) son diferentes.

# Estadístico t (relacionada): Por ejemplo, un resultado de 4.2.
# Valor p (relacionada): Si el valor p es menor que 0.05 (por ejemplo, 0.00005), se rechaza la hipótesis nula.
# Conclusión: Si el valor p < 0.05, se puede afirmar que hubo un cambio significativo en el rendimiento después del programa de tutorías.


# # E3: Test de hipótesis de una cola
# 
# Repite el ejercicio 2, pero realiza un test de una cola para verificar
# si el rendimiento después del programa es mayor que antes.


#


# Prueba de una cola (rendimiento después > antes)
t_stat_one_tail, p_value_one_tail = stats.ttest_rel(rendimiento_antes, rendimiento_despues)
p_value_one_tail /= 2  # Dividir el valor p para obtener la prueba de una cola
bool_hay_credimiento = rendimiento_despues.mean() > rendimiento_antes.mean()

print("Estadístico t (una cola):", t_stat_one_tail)
print("Valor p (una cola):", p_value_one_tail)
if bool_hay_credimiento:
  print(f"Hay crecimiento (no necesariamente significativo)")
else:
  print(f"No hay crecimiento (no necesariamente significativo)")


# ## Pregunta
# 
# -   ¿Puedes rechazar la hipótesis nula de que el rendimiento después del
#     programa no es significativamente mayor que el antes al 5% de
#     significancia?


# Respuesta: Este ejercicio usa el resultado del ejercicio 2, pero con una prueba de una cola.

# Estadístico t (una cola): Por ejemplo, un resultado de 4.2.
# Valor p (una cola): Dividido entre 2, si el valor p es 0.000025 (dividiendo 0.00005 entre 2), entonces es menor que 0.05.
# Conclusión: Si el valor p/2 < 0.05, se rechaza la hipótesis nula y se acepta que el rendimiento después del programa es significativamente mayor que antes.


# # E4: Test de hipótesis de dos colas aplicado a ingresos por departamento
# 
# Supongamos que estamos analizando los ingresos generados por dos
# departamentos de una empresa y queremos determinar si existe una
# diferencia significativa en los ingresos medios entre ellos. Considera
# un riesgo de equivocarte al encontrar una diferencia de 0.1%


import numpy as np
from scipy import stats

# Generamos datos simulados de ingresos para dos departamentos
np.random.seed(42)
ingresos_depto_A = np.random.normal(loc=50000, scale=5000, size=100)  # Media de 50,000 con desviación de 5,000
ingresos_depto_B = np.random.normal(loc=51000, scale=4800, size=100)  # Media de 51,000 con desviación de 4,800


# Realizamos un test de hipótesis de dos colas
t_stat, p_val = stats.ttest_ind(ingresos_depto_A, ingresos_depto_B)

print("Estadístico t:", t_stat)
print("Valor p:", p_val)

# Interpretación del resultado
alpha = 0.001  # Nivel de significancia
if p_val < alpha:
    print("Rechazamos la hipótesis nula. Existe evidencia para afirmar que las medias son diferentes.")
else:
    print("No podemos rechazar la hipótesis nula. No hay evidencia suficiente para afirmar que las medias son diferentes.")


# ## Pregunta
# 
# -   ¿Existe evidencia estadística para afirmar que los ingresos medios
#     entre los departamentos A y B son diferentes?


# - Estadístico t: Este valor indica la magnitud y dirección de la diferencia entre las medias.
# - Valor p: Si es menor que 0.05, rechazamos la hipótesis nula y concluimos que hay diferencias significativas entre los ingresos medios de los dos departamentos.

# Nota: La respuesta exacta puede variar debido a la generación aleatoria de datos.


