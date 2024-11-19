# Lists

my_list = []

print(my_list)
print(type(my_list))
print(len(my_list))

favorite_files = ['The graduate', 'Reservoir Dogs', 'Fear and Loathing in Las Vegas']
print(favorite_files)
print(type(favorite_files))
print(len(favorite_files))

my_list = ['<3', 77, 3.89, True, False, ['sub', 'list', '0.2']]
print(my_list)
print(len(my_list))

# ! Warning Better comments extension

# Concatenar listas
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print()

# Indices y slices
movie_info = ['Fight Club', 1999, ['triller', 'drama', 'crime'], 139, 8.644]
print(movie_info[0])
print(type(movie_info[0]))

print(movie_info[1:4])
print(type(movie_info[1:4]))
print(len(movie_info[1:4]))

print(movie_info[2:100])
print(len(movie_info[2:100]))

print(movie_info[1:])
print(len(movie_info[1:]))

print(movie_info[:-3])

# Lists Modification
# Listas son mutables

shawshank_movie = ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
shawshank_movie.append('Frank Darabont')
print(shawshank_movie)

godfather_movie = ['The Godfather', 'USA', 1972]
# agregamos los nombres del director y compositor al final de la lista
godfather_movie.extend(['Francis Ford Coppola', 'Nino Rota'])
print(godfather_movie)

# Append agega sólo un elemento al final, el resultado es distinto a extend
row = [1, 2]
row.append([3, 4])
print(row)

dark_knight_movie = ['The Dark Night', 'USA', 'fantasy, action, thriller', 152]
dark_knight_movie.insert(2, 2008)
print(dark_knight_movie)

movies = ['Matrix', 'Matrix 2', 'Matrix 3']
movies.pop()
print(movies)

movies = ['Matrix', 'Matrix 2', 'Matrix 3']
movies.pop(1)
print(movies)

movies = ['Matrix', 'Matrix 2', 'Matrix 3']
popped_value = movies.pop(1)
print(popped_value)

my_list = [1, 2, 3, 3, 4]
my_list.remove(3) # Elimina la primera aparición de un valor específico
print(my_list)

# Ordering Lists
years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
print(years)

years.sort()
print(years)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years.sort(reverse=True)
print(years)

movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Schindler\'s List']
movies.sort()
print(movies)

movies = ['The Shawshank Redemption', 'The Godfather', 'the Dark Knight', 'Schindler\'s List']
movies.sort()
print(movies)

movies = ['The Shawshank Redemption', 'The Godfather', 'the Dark Knight', 'Schindler\'s List']
movies.sort(reverse=True)
print(movies)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years_sorted = sorted(years)
print(years_sorted)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years.sort()
print(years)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years_sorted = sorted(years, reverse=True)
print(years_sorted)

