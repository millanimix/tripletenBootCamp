# Chapter 3. Strings

my_string_1 = '¡String 1, string 2, string rojo, string, azul!'
my_string_2 = "¡String 1, string 2, string rojo, string, azul!"

print(my_string_1)
print(my_string_2)

# Usar dobles para imprimir apostrofe
print("Let's learn about strings!")

# Caráceres de escape
print('Let\'s learn about strings!')

print('Pete\'s favorite movie is:\t\t the last one he watches\n:D')

shopping_list = '''Mi lista de compras:
2 cartones de leche,
cereales de desayuno,
huevos,
pan'''

print(shopping_list)

sonnet = "Que la ruda mano del invierno no deshaga,\nEn ti el verano, antes tú debes ser destilado:\nEndulza algún pomo, en algún lugar atesórate\nCon el tesoro de la belleza antes que ella a sí se mate.\nNo es usura prohibida hacer pagar,\nA quien feliz paga por lo que debe;\nEso sería para ti engendrar otro tú,\nO diez veces más feliz, sea un diez por uno;\nDiez veces más feliz serás de lo que eres,\nSi diez de ti diez veces te figuran:\nPues, ¿qué podría hacer la muerte si partes,\nDejándote vivo, con descendencia?\nNo seas egoísta, tu belleza es mucha para conquista\nDe la muerte, que a los gusanos tus herederos haría."
print(sonnet)
print()
print(len(sonnet))

string_1 = 'HolaAdiós'
string_2 = 'Hola Adiós'
string_3 = 'Hola\nAdiós'
print(len(string_1))
print(len(string_2))
print(len(string_3))

print(len(''))

# Index String

word = 'supercalifragilisticexpialidocious'
letter = word[5]
print(letter)

last_letter = word[-1]
third_from_end = word[-3]
print(last_letter, third_from_end)

#IndexError
# word = 'word'
# print(word[8])

# Strings inmutable dataytpe
# word = 'bbc'
# word[0] = 'a'

word = 'bbc'
word = 'abc'

# Slices
city = 'Rio de Janeiro, Brasil'
substring = city[7:14]
print(substring)

print(city[4:1000])
print(city[-15:500])
print(city[4:0])

print(city[16:])

# Strings formateados
message = 'Vistoria tiene 23 años y mide 157 cm'
print(message)

# Mucho trabajo
name = 'Victoria'
age = 23
height = 157
message = name + ' tiene ' + str(age) + ' años y mide ' + str(height) + ' cm'
print(message)

# Usando f-strings
message = f'{name} tiene {age} años y mide {height} cm'
message = f'{name} tiene {age + 1} años y mide {height} cm'
print(message)

# Método format()
message = '{} tiene {} años y mide {} cm'.format(name, age, height)
print(message)
message = '{n} tiene {a} años y mide {h} cm'.format(h = height, n = name, a = age)
print(message)

# String Methods
message = '¡Hola, me llamo Han Solo!'
print(message)
message_new = message.upper()
print(message_new)

message_new = message.lower()
print(message_new)

shopping_list = '''aciete de colza
aceite de girasol
aceite de aguacate
aciete de cacahuate'''
print(shopping_list.replace('aciete','aceite'))

user_ids = '_151234_, _792051_, _955247_'
user_ids = user_ids.replace('_', '')
print(user_ids)

column_name = '          fecha de compra    '
print(column_name)
print(len(column_name))
print()
print(column_name.strip())
print(len(column_name.strip()))

name = 'Clint Eastwood'
print(name[:5])

name = 'Clint Eastwood'
print(name[100:])

city = 'Moscú'
country = 'Rusia'
phrase = '{0} es la capital de {1}'.format(city, country)
print('FIN')