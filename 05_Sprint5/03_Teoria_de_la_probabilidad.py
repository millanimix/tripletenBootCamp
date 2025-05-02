import pandas as pd
from math import factorial
import numpy as np
from scipy import stats as st
import math as mt

cool_rock = pd.DataFrame(
    {
        'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
        ],
        'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
        ],
    }
)
print(cool_rock)

# Probability of Smells Like Teen Spirit being fisrt in the list
print('\n The probability of Smells Like Teen Spirit being first in the list is: ')
print(
    len(cool_rock[cool_rock['Song'] == 'Smells Like Teen Spirit']) / len(cool_rock)
)

# Probability of Queen being the artist of the song
desired_artist = 'Queen'
desired_outcomes = len(cool_rock[cool_rock['Artist'] == desired_artist])
total_outcomes = len(cool_rock)
probability = desired_outcomes / total_outcomes
print(f'The probability of Queen being the artist of the song is: {probability:}')

# Permutaciones
# define el número necesario de cursos
courses_amount = 3
# calcula el factorial de 3 (el valor de la variable courses_amount)
result = factorial(courses_amount)
# muestra el resultado
print('Permutations of 3!:')
print(result)

print('Example list of candidates')
candidates_amount = 5
lists_amount = factorial(candidates_amount)
print(lists_amount)

# Factorial
# define los valores para las variables n y k
n = 10
k = 3
# realiza los cálculos
combinations = factorial(n) / (factorial(k) * factorial(n-k))
print('Total de combinaciones de helados:')
print(combinations)

# Excesice
n = 5 # define aquí el número de candidatos
k = 3 # define aquí el número necesario de compañeros de equipo
combinations = factorial(n) / (factorial(k) * factorial(n-k))
print('Total de combinaciones de equipos:')
print(combinations)

# Excesice 1
tasks = 10
permutations = factorial(tasks)
probability = 1 / permutations
print('The probability is:')
print(probability)

# Excesice 2
tasks = 10
chosen = 3
combinations = factorial(tasks) / (factorial(chosen) * factorial(tasks-chosen))
probability = 1 / combinations
print('The probability is:')
print(probability)

# Distributions with Python
data = np.array([1, 3, 5, 7, 11, 13, 17, 19, 23, 317])
print('El primer elemento:', data[0])
print('El último elemento:', data[-1])
print('Todos los elementos excepto el primero y el último:', data[1:-1])

# Create a random normal distribution
print('\nNormal distribution')
data = np.random.normal(size = 20)
print(data)

# Create a random array with mean and standard deviation
print('\nNormal distribution with mean an standard deviation')
mean = 15
std_dev = 5
data = np.random.normal(mean, std_dev, size=20)
print(data)
# declara una variable para almacenar el número de visitantes.
# como aún no hemos empezado a contar,
# el número de visitantes con una bolsa pesada es cero.
visitors_number = 0
# crea un bucle para iterar consecutivamente sobre el peso de cada bolsa.
for weight in data:

    # si el peso de la bolsa actual es mayor que la media, aumenta el contador.
    if weight > mean:
        visitors_number += 1

# muestra el número de visitantes con bolsas pesadas.
print('Número de visitantes con bolsas pesadas:', visitors_number)

print('\nExercises')
exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)
failed_students = 0
for result in exam_results:
    if result < 20:
        failed_students += 1

print('Número de estudiantes reprobados:', failed_students)

print('\nExercise 2')

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)

summarized_data = {'excellent': 0, # añade el valor inicial aquí,
                   'good': 0, # añade el valor inicial aquí,
                   'average': 0, # añade el valor inicial aquí,
                   'passable': 0, # añade el valor inicial aquí,
                   'failed': 0} # añade el valor inicial aquí

# escribe aquí el código para contar el número de estudiantes para cada tipo de resultados obtenidos.
for result in exam_results:
    if result >= 90:
        summarized_data['excellent'] += 1
    elif result >= 70:
        summarized_data['good'] += 1
    elif result >= 50:
        summarized_data['average'] += 1
    elif result >= 20:
        summarized_data['passable'] += 1
    else:
        summarized_data['failed'] += 1

# código para mostrar los resultados en pantalla. No lo cambies.
for result in summarized_data:
    print(result, '-', summarized_data[result])

# Binomial distribution
print('\nCompute k success for n trials')
c = factorial(10)/(factorial(7)*factorial(3))
print(c)

print('\nCompute k = 90 success for n = 100 trials')
c = factorial(100)/(factorial(90)*factorial(10)) 
print(c)

# Exercise
# Los portátiles de Pineapple son caros, pero siguen siendo populares entre los geeks de la informática: 
# el 60% de los clientes están dispuestos a comprarse una computadora portátil de esta marca si acuden a la tienda.
# Los portátiles de Banana son más baratos, pero no tan populares: solo el 20% de los visitantes de la tienda están
# dispuestos a comprarlos.
# Supongamos que la tienda solo tiene a la venta equipos de Pineapple.
# ¿Cuál es la probabilidad de que 50 de cada 80 clientes realicen una compra en un día?

print('\nBinomial distribution')
p = 0.6
q = 0.4
n = 80
k = 50
probability = factorial(n)/(factorial(k)*factorial(n-k)) * (p**k) * (q**(n-k))
print(probability)

# Exercise 2
# Supongamos que, al lado de una tienda de hardware Pineapple, hay un gran centro comercial con otra tienda que
# vende computadoras Banana. 160 clientes visitan esa tienda durante el día.
# ¿Cuál es la probabilidad de que 50 de esos visitantes se compren una computadora portátil?
# Recuerda que solo el 20% de los usuarios están dispuestos a comprar un portátil de la marca Banana.
p = 0.2 # la probabilidad de que un cliente realice una compra
q = 0.8 # la probabilidad de que un cliente NO realice una compra
n = 160 # el número total de visitantes
k = 50 # el número de visitantes que esperamos que realicen una compra
probability = factorial(n) / (factorial(k) * factorial(n-k)) * (p ** k) * (q ** (n-k))
print(probability)

# Normal Distribution
print('Normal distribution')
# creamos un objeto con datos distribuidos normalmente con una media de 5 000
# y una desviación estándar de 1500.
data = st.norm(5000, 1500)
# creamos una variable para almacenar el coste deseado.
desired_cost = 4000
# calculamos la probabilidad de obtener el valor desired_cost.
probability = data.cdf(desired_cost)
print('\n¿Cuál es la probabilidad de que un estudiante pueda aprender una nueva profesión por menos de 4 000 dólares?')
print(probability)
# establecemos el valor de la probabilidad. Buscaremos el umbral del coste de los estudios 
# para el 10% de los estudiantes que gastaron menos dinero.
target_level = 0.1
# encontramos el importe que no supere los gastos del 10% de estudiantes que gastaron menos dinero.
cost = data.ppf(target_level)
print('\n¿Cuál es el coste máximo de la formación para el 10% de los estudiantes que gastaron menos dinero en sus estudios?')
print(cost)
print('\nLa puntuación media en el examen del Certificado de análisis de datos es 1000 y la desviación estándar es 100. Hay que encontrar la probabilidad de obtener entre 900 y 1 100 puntos en el examen.')
print(st.norm(1000, 100).cdf(1100) - st.norm(1000, 100).cdf(900))

# Exercises
print('\n Exercise 1')
# El número de visitantes mensuales de una tienda virtual tiene una distribución normal
# con una media de 100500 y una desviación estándar de 3500.
# Encuentra la probabilidad de que en el próximo mes el sitio web del outlet tenga:
# menos de 92000 visitantes;
# más de 111000 visitantes.

mu = 100500 # ¿cuál es la media de la distribución?
sigma = 3500  # ¿cuál es la desviación estándar de la distribución?
more_threshold = 111000 # ¿Cuál es el límite superior del número de visitantes?
fewer_threshold = 92000 # ¿Cuál es el límite inferior del número de visitantes?
p_more_visitors = 1 - st.norm(mu, sigma).cdf(more_threshold) # calcula la probabilidad de que el número de visitantes sea superior al umbral superior
p_fewer_visitors = st.norm(mu, sigma).cdf(fewer_threshold) # calcula la probabilidad de que el número de visitantes sea inferior al umbral inferior
print(f'Probabilidad de que el número de visitantes sea superior a {more_threshold}: {p_more_visitors}')
print(f'Probabilidad de que el número de visitantes sea inferior a {fewer_threshold}: {p_fewer_visitors}')

print('\n Exercise 2')
# Otra tienda online, Fancy Pants, vende productos de regalo a un público muy limitado de clientes corporativos.
# Las ventas semanales en la tienda de conjuntos de ajedrez de lujo fabricados con colmillo de mamut tienen una
# distribución normal con una media de 420 y una desviación estándar de 65.
# El equipo de inventario está decidiendo cuántos conjuntos pedir. Quieren que la posibilidad de venderlos todos
# la próxima semana sea del 90%. ¿Cuántos deben pedir?
mu = 420 # escribe tu código aquí: ¿cuál es la media?
sigma = 65 # escribe tu código aquí: ¿cuál es la desviación estándar?
prob = 0.90 # escribe tu código aquí: ¿cuál es la probabilidad requerida de vender todos los artículos?
n_shipment = st.norm(mu, sigma).ppf(1 - prob) # escribe tu código aquí: ¿cuántos artículos se deben pedir?
print('Cantidad de artículos a pedir:', int(n_shipment))

print('\n Exercise 3')
# Los precios de los pedidos realizados en una tienda virtual tienen una distribución normal con una media
# de 24 dólares y una desviación estándar de 3.20 dólares.
# Algunos clientes eligen la entrega rápida por mensajería, que tiene un precio fijo independientemente del
# valor del pedido.
# Los clientes tienden a molestarse cuando el costo de la entrega es igual al costo del pedido. ¿Cuánto debería
# costar el envío por mensajería para que no supere el precio del pedido en el 75% de los casos?
mu = 24 # coloca tu código aquí: ¿cuál es la media de la distribución?
sigma = 3.20 # coloca tu código aquí: ¿cuál es la desviación estándar de la distribución?
threshold = 0.75 # coloca tu código aquí: ¿qué porcentaje de pedidos debería costar más del doble del costo de envío?
max_delivery_price = st.norm(mu, sigma).ppf(1 - threshold) # coloca tu código aquí: el costo máximo de envío
print('Costo máximo de envío por mensajería:', max_delivery_price)

print('\nAproximación normal a distribución binomial')
# Una empresa ha decidido anunciarse online. El servicio de publicidad dice que, de promedio, el 15% de los usuarios
# hacen clic en sus anuncios. Eso es 750 visitas por cada 5000 vistas.
# La empresa coloca anuncios, compra 5000 impresiones (vistas) y solo obtiene 715 visitas. ¡El equipo de marketing
# está disgustado! ¿No les habían prometido 750 visitas? Usaremos argumentos estadísticos para calmarlos.
# En resumen: cuando un usuario ve el anuncio, hay un 15% de posibilidades de que haga clic en él. Esto nos da una
# distribución binomial con n = 5000 y p = 0.15.
# Utilizaremos la distribución normal para aproximar la distribución binomial y calcular la probabilidad de obtener
# 715 clics o menos.
# establecemos los valores de los parámetros
binom_n = 5000
binom_p = 0.15
clicks = 715
# calculamos el valor esperado de éxitos y sigma
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))
# calculamos la probabilidad de obtener 715 visitas o menos
p_clicks = st.norm(mu, sigma).cdf(clicks)
print(p_clicks)

print('\nExcerice 1')
# Una empresa envía a sus clientes un boletín electrónico mensual con novedades y ofertas de los socios. Sabemos que
# el 40% de los clientes abre el boletín.
# Uno de los socios está planeando una campaña publicitaria y espera llegar a unos 9000 clientes. Calcula la
# probabilidad de que se cumplan las expectativas del socio si el boletín se envía a 23 000 personas.
# En el ejemplo anterior, hemos creado una variable llamada clicks. Aquí, crea otra llamada threshold y guarda el
# valor 9000 en ella. Que el tamaño de la población sea binom_n y que la probabilidad de que se abra el boletín sea
# binom_p.
# Guarda la probabilidad de que se cumplan las expectativas del socio como p_threshold y muéstrala.
threshold = 9000
binom_n = 23000
binom_p = 0.40
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))
p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(p_threshold)

print('\nTest')
threshold = 500
binom_n = 5000
binom_p = 0.11
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))
p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(p_threshold)