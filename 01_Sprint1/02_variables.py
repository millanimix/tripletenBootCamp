# Practice file S1

print ('¡Hola, mundo!')

print('El número favorito de Max es...')
print()
print(3)

emperor = 'Romulus Augustulus'
reign_start = 475

print(emperor)
print(reign_start)

print(emperor, reign_start)

# Operators practice 
# suma
print(1.5 + 10)
# Resta
print(1.5 - 10)
# Multiplcacion
print(1.5 * 10)
# exponente
print(1.5 ** 10)
# Division
print(1.5 / 10)
# Cociente
print(15 // 10)
# Modulo
print(15 % 10)

print( (2 ** 3 + 12 / 2) / (5 * 4 -13))

french_speakers = 284.9
german_speakers = 132.0

total_speakers = french_speakers + german_speakers

print('Millones de personas que hablan francés o alemán:', total_speakers)

# Data types practice
language = 'Chino'
print(type(language))

# Strings
ch_language = 'Chino'
en_language = 'Inglés'

# Flotantes
ch_website_share = 0.017
en_website_share = 0.539

# Entero
ch_total_speakers = 1107
en_total_speakers = 1121

# Booleanos
ch_majority_native = True
en_majority_native = False

# Operador suma
print(ch_language + en_language)
print(ch_website_share + en_website_share)
print(ch_total_speakers + en_total_speakers)
print(ch_majority_native + en_majority_native)

# Se pueden multiplicar pero no sumar
print(' 123ABC ' * 6)

#Conversión de tipos de datos
total_sites = 10000000

en_sites = total_sites * en_website_share
en_sites = int(en_sites)

print(en_sites)
print(type(en_sites))

ch_total_speakers = int(ch_total_speakers)
ch_total_speakers = ch_total_speakers + 10
print(ch_total_speakers)
print(type(ch_total_speakers))

zipcode = 90210
print(type(zipcode))
zipcode = str(zipcode)
print(type(zipcode))

# Error Handling

# SyntaxError
# print ('Hola'

# Operating error & TypeError
# print (777 / 0)
# numbers = 'uno dos tres cuatro' + 5
# print(numbers)

# NameError
# apple_price = 1.25
# banana_price = 0.99
# print('Precio total:', apple_price + banana_price + kiwi_price)

try:
    print(777 / 0)
except:
    print('¡No podemos dividir entre cero')
    print('¡Sigamos adelante!')


metric = 34
print('métrica:', metric)

mi_string = 'TripleTen'
mi_flotante = 123.456
str(mi_flotante)
str(mi_string)

# int Lists Operations
citizen_CA = [-465, 156, -567, -6051, 8607]

total_amount = sum(citizen_CA)
max_tax_due = min(citizen_CA)
max_rebate = max(citizen_CA)

print(total_amount)
print(max_tax_due)
print(max_rebate)