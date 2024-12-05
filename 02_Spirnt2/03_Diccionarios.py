# Dictionaries

schedule = {
    'SU2222': '12.06.18 12:30',
    'SU1111': '12.06.18 14:05',
    'SU0777': '12.06.18 17:00'
}

print(schedule) 
print(len(schedule))

print()
print('Extraer valores de diccionarios')
print()

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan': 96.27,
    'Walmart': 130.68
}

coca_cola_price = financial_info['Coca-Cola']
print(coca_cola_price)

pepsi_price = financial_info.get('Pepsi')
nike_price = financial_info.get('Nike')
print(pepsi_price)
print(nike_price)
print()

pepsi_price = financial_info.get('Pepsi', -1)
nike_price = financial_info.get('Nike', -1)
print(pepsi_price)
print(nike_price)

# Diccionario anidado que representa productos
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Inicializa las variables
total_incomes = 0
more_expensive_value = 0
    
# Calcula los ingresos totales y encuentra el producto más caro
for product in products:
    product_price = products[product]['price']
    total_incomes += products[product]['price'] * products[product]['quantity'] * (1 - products[product]['discount'])
    if more_expensive_value < product_price:
        more_expensive_value = product_price
        name_product = product

print(f'Ingresos totales: ${total_incomes}')
print(f'Producto más caro: {name_product} (Precio actualizado a ${more_expensive_value * (1 - 0.1)})')

# Respuesta
# Diccionario anidado que representa productos
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Inicializa las variables
total_cost = 0
most_expensive_product = None
highest_price = 0

# Calcula el costo total y encuentra el producto más caro
for product in products:
    # Accede a los detalles de producto
    price = products[product]['price']
    quantity = products[product]['quantity']
    discount = products[product]['discount']

    # Calcula el costo de cada producto
    cost = price * quantity * (1 - discount)
    total_cost += cost

    # Comprueba si el producto actual es el más caro
    if price > highest_price:
        highest_price = price
        most_expensive_product = product

# Actualiza el precio del producto más caro (ejemplo: reducirlo en un 10%)
if most_expensive_product:
    products[most_expensive_product]['price'] *= 0.9

# Muestra los resultados
print(f"Ingresos totales: ${total_cost:.2f}")
print(f"Producto más caro: {most_expensive_product} (Precio actualizado a ${products[most_expensive_product]['price']:.2f})")

# Next steps
financial_info = {
'American Express': {'stock_price': 93.23, 'market_cap': 93.7, 'dividend_yield': 1.3},
'Boeing': {'stock_price': 178.44, 'market_cap': 101.2, 'dividend_yield': 0.0},
'Coca-Cola': {'stock_price': 45.15, 'market_cap': 198.6, 'dividend_yield': 3.1},
'Nike': {'stock_price': 97.99, 'market_cap': 152.0, 'dividend_yield': 0.8},
'JPMorgan': {'stock_price': 96.27, 'market_cap': 362.5, 'dividend_yield': 2.6},
'Walmart': {'stock_price': 130.68, 'market_cap': 370.0, 'dividend_yield': 1.8}
}

# Agregar y eliminar elementos en un diccionario

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan': 96.27,
    'Walmart': 130.68,
    'Microsoft': 208.35
}
financial_info['Walt Disney'] = 119.34
print(financial_info)

# Verificar si la clave ya existe y agregar o actualizar

if financial_info.get('Walt Disney') == None:
    financial_info['Walt Disney'] = 119.34
else:
    financial_info['Walt Disney'] += 3.2

print(financial_info)

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan': 96.27,
    'Walmart': 130.68,
    'Microsoft': 208.35
}

del financial_info['Nike']
print(financial_info)

# pop method: Para eliminar un elemento del diccionario y acceder a su valor

walmart_price = financial_info.pop('Walmart')
print(walmart_price)
print(financial_info)


clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

incomes_per_field = {} # aquí colocarás los ingresos para cada campo

for client in clients:
    area = client[4]
    income = client[3]
    
    if incomes_per_field.get(area) == None:
        incomes_per_field[area] = [income]
    else:
        incomes_per_field[area].append(income)
    
print(incomes_per_field)

print()
print('Methods')
print(f'.keys(): {incomes_per_field.keys()}')
print(f'.values(): {incomes_per_field.values()}')
print(f'.items(): {incomes_per_field.items()}')

