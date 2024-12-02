# Expresiones lógicas y operadores de comparación 
# Logical statements
# Logical operators: and, or, not

shawshank_release_year = 1994
titanic_release_year = 1997

print(shawshank_release_year > titanic_release_year)

movie_info = ['Fight Club', 'USA', 1999, 'thirller, drama, crime', 139, 8.644]
print(movie_info[2] > 1996 and movie_info[2] < 1998)
print(movie_info[2] > 1996 or movie_info[2] < 1998)

print(not(movie_info[2] > 1996 and movie_info[2] < 1998))

print('Funciones de predicado')
print('hola'.islower())
print('777'.isdigit())
print('la cadena contiene espacios, así como signos de puntiación'.isalpha())

# if-else statements
print()
print('if-else statements')
print()
weather = 'lluvia'

if weather == 'lluvia':
    print('llevar paraguas')

print('¡vamos!')

weather = 'sol'

if weather == 'lluvia':
    print('llevar paraguas')
else:
    print('llevar un sombrero')

print('¡vamos!')

# comprobación de substring

if 'estoy' in 'en equipo':
    print('Aquí estoy yo en el equipo')
else:
    print('En verdad, no hay yo en el equipo')

quote = 'El progreso es imposible sin cambio y aquellos que no pueden cambiar de opinión no pueden cambiar nada.'
if 'ogres' in quote:
    print('Donde hay progreso, ¡hay queso!')
else:
    print('¡Aquí no, pequeño bromista!')

# else and elif

weather = 'lluvia'

if weather == 'lluvia':
    item_to_take = 'paraguas'
if weather == 'sol':
    item_to_take = 'sombrero'
if weather == 'nieve':
    item_to_take = 'gorro y bufanda'
else:
    item_to_take = 'nada'

print(weather)
print(item_to_take)

weather = 'lluvia'

if weather == 'lluvia':
    item_to_take = 'paraguas'
elif weather == 'sol':
    item_to_take = 'sombrero'
elif weather == 'nieve':
    item_to_take = 'gorro y bufanda'
else:
    item_to_take = 'nada'

print(weather)
print(item_to_take)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
for year in years:
    if 1960 <= year <= 1969:
        print('La pelicula se estrenó en la decada de 1960.')
    elif 1970 <= year <= 1979:
        print('La pelicula se estrenó en la decada de 1970.')
    elif 1980 <= year <= 1989:
        print('La pelicula se estrenó en la decada de 1980.')
    elif 1990 <= year <= 1999:
        print('La pelicula se estrenó en la decada de 1990.')
    elif 2000 <= year <= 2009:
        print('La pelicula se estrenó en la decada de 2000.')
    else:
        print('Tiempo no definido')

# Modificación de tablas
# Modifying tables

print()
print('Modifying tables')
print()

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1994, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_name = 'Schindler\'s List'
correct_year = 1993

for movie in movies:
    if movie[0] == movie_name:
        movie[1] = correct_year

for movie in movies:
    print(movie)

