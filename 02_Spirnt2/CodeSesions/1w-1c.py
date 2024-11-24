# Sprint 2

lista_simple = ['Sueños de fuga', 'EE.UU', 1994, 'drama', 142, 9.111]


movies_info = [
    ['Sueños de fuga', 'EE.UU', 1994, 'drama', 142, 9.111],
    ['El padrino', 'EE.UU', 1972, 'drama, crimen', 175, 8.730],
    ['Batman: El caballero de la noche', 'EE.UU', 2008,'fantasía, acción, thriller', 152, 8.499],
    ['El señor de los anillos: el retorno del rey', 'New Zealand', 2003, 'fantasía, adventure, drama', 201, 8.625],
    ['Tiempos violentos', 'EE.UU', 1994, 'thriller, comedia, crimen', 154, 8.619],
    ['El bueno, el malo y el feo', 'Italia', 1966, 'western', 178, 8.5211],
    ['El club de la pelea', 'EE.UU', 1999, 'thriller, drama, crimen', 139, 9],
    ['Harakiri', 'Japan', 1962, 'drama, acción, histórico', 133, 8.4],
    ['Mente indomable', 'EE.UU', 1997, 'drama, romance', 126, 5J]
]

movies_info[0][1]
print(movies_info)

# categoria_de_la_pelicula = asignar_categoria_segun_puntaje(listas_de_info_de_pelicula)

def asignar_categoria_segun_puntaje (lista_de_info_de_pelicula):
    print(lista_de_info_de_pelicula[-1])

asignar_categoria_segun_puntaje(lista_simple)
asignar_categoria_segun_puntaje(movies_info[5])


def categorizar_pelicula (pelicula):
    score = pelicula[5]
    if score >= 8.5:
        return 'buena'
    elif score >= 7:
        return 'media'
    else:
        return 'mala'
    
