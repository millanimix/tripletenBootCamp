order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

#EJEMPLO: Calcular el precio total del pedido

# variable del precio total del pedido
total_price = 0 

# iterar sobre cada diccionario de la lista
for item in order: 
# añadir a la variable el precio del elemento multiplicado por la cantidad
    total_price += item['price'] * item['quantity']

print(total_price)

#Ejemplo: Filtrar la categoria pizza

# variable para almacenar el resultado
filtered_order = [] 

for item in order: # iterar sobre cada diccionario de la lista
	if item['category'] == 'pizza': # si la categoría es pizza...
		filtered_order.append(item) # agregamos el diccionario a la lista filtered_order

# mostramos la lista filtrada de diccionarios
print(filtered_order)

#Ejercicio: Calcular el precio total para todas la pizzas
order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'comment': 'Add extra cheese please!',
        'price': 9 # precio por elemento
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'comment': '',
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'comment': '',
        'price': 2
    },
    {
        'item': 'Apple juice 0.5 l',
        'category': 'beverages',
        'quantity': 1,
        'comment': '',
        'price': 1
    },
    {
        'item': 'Croissant with cheese',
        'category': 'baked foods',
        'quantity': 2,
        'comment': '',
        'price': 1
    }
]

# empieza a escribir tu bucle for aquí
total_price = 0

for item in order:
	if item['category'] == 'pizza':
		total_price += item['price'] * item['quantity']
		
print(total_price)