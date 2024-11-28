# Expresiones lógicas y operadores de comparación 

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