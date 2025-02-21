import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Parámetros de la distribución normal
media = 170  # media en cm
desviacion_estandar = 10  # desviación estándar en cm

# Tamaños de muestra
tamanos_muestra = [10, 100, 500, 1000]

# Gráfico para cada tamaño de muestra
plt.figure(figsize=(14, 10))
for i, n in enumerate(tamanos_muestra, 1):
    # Generar la muestra
    
    muestra = np.random.normal(media, desviacion_estandar, n)
    
    # Crear el histograma y la curva de densidad
    plt.subplot(2, 2, i)
    sns.histplot(muestra, bins=15, kde=True, color='green', stat='density')
    x = np.linspace(media - 4*desviacion_estandar, media + 4*desviacion_estandar, 1000)
    plt.plot(x, norm.pdf(x, media, desviacion_estandar), color='darkblue', linestyle='--', label="Densidad teórica")
    plt.title(f'Tamaño de muestra: {n}')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Densidad')
    plt.legend()

plt.tight_layout()
plt.show()

# Cálculo de probabilidades
altura_baja = 150
altura_alta = 180

prob_menor_160 = norm.cdf(altura_baja, media, desviacion_estandar)
prob_mayor_180 = 1 - norm.cdf(altura_alta, media, desviacion_estandar)

print(f"Probabilidad de que una persona mida menos de {altura_baja} cm: {prob_menor_160:.4f}")
print(f"Probabilidad de que una persona mida más de {altura_alta} cm: {prob_mayor_180:.4f}")