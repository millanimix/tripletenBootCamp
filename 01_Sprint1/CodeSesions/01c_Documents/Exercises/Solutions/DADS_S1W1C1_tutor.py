
# # Sprint 1 - Week 1 - Class 1
# 
# Coding Session
# 
# # Ejercicio 1
# 
# ## E1.1
# 
# John tiene 25 años y su hermano 20. Asigna sus edades a las variables
# `john_age` y `brother_age`, y verifica los tipos de variables que son
# cada una de ellas.


john_age = 25
brother_age = 20

print(type(john_age))
print(type(brother_age))


# ## E1.2
# 
# Calcula su diferencia de edad en una nueva variable (`diff_ages`), y
# luego muestra la siguiente frase “John tiene `john_age` años. Su hermano
# tiene `brother_age` y la diferencia de edad entre ellos es `diff_ages`”


diff_ages = john_age - brother_age
print("John tiene", john_age, "años. Su hermano tiene", brother_age, "y la diferencia de edad entre ellos es", diff_ages)


# # Ejercicio 2
# 
# ## E2.1
# 
# Escribe y rellena las siguientes variables:
# 
# `name` -\> John
# 
# `john_bitcoins` -\> 2.45
# 
# `btc_to_usd` -\> 71000
# 
# `has_driving_license` -\> True
# 
# Muestra todas las variables. A continuación, aplica la función type a
# cada una y comprueba el resultado. Después, calcula e imprime la
# cantidad de BTC que John tiene en dólares estadounidenses, utilizando el
# tipo de conversión indicado.


name  = 'John'
john_bitcoins  = 2.45
btc_to_usd = 71000
has_driving_license  = True

print(name)
print(john_bitcoins)
print(btc_to_usd)
print(has_driving_license)

print(type(name))
print(type(john_bitcoins))
print(type(btc_to_usd))
print(type(has_driving_license))

john_usd_worth = john_bitcoins * btc_to_usd
print(john_usd_worth)


# # Ejercicio 3
# 
# ## E3.1
# 
# John compró más de 1.3 bitcoins. Ejecuta el siguiente código y observa
# el error.


john_bitcoins = '2.45'

john_bitcoins = john_bitcoins + 1.3


# ## E3.2
# 
# Ahora agrega una línea entre las dos líneas de código existentes para
# convertir la variable a float, e imprimir la variable y su tipo. ¿Qué
# pasó?


john_bitcoins = '2.45'

john_bitcoins = float(john_bitcoins)

john_bitcoins = john_bitcoins + 1.3

print(john_bitcoins)
print(type(john_bitcoins))


# ## E3.3
# 
# Ahora convierte los bitcoins de John a int e imprime la variable y su
# tipo. ¿Qué pasó? ¿Ha perdido bitcoins?


john_bitcoins = int(john_bitcoins)

print(type(john_bitcoins))
print(john_bitcoins)


# # Ejercicio 4
# 
# John quiere enviar el 10% de su bitcoin a su amigo Max. Sin embargo,
# seleccionó una cartera que, por alguna razón, no es considerada válida,
# lo que hace que el programa genere un error.
# 
# ## E4.1
# 
# Ejecuta el código y observa el error. ¿Por qué recibimos este error?


btc_wallet_2 = '3.75'

btc_to_send = btc_wallet_2 * 0.1


# ## E4.2
# 
# Añade código para que el error quede más claro, mostrando el mensaje “Tu
# cartera no es válida. Por favor, inténtalo de nuevo.”, cuando falla.
# 
# Haz esto utilizando try except.


try:
    btc_to_send = btc_wallet_2 * 0.1
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')


# ## E4.3
# 
# Ahora corrige el código para que no produzca más errores. ¿A qué tipo de
# datos debemos convertir la cartera?


try:
    btc_to_send = float(btc_wallet_2) * 0.1
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')


# ## E4.4
# 
# Utiliza la función apropiada para convertirla y luego muestra la
# cantidad de btc enviada a su amigo Max de la siguiente manera: “Has
# enviado `btc_to_send` bitcoins con éxito”.


try:
    btc_to_send = float(btc_wallet_2) * 0.1
    print("Has enviado", btc_to_send, "bitcoins con éxito")
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')


# # Ejercicio 5
# 
# ## E5.1
# 
# Crea una lista que contenga 4 elementos a ser comprados en una tienda de
# abarrotes “azucar”, “flores”, “muchos colores”, “X”. Llámala
# `compras_abarrotes`.


compras_abarrotes = ["azucar", "flores", "muchos colores", "X"]


# ## E5.2
# 
# Imprime el tercer elemento de la lista


compras_abarrotes[2]


# ## E5.3
# 
# Imprime el tamaño de la lista


len(compras_abarrotes)


# ## E5.4
# 
# Adiciona un producto más al final de la lista.


compras_abarrotes.append("bellota") # Si usan append, preguntarse por qué no es necesario asignar el nuevo valor de compras_abarrotes
compras_abarrotes


# ## E5.5
# 
# Adiciona un producto más en la posicion 2 de la lista e imprime el
# resultado.


compras_abarrotes.insert(1, 'burbuja')
compras_abarrotes


# # Ejercicio 6
# 
# Sea una lista de productos de ferretería dada por Tornillos, Martillo,
# Pegamento. Llama a esa variable `compras_ferreteria`
# 
# ## E6.1
# 
# Crea esta nueva lista


compras_ferreteria = ["Tornillos", "Martillo", "Pegamento"]


# ## E6.2
# 
# Adiciona esta lista `compras_abarrotes` y guarda el resultado en
# `compras_ferreteria_mas_abarrotes`


compras_ferreteria_mas_abarrotes = compras_ferreteria + compras_abarrotes
compras_ferreteria_mas_abarrotes


# ## E6.3
# 
# Ordena la lista de compras en orden reverso e imprime el resultado
# final.


compras_ferreteria_mas_abarrotes.reverse()
compras_ferreteria_mas_abarrotes


# # Ejercicio 7
# 
# Sea la lista `python` definida a continuación


python = ['p','y','t','h','o','n']


# ## E7.1
# 
# Establezca 3 formas diferentes de obtener solamente los caracteres “py”
# filtrando la lista


print(python[0:2])
print(python[:2])
print(python[:-4])


# Sea ahora la lista `numeros` dada por


numeros = list(range(0,11,1))
print(numeros)


# ## E7.2
# 
# Obtenga solamente los elementos que se encuentran en una posición par


numeros[1::2]
# https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences


