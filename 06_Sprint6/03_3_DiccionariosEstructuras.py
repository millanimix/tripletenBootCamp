bus_schedule = {
    '72': ['8:00', '12:00', '17:30'],
    '26': ['9:30', '15:00'],
    '17': ['7:30', '12:30', '15:30']
}

# iteramos sobre las claves y los valores del diccionario
for route, times in bus_schedule.items():
    # iteramos sobre los valores de la lista
    for time in times:
        # mostramos la ruta y su horario correspondiente
	      print(f"Ruta {route} - Hora {time}")

bus_schedule = {
    '72': ['8:00', '12:00', '17:30'],
    '26': ['9:30', '15:00'],
    '17': ['7:30', '12:30', '15:30']
}

for route, times in bus_schedule.items():
    earliest_time = times[0]
    print(f'La primera hora para el autobús #{route} es {earliest_time}')

# Lista de diccionarios
movies_table = [
    {'movie_name':'The Shawshank Redemption', 'country':'USA', 'genre':'drama', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'The Godfather', 'country':'USA', 'genre':'drama, crime', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'The Dark Knight', 'country':'USA', 'genre':'fantasy, action, thriller', 'year':2008, 'duration':152, 'rating':8.499}
]

# ahora accedemos a la columna por su nombre:
print(movies_table[2]['movie_name'])

