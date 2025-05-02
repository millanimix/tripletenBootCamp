# Prueba de hipotesis
from scipy import stats as st
import numpy as np
import pandas as pd

# Tu socio comercial dice que el sitio web que creaste se ha convertido en un medio para
# atraer usuarios. Dicen que los usuarios pasan dos horas al día en el sitio web. En otras
# palabras, nuestra hipótesis nula es que los usuarios pasan 2 horas en el sitio web.
# Han tomado una muestra de 200 personas de los registros de tiempo pasado en el sitio
# web. Vamos a comprobar la hipótesis de tu compañero realizando una prueba y comparando
# el valor p resultante con el umbral que fijaremos en el 5%.

time_on_site = pd.read_csv('05_Sprint5/datasets/user_time.csv')
interested_value = 120 # tiempo transcurrido en el sitio web

alpha = .05 # la significancia estadística crítica (umbral)

# realizar una prueba
results = st.ttest_1samp(
    time_on_site, 
    interested_value)

# imprimir el valor p resultante
print('valor p: ', results.pvalue)

# comparar el valor p con el umbral
if (results.pvalue < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# El valor p resultante es 0.27702871, es decir, 27.7%. Esto representa la probabilidad
# de obtener un tiempo medio igual a 2 horas. Dado que esta probabilidad es bastante
# alta, parece que los usuarios pasan realmente unas dos horas en el sitio web. Utilizamos
# una prueba bilateral porque no nos importaba si el valor que obteníamos era superior o
# inferior al que proponía tu pareja (es decir, si era inferior o superior a 2 horas).

print('Exercise')
# Eres el dueño de una cadena de estaciones de alquiler de patinetes llamada Scooters
# Get You There. Hay 20 locales en el centro de la ciudad y cada uno tiene un máximo de
# 50 patinetes eléctricos. Quieres probar la hipótesis de que en el último mes hubo un
# promedio de 30 patinetes disponibles en cualquier estación durante el día. Un grupo
# urbano llamado 'Squirrel' destacó la importancia de este número en su estudio de la
# movilidad de los residentes. Si hay menos patinetes en la estación, los usuarios pensarán
# que no podrán alquilar uno cuando lo necesiten, pero cuando haya más, la gente pensará que
# no podrán aparcar su patinete después de un viaje porque no habrá aparcamiento.
# Cada hora, cada estación envía el número de patinetes disponibles al servidor. Has descargado
# los números de 13:00 a 16:00 durante los últimos 30 días. Prueba tu hipótesis usando esta
# muestra. Establece un umbral de 5% para la significación estadística.

scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])
optimal_value = 30 # escribe tu código aquí
alpha = 0.05 # establece la significación estadística crítica
results = st.ttest_1samp(
    scooters,
    optimal_value
) # realiza la prueba t
print('valor p: ', results.pvalue) # extrae el valor p de los resultados de la prueba)
if (results.pvalue < alpha): # compara el valor p con el umbral alpha
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")

# Claramente, no había un promedio de 30 patinetes por estación. Además, el número
# real difería de 30 en un grado estadísticamente significativo. La probabilidad de
# obtener esta diferencia aleatoriamente es menor que el nivel de significación que
# elegimos. Pero, ¿qué pasa si la investigación del grupo de urbanistas hubiera demostrado
# que no es tan importante tener más de una cierta cantidad de patinetes sino tener no menos
# de una cierta cantidad? En ese caso, solo habríamos prestado atención a un lado de la
# desigualdad y la hipótesis alternativa habría contenido el símbolo "<", no "≠".
# Veremos cómo probar hipótesis como esa en la próxima lección y ahora vamos a buscar el
# patinete disponible más cercano para dar un paseo.

print('\nHipotesis de una cola')
# Estás vendiendo sandías online. Para venderlas todas antes de que termine la temporada,
# contrataste a desarrolladores web para crear una página web llamada Watermelon Life.
# Observando las estadísticas, notaste que cuanto más tiempo las personas pasaban en tu
# sitio web (cuantos más bloques veían), más a menudo compraban sandías. El promedio de
# bloques vistos fue de 4.867.
# Los diseñadores insistieron en que cambies los primeros bloques para cumplir con las
# nuevas pautas, lo hiciste, pero la cantidad de pedidos no cambió. Pero probablemente los
# usuarios empezaron a realizar compras más rápidamente. Comprobemos si ese es el caso: si
# es así, los usuarios deberían decidir realizar compras después de ver solo los primeros
# bloques de la página web, por lo que la cantidad de bloques que ven debería ser menor ahora.
# Utilizaremos una muestra de 100 clientes seleccionados al azar. El dataset es el número de
# bloques de la página web vistos. Nuestra hipótesis nula es que el número de bloques de páginas
# de destino vistos es mayor o igual que 4.867.
screens = pd.Series([4, 2, 4, 5, 5, 4, 2, 3, 3, 5, 2, 5, 2, 2, 2, 3, 3, 4, 8, 3, 4, 3, 5, 5, 4, 2, 5, 2, 3, 7, 5, 5, 6,  5, 3, 4, 3, 6, 3, 4, 4, 3, 5, 4, 4, 8, 4, 7, 4, 5, 5, 3, 4, 6, 7, 2, 3, 6, 5, 6, 4, 4, 3, 4, 6, 4, 4, 6, 2, 6, 5, 3, 3, 3, 4, 5, 3, 5, 5, 4, 3, 3, 3, 1, 5, 4, 3, 4, 6, 3, 1, 3, 2, 7, 3, 6, 6, 6, 5, 5])

prev_screens_value = 4.867 # número promedio de bloques vistos

alpha = 0.05  # nivel de significación

results = st.ttest_1samp(screens, prev_screens_value)

# prueba unilateral: el valor p se divide en dos
print('valor-p: ', results.pvalue / 2)

# prueba unilateral a la izquierda:
# rechaza la hipótesis solo si la media muestral es significativamente menor que el valor propuesto
if (results.pvalue / 2 < alpha) and (screens.mean() < prev_screens_value):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# Como puedes ver en el código, en una prueba unilateral con la hipótesis alternativa
# "El número de bloques vistos disminuyó", la hipótesis nula se rechaza si se cumplen dos condiciones:
# — El valor observado es menor que el predicho.
# — La diferencia entre los valores es estadísticamente significativa (dividimos el valor p
# que obtuvimos de la prueba bilateral entre 2).

print('\nExercise')
# El 1 de junio de 2019 tomaste un curso del famoso coach y empresario llamado Robby Tobbinson.
# Si aplicas sus exclusivas técnicas conscientes de negocio se garantiza que tu proyecto online
# generará al menos $800 por día, quizás más, en solo un mes. Él te lo promete.
# Las promesas están bien pero las pruebas estadísticas son mejores. Vamos a ver qué nos dicen
# los números.
# Utiliza un dataset con los ingresos diarios del último mes para probar tu hipótesis. La
# hipótesis es que tus ingresos diarios promedio igualaron o superaron los $800.
# Recuerda: la hipótesis que contiene el signo de igualdad suele ser la hipótesis nula. Por lo
# tanto, "Todo saldrá como lo predijo el coach" es tu hipótesis nula y "Los ingresos serán menores
# de lo que se predijo" es la hipótesis alternativa. Las desviaciones aleatorias siempre son
# posibles. Solo puedes decir "¡La metodología de Tobbinson no funcionó!" si tus ingresos son 
# significativamente inferiores a la cantidad propuesta.

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 800 # ¿cuánto prometió Robby Tobbinson?

alpha = 0.05 # indica el nivel de significación estadística

results = st.ttest_1samp(revenue, interested_value) # utiliza la función st.ttest_1samp()

print('valor p:', results.pvalue / 2) # imprime el valor p para una prueba unilateral)

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value): # compara el valor obtenido y el nivel crítico de significación estadística
    # y verifica si la media muestral está en el lado correcto del interested_value):
    print(
        "Rechazamos la hipótesis nula: los ingresos fueron significativamente inferiores a 800 dólares"
    )
else:
    print(
        "No podemos rechazar la hipótesis nula: los ingresos no fueron significativamente inferiores"
    )

# El coaching está muy bien, pero necesitarás algo más que mindfulness para ganar $800 por día.

print('\nHipótesis sobre la igualdad de las medias de dos poblaciones')
# Veamos un ejemplo con dos datasets: la cantidad gastada en compras realizadas en un mes por
# visitantes provenientes de dos canales diferentes. Tienes una muestra aleatoria de 30 compras
# de cada canal.

sample_1 = [3071, 3636, 3454, 3151, 2185, 3259, 1727, 2263, 2015, 
            2582, 4815, 633, 3186, 887, 2028, 3589, 2564, 1422, 1785, 
            3180, 1770, 2716, 2546, 1848, 4644, 3134, 475, 2686, 
            1838, 3352]

sample_2 = [1211, 1228, 2157, 3699, 600, 1898, 1688, 1420, 5048, 3007, 
            509, 3777, 5583, 3949, 121, 1674, 4300, 1338, 3066, 
            3562, 1010, 2311, 462, 863, 2021, 528, 1849, 255, 
            1740, 2596]

alpha = 0.05  # el nivel de significancia estadística crítica
# si el valor p es menor que alpha, rechazamos la hipótesis

results = st.ttest_ind(sample_1, sample_2) # realizar una prueba

print('valor p: ', results.pvalue) # extraer el valor p

if results.pvalue < alpha: # comparar el valor p con el umbral
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# El valor p nos dice que aunque las cantidades promedio para los dos canales son diferentes,
# existe un 19.12% de probabilidad de obtener aleatoriamente una diferencia de ese tamaño o
# mayor. Esta probabilidad es claramente demasiado alta para concluir que existe una diferencia
# significativa entre los importes promedio gastados.

print('\nExercise 1')
# Hay dos conjuntos de datos: el tiempo promedio que pasan en un sitio web 1) los usuarios que
# inician sesión con nombre de usuario y contraseña, y 2) los usuarios que inician sesión a través
# de las redes sociales. Prueba la hipótesis de que ambos grupos de usuarios pasan la misma cantidad
# de tiempo en el sitio web.
