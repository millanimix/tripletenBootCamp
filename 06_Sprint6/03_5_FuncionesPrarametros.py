def omelet(eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

# print(omelet())

# añade un valor por defecto para eggs_number al parámetro
def omelet(eggs_number=2):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

print(omelet())

# añade un valor por defecto para eggs_number al parámetro
def omelet(cheese, eggs_number=2):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    return result

print(omelet(False))

#Ejemplo; Filtrar por genero, parametro genre con valor por defecto 'drama' y data sin valor por defecto
# esta función imprime las tablas filtradas. No modificar
def print_movie_info(data):
    for movie in data:
        print(movie)


# define tu función filter_by_genre() aquí
def filter_by_genre(data, genre='drama'):
    filtered_movies = []
    for movie in data:
        if genre in movie[3]:
            filtered_movies.append(movie)
    return filtered_movies

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# a continuación ejecutamos dos funciones para obtener resultados. No las modifiques
movies_filtered = filter_by_genre(movies_info)
print_movie_info(movies_filtered)