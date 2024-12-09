# Funciones

def omelet(eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

# llamada a la función con 2 huevos, su resultado se asigna a la variable omelet_type
omelet_type = omelet(2)
print(omelet_type) # imprime el resultado de la instrucción anterior
print(omelet(3)) # imprime el resultado de una nueva llamada con 3 huevos

def square(x):
    return x ** 2

print(f'The Square is: {square(2)}')

print()
print('Funciones para optimizar el código')
print()

def calculate_total_price(price, quantity):
    total = price * quantity
    if total > 100:
        total -= total * 0.05
    return total

first_item_quantity = 3
first_item_price = 10.0

second_item_quantity = 2
second_item_price = 51.0

third_item_quantity = 10
third_item_price = 4.0

first_item_total = calculate_total_price(first_item_price, first_item_quantity)
second_item_total = calculate_total_price(second_item_price, second_item_quantity)
third_item_total = calculate_total_price(third_item_price, third_item_quantity)

print(first_item_total)
print(second_item_total)
print(third_item_total)

print()
print('Actividad')
print()

# Inventario de libros inicial
inventory = []

# Tarea 1: encapsular la adición de un libro
def add_book(title, author, available=True):
    inventory.append({"title": title, "author": author, "available": available})

# Tarea 2: encapsular la comprobación de disponibilidad
def check_availability(title):
    for book in inventory:
        if book["title"] == title:
            print(f"'{title}' está disponible: {book['available']}")
            return
    print(f"'{title}' no está en el inventario.")

# Tarea 3: encapsular el préstamo de un libro
def lend_book(title):
    for book in inventory:
        if book["title"] == title:
            if book["available"]:
                book["available"] = False
                print(f"'{title}' ha sido prestado.")
            else:
                print(f"'{title}' ya está prestado.")
            return
    print(f"'{title}' no está en el inventario.")

# Tarea 4: encapsular el listado de todos los libros
def list_books(status="all"):
    for book in inventory:
        if status == "all":
            print(f"Título: {book['title']}, Autor(a): {book['author']}, Disponible: {book['available']}")
        elif status == "available" and book["available"]:
            print(f"Título: {book['title']}, Autor(a): {book['author']}, Disponible: {book['available']}")
        elif status == "lent" and not book["available"]:
            print(f"Título: {book['title']}, Autor(a): {book['author']}, Disponible: {book['available']}")

# Usar las funciones

# Agregar libros al inventario
add_book("1984", "George Orwell")
add_book("To Kill a Mockingbird", "Harper Lee", available=True)
add_book("The Great Gatsby", "F. Scott Fitzgerald")

# Comprobar la disponibilidad de un libro
check_availability("1984")
check_availability("Moby Dick")

# Prestar un libro
lend_book("1984")
lend_book("The Great Gatsby")

# Listar todos los libros
print("\nTodos los libros:")
list_books("all")

print("\nLibros disponibles:")
list_books("available")

print("\nLibros prestados:")
list_books("lent")

print()
print('Filter Functions')
print()

# función que devuelve una copia filtrada de una lista anidada
def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration:
            filtered_result.append(row)
# devuelve los resultados filtrados
    return filtered_result 

# esta función acepta la lista anidada como entrada y la muestra, sin devolver nada
def print_movie_info(data):
    for movie in data:
        print(movie)

# llamemos a la función sobre movies_info:

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

movies_filtered = filter_by_timing(movies_info, 180)
print_movie_info(movies_filtered)


print()
print('Filter Functions Activity')
print()

# esta función imprime la tabla filtrada. No modificar
def print_movie_info(data):
    for movie in data:
        print(movie)

def filter_by_year(data, year): 
    filtered_result = []
    for row in data:
        if row[2] > year:
            # print(year)
            filtered_result.append(row)
    return filtered_result 

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

# A continuación tienes dos llamadas a funciones: para filtrar y para imprimir
movies_filtered = filter_by_year(movies_info, 1990)
print_movie_info(movies_filtered)

print()
print('Global and local Variable')
print()

milk = 50 # Variable global

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    result = result + ' y leche (ml): ' + str(milk) # Acceder a la variable global
    print(result)

omelet(True, 3)

counter = 10 # Variable global

def increment_counter():
    global counter  # Acceder a la variable global
    counter += 1  # Modificar la variable global

increment_counter()
print(counter)
increment_counter()
print(counter)

result = '¡El omelet está listo!' # Variable global

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    print(result)

omelet(True, 3)
print(result)


# Variable global que representa el saldo bancario inicial
balance = 1000\

# Muestra el saldo inicial
print(f"Saldo inicial: {balance}")

# Función para realizar una operación de depósito
def deposit_money(amount):
    global balance  # Accede a la variable global 'balance'
    local_balance = balance  # Variable local para realizar un seguimiento del saldo temporal

    # Agrega el monto del depósito al saldo local
    local_balance += amount
    
    # Actualiza el saldo global
    balance = local_balance

# Realiza operaciones de depósito
deposit_money(200)  # Depositar 200
print(f"Saldo global actualizado: {balance}")

deposit_money(150)  # Depositar 150
print(f"Saldo global actualizado: {balance}")

print()
print('Global and local Variable Exercise')
print()

# Diccionario global que representa los niveles de inventario actuales
inventory = {
    'manzana': 50,
    'plátano': 30,
    'naranja': 20
}

# Muestra el inventario inicial
print("Inventario inicial:", inventory)

# Función para agregar stock
def add_stock(product, quantity):
    global inventory
    if product in inventory:
        # El producto existe, actualiza el stock existente
        local_quantity = inventory[product]
        local_quantity += quantity
        inventory[product] = local_quantity
        print(f"Se agrega(n) {quantity} {product}(s). Nuevo inventario: {inventory[product]}")
    else:
        # El producto no existe, agrega el nuevo producto al inventario
        inventory[product] = quantity
        print(f"Se agrega el nuevo producto {product} con {quantity} unidades. Nuevo inventario: {inventory[product]}")

# Función para quitar stock
def remove_stock(product, quantity):
    global inventory
    if product in inventory:
        local_quantity = inventory[product]
        if local_quantity >= quantity:
            local_quantity -= quantity
            inventory[product] = local_quantity
            print(f"Se quita(n) {quantity} {product}(s). Nuevo inventario: {inventory[product]}")
        else:
            print(f"Stock insuficiente de {product}. No se puede(n) quitar {quantity} {product}(s).")
    else:
        print(f"El producto {product} no existe en el inventario. No se puede quitar el stock.")

# Realiza operaciones de stock
add_stock('manzana', 20)       # Agregar 20 manzanas
remove_stock('plátano', 10)   # Quitar 20 plátanos
remove_stock('naranja', 25)   # Intentar quitar 25 naranjas
remove_stock('uva', 50)       #  Quitar 50 uvas
add_stock('kiwi', 30)        # Agregar el nuevo producto 'kiwi' con 30 unidades
remove_stock('kiwi', 15)     # Quitar 15 kiwis

def my_function():
    print('hola')

print(my_function())

def subtraction(minuend, subtrahend):
    result = minuend - subtrahend
    print(result)

# subtraction(minuend=5, 6)
#Puedes combinar argumentos posicionales y con nombre. Pero no olvides especificar primero
# el argumento posicional. A continuación, puedes especificar el argumento con nombre.
# Por lo tanto, una llamada correcta a la función tiene el siguiente formato: 
subtraction(5, subtrahend=6)