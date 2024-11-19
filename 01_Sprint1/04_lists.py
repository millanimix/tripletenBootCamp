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

