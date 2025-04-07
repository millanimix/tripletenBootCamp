# Estadistica_descriptiva
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Histogramas de frecuencia
# data = pd.Series([11, 20, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99])
# data.hist(bins=4, alpha=0.5)

# data.hist(
#     bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99], alpha=0.7
# )
# plt.show()

# Ejercicio
# el dataset pur_time (del inglés purchase_time que significa tiempo de compra)
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])
# pur_time.hist(
#     bins=[15, 30, 45, 60, 75, 90],
#     alpha=0.7
# )

pur_time.hist(
    bins=[15, 35, 55, 75, 90],
    alpha=0.5
)
pur_time.hist(
    bins=[15, 45, 55, 90],
    alpha=0.5
)

plt.show()

# Measure of Position and Variability
data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(' La media es igual a', data.mean())
print(' La mediana es igual a', data.median())

# New values influenenced on the mean and median
data_new = pd.Series([0, 0.1, 0.2, 0.3, 0.4, 5, 60, 70, 80, 90, 100])
print('La media es igual a', data_new.mean())
print('La mediana es igual a', data_new.median())

# Variability measures
# Boxplot wyth Python
dataset = pd.Series([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6])
sns.boxplot(dataset)
# plt.show()

# Exercise 1: ¿cómo medimos la dispersión alrededor de la medida algebraica de posición, es decir, alrededor de la media?
print('Exercise 1')
data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# escribe tu código aquí: busca el valor medio en el dataset
mean_value = data.mean()
print(mean_value)
# escribe tu código aquí: para cada elemento del dataset, encuentra su distancia a la media
spacing_all = data - mean_value
print(spacing_all)
# escribe tu código aquí: calcula la distancia media
spacing_all_mean = spacing_all.mean()
print(spacing_all_mean)

# Variance
print('\nVariance')
x = [1, 2, 3, 4, 5, 6]
variance = np.var(x)
print(variance)

print('Covariance')
x = [1, 2, 3, 4, 5, 6]
y = [41, 62, 89, 96, 108, 115]
# Matriz de covarianza
covariance_matrix = np.cov(x, y)
print(covariance_matrix)
# Extraer la covarianza como valor
covariance = covariance_matrix[0][1] # La diagonal principal es la varianza de cada variable
print(covariance)

# Exercise 1: Variance
data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
variance = np.var(data)
print(variance)

# Standard Deviation
print('\nStandard Deviation')
s = pd.Series([1, 2, 3, 4, 5, 6])
print(s.describe())

x = [1, 2, 3, 4, 5, 6]
standard_deviation = np.std(x)
print(standard_deviation)
# Compute standard deviation from variance
variance = 3.5
standard_deviation = np.sqrt(variance)
print(standard_deviation)

# Normal Distribution
print('\nNormal Distribution')

# Exercises 1: Standard Deviation
data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
standard_dev = np.std(data)
print(standard_dev)

# Exercises 2: Variance: Standard Deviation
adv_mean = 3
adv_var = 0.25
# calcula la desviación estándar
adv_std = np.sqrt(adv_var)

# calcula el tiempo de visualización del mensaje
adv_time = adv_mean + 3*adv_std
print(f'El tiempo de visualización del mensaje es {adv_time}')
print('El tiempo de visualización del mensaje es', adv_time)

# Exercise 3: Trivia contest
# calcula el número promedio de personas que responden correctamente
# 3% of 6000 participants answer correctly
quiz_mean = 0.03 * 6000
print(f'quiz_mean: {quiz_mean}')
# calcula la desviación estándar (0.4%) del número total de participantes 
quiz_std = 0.004 * 6000
print(f'quiz_std: {quiz_std}')

# calcula el límite inferior del intervalo
quiz_bottom_line = quiz_mean - 3*quiz_std
# calcula el límite superior del intervalo
quiz_top_line = quiz_mean + 3*quiz_std

print(f'Intervalo: {quiz_bottom_line} - {quiz_top_line}')

# Outliers: Válores atípicos
print('Outliers')
q1 = 25
q3 = 41
iqr = q3 - q1
print(f'IQR = {iqr}')

# calcula el límite inferior del intervalo de confianza para los outliers
outlier_bottom_line = q1 - 1.5 * iqr
# calcula el límite superior del intervalo de confianza para los outliers
outlier_top_line = q3 + 1.5 * iqr
print(f'Intervalo: {outlier_bottom_line} - {outlier_top_line}')