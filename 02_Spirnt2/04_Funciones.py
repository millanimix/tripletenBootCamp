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


# crea aquí tu función filter_clients
def filter_clients(data, area):
    new_list = []
    for client in data:
        if client[4] == area:
            new_list.append(client)
    return new_list

filtered_list  = filter_clients(clients, 'Transportation') # llama a la función aquí

# muestra el resultado aquí
print(filtered_list)

# define tu función aquí
def clean_user(user_info, index_name, index_age):
    # Paso 1: elimina del nombre espacios iniciales y finales, así como guiones
    user_name_1 = user_info[index_name].strip()
    user_name_1 = user_name_1.replace('_', ' ')

    # Paso 2: convierte la edad en entero
    user_age_1 = int(user_info[index_age])

    # Paso 3: separa el nombre y el apellido en una sublista
    user_name_1 = user_name_1.split()

    # Prepara la lista con la información completa del usuario
    # Reemplaza el nombre y la edad originales con los datos limpios
    user_info[index_name] = user_name_1
    user_info[index_age] = user_age_1

    return user_info

# Prueba la función
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
name_index = 1
age_index = 2

print(clean_user(test_user, name_index, age_index)) # completa aquí el llamado de la función

print()
print()

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

users_categories_low = []
for user in users:
    categories_low = []
    for category in user[3]: # escribe tu código aquí
        lowered_category = category.lower() # escribe tu código aquí
		# escribe tu código aquí
        categories_low.append(lowered_category)
    user.pop(3)
    user.insert(3, categories_low)
    users_categories_low.append(user)

# escribe tu código aquí
print(users_categories_low)


print()
print()

def clean_user(user_info, name_index, age_index, cat_index):

  # Paso 1: pon todo en minúsculas y elimina del nombre espacios iniciales y finales, así como guiones
  user_name_1 = user_info[name_index].lower()
  user_name_1 = user_name_1.strip()
  user_name_1 = user_name_1.replace('_', ' ')

  # Paso 2: convierte la edad en entero
  user_age_1 = int(user_info[age_index]) # escribe tu código aquí

  # Paso 3: separa el nombre y el apellido en una sublista
  user_name_1 = user_name_1.split() # escribe tu código aquí

  # Paso 4: separa el nombre y el apellido en una sublista
  categories_low = []
  for category in user_info[cat_index]: # escribe tu código aquí
      lowered_category = category.lower()
      categories_low.append(lowered_category)

  # Prepara la lista con la información completa del usuario
  # Reemplaza el nombre y la edad originales con los datos limpios
  # escribe tu código aquí
  user_info[name_index] = user_name_1
  user_info[age_index] = user_age_1
  user_info[cat_index] = categories_low

  return user_info


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

name_index = 1
age_index = 2
cat_index = 3
users_cleaned = []

for user in users: # escribe tu código aquí
    user_cleaned = clean_user(user, name_index, age_index, cat_index) # escribe tu código aquí
    users_cleaned.append(user_cleaned) # escribe tu código aquí

print(users_cleaned)



print()
print()

users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for user in users:
	# escribe tu código aquí
    spending_list = user[4]
    revenue += sum(spending_list)

print(revenue)


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount: # escribe tu código aquí
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
	total_amount_spent +=  new_purchase# escribe tu código aquí

print(total_amount_spent)


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]


# escribe tu código aquí
for user in users:
    if user[2] < 30:
        print(user[1][0])

print()
for user in users:
    if user[2] < 30 and sum(user[4]) > 1000:
        print(user[1][0])

print()
for user in users:
    for category in user[3]:
        if category == 'clothes':
            print(user[1][0], user[2])

print()
print()
def get_client_by_cat(users, id_index, name_index, age_index, category_index, amounts_index, filter_category):
    # escribe tu código aquí
    filtered_clients = []
    for user in users:
        for category in user[category_index]:
            if category == filter_category:
                id_user = user[id_index]
                name_user = user[name_index]
                age_user = user[age_index]
                expenses_user = sum(user[amounts_index])
                filtered_clients.append([id_user, name_user, age_user, expenses_user])
    
    return filtered_clients

# La lista de usuarios
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
]

# Llama a la función con la categoría 'home'
result = get_client_by_cat(users, 0, 1, 2, 3, 4, 'home') # escribe tu código aquí

# Muestra en pantalla la lista que resulta
print(result)
