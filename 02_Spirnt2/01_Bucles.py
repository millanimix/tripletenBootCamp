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

# Listas anidadas / Nested lists

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

for row in movies_info:
    print(row)

for row in movies_info:
    print(row[0])


# Lista anidada de pedidos: [precio, cantidad, descuento]
orders = [
    [199.99, 2, 0.10],  # 10% de descuento
    [349.99, 1, 0.05],  # 5% de descuento
    [129.99, 3, 0.00],  # Sin descuento
    [499.99, 1, 0.20],  # 20% de descuento
    [249.99, 4, 0.15],  # 15% de descuento
]
# Inicializa las variables
total_revenue = 0
highest_order_value = 0
order_revenue = []

# Recorre los pedidos
for order in orders:
    total_revenue += (order[0] - order[0]*order[2]) * order[1]
    order_revenue.append((order[0] - order[0]*order[2]) * order[1])

### AQUÍ VA TU CÓDIGO ###
highest_order_value = max(order_revenue)
print("Ingresos totales después de descuentos y tasas:", total_revenue) # Salida: Ingresos totales después de descuentos y tasas: 2332.4005
print("Valor de pedido único más alto:", highest_order_value)  # Salida: Valor de pedido único más alto: 849.966
