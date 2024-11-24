# Bucles

fr_speakers = 284.9
fr_speakers = 284.9 + 2.5
print(fr_speakers)

fr_speakers = 284.9
fr_speakers = fr_speakers + 2.5
print(fr_speakers)

# Asignación auentada / Augmented Assigment
fr_speakers = 284.9
fr_speakers += 2.5
print(fr_speakers)

items = 10

items += 5 # igual que items = items + 5
print(items)

items -= 5 # igual que items = items - 5
print(items)

items *= 5 # igual que items = items * 5
print(items)

items /= 5 # igual que items = items / 5
print(items)

# Funciones integradas / Built-in Functions
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 126]

total_duration = sum(movies_duration) # suma todos los elementos de la lista
max_duration = max(movies_duration)
min_duration = min(movies_duration)

print(total_duration)
print(max_duration)
print(min_duration)

# Bucle for / for loops
film_genres = ['scifi', 'drama', 'thriller', 'comedy', 'action']

print(film_genres[0])
print(film_genres[1])
print(film_genres[2])
print(film_genres[3])
print(film_genres[4])

film_genres = ['scifi', 'drama', 'thriller', 'comedy', 'action']
for value in film_genres:
    print(value)

film = ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
for value in film:
    print(value)

review = 'The Emoji Movie dejó mucho que desear. Dos estrellas demasiado generosas.'
for symbol in review:
    print(symbol)