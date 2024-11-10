# Excercise 1

john_age = 25
brother_age = 20

print(type(john_age))
print(type(brother_age))

#-------

diff_ages = john_age - brother_age
print("John tiene", john_age, "años. Su hermano tiene", brother_age, "y la diferencia de edad entre ellos es", diff_ages)

#-------

name = "John"
john_bitcoins = 2.45
btc_to_usd = 71000
# has_driving


#------
john_bitcoins = 2.45

john_bitcoins = john_bitcoins + 1.3

print(john_bitcoins)


#----
btc_wallet_2 = '3.75'
try:
    btc_to_send = btc_wallet_2 * 0.1
except:
    print("Tu cartera no es válida. Por favor, inténtalo de nuevo")