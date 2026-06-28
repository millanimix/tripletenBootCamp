def omelet(eggs_number=2):
    if eggs_number > 0:
        return '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    else:
        return '¿Cómo puedo hacer un omelet sin huevos?'
    print('Nunca podré mostrar el resultado :(')


print(omelet(3))
print(omelet(0))

# Multiples resultados
def area_and_perim(side_1, side_2):
    area = side_1 * side_2
    perimeter = 2 * (side_1 + side_2)
    return area, perimeter

print(area_and_perim(2, 3))

# Ejemplo descrompimiendo la tupla
def find_area_and_perim(side1, side2):
    area = side1 * side2
    perimeter = 2 * (side1 + side2)
    return area, perimeter

# descomprime el resultado de la función
rec_area, rec_perimeter = (find_area_and_perim(7, 3))

print(f'El área del rectángulo es {rec_area}, el perímetro es {rec_perimeter}')

