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

