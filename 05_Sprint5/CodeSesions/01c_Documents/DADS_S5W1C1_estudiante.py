# # Sprint 5 - Week 1 - Class 1
# 
# Distribuciones
# 
# # E1: Distribución normal y alturas en Chile
# 
# La altura promedio de la población adulta en Chile es aproximadamente de
# 170 cm para hombres, con una desviación estándar de 10 cm. Utilizando
# estos datos, realiza el siguiente ejercicio en Python.
# 
# -   Simula muestras de tamaños 10, 100, 500 y 1000 de alturas, asumiendo
#     una distribución normal con media de 170 y desviación estándar
#     de 10. Para cada muestra, genera un histograma y una curva de
#     densidad sobrepuesta para visualizar la distribución de las alturas.
#     Asegúrate de que cada gráfico esté etiquetado con el tamaño de la
#     muestra.
# 
# -   Calcula la probabilidad de que una persona tenga una altura menor a
#     150 cm (más baja que el promedio) y mayor a 180 cm (más alta que el
#     promedio). Recuerda usar la función de distribución acumulativa para
#     calcular estas probabilidades.
# 
# -   Interpreta los resultados de las probabilidades. ¿Qué tan común es
#     que una persona en Chile mida menos de 160 cm o más de 180 cm?


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm



# # E2: Distribución exponencial para la tasa de llegada de clientes en locales de retail
# 
# En una empresa de retail, queremos estudiar el tiempo entre la llegada
# de clientes a las cajas de pago en tres locales diferentes. Sabemos que:
# 
# -   En el Local A llega en promedio 1 cliente por minuto.
# 
# -   En el Local B llegan en promedio 3 clientes por minuto.
# 
# -   En el Local C llegan en promedio 6 clientes por minuto. Asumiendo
#     que la llegada de clientes sigue una distribución exponencial
#     (tiempo entre eventos), realiza los siguientes pasos:
# 
# -   Para cada local, simula la distribución de tiempos entre llegadas de
#     clientes usando una tasa media (λ) de 1, 3, y 6 clientes por minuto
#     respectivamente. Genera una muestra de 1000 tiempos entre llegadas
#     para cada local y grafica los histogramas correspondientes.
# 
# -   Traza los histogramas y las curvas de densidad exponenciales para
#     cada local en un mismo gráfico (3 gráficos en total), usando seaborn
#     o matplotlib.
# 
# -   Calcula la probabilidad de que lleguen al menos 100 clientes en:
# 
#     -   30 minutos
#     -   1 hora
#     -   1 hora y 30 minutos
# 
# Para ello, usa la propiedad de la distribución de Poisson para contar el
# número de eventos en un intervalo de tiempo dado (tasa λ x tiempo).


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon, poisson


# # E3: Conversión de Clientes en Retail
# 
# Como analistas en una tienda de retail, queremos entender la
# probabilidad de que los clientes realicen una compra al ingresar a la
# tienda. Sabemos que:
# 
# -   En el Local A, la probabilidad de que un cliente realice una compra
#     es del 20%.
# 
# -   En el Local B, la probabilidad de conversión es del 35%.
# 
# -   En el Local C, la probabilidad de conversión es del 50%.
# 
# -   Simula el número de clientes que realizan una compra en muestras de
#     20, 50 y 100 clientes, en cada local, basándote en la probabilidad
#     de conversión dada. Genera histogramas para visualizar el número de
#     compradores en cada muestra.
# 
# -   Calcula la probabilidad de que al menos 10 clientes realicen una
#     compra cuando ingresan 20, 50, y 100 clientes en cada local.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom


# # E4: Distribución uniforme de tiempos de espera
# 
# Imagina que eres analista de datos de una compañía ferroviaria y estás
# estudiando los tiempos de espera de los pasajeros en una estación de
# tren. Sabes que los trenes llegan cada 30 minutos, pero el horario es
# irregular, por lo que los pasajeros pueden esperar un tiempo entre 0 y
# 30 minutos en cualquier momento.
# 
# -   Genera una muestra de 1000 pasajeros, simulando el tiempo de espera
#     para cada uno, asumiendo que la espera sigue una distribución
#     uniforme entre 0 y 30 minutos. Grafica un histograma de los tiempos
#     de espera y traza la línea de la densidad teórica de la distribución
#     uniforme en el mismo gráfico.
# 
# -   Calcula la probabilidad de que un pasajero espere menos de 5 minutos
#     y la probabilidad de que un pasajero espere más de 20 minutos.
# 
# -   Calcula el tiempo de espera promedio y la desviación estándar de la
#     muestra generada.


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform


