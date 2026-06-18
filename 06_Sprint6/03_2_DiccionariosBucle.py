financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan': 96.27,
    'Walmart': 130.68
}

# Para recorrer las claver de un diccionario
for key in financial_info.keys():
    print(key)

# Para recorrer los valores de un diccionario
for value in financial_info.values():
    print(value)

financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0

for value in financial_info.values():
    total_value += value

print(total_value)

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan': 96.27,
    'Walmart': 130.68
}

for key, value in financial_info.items():
    print(key, value)

financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0 # el valor que actualizarás en cada iteración del bucle

# escribe tu bucle for aquí. En cada iteración del ciclo, extrae el precio
# y actualiza la variable total_value
for key, value in financial_info.items():
    total_value += value

print(total_value)