# Parametro tipo tubla, *args

# def promedio(*numeros):
#     """
#     Recibe un solo parametro de tipo tupla, de valores numericos
#     e imprime su promedio
#     """
#     promedio = sum(numeros)/len(numeros)
#     print('El promedio es: ' promedio)


# promedio(4)
# promedio(4, 5, 6)
# promedio(1, 3, 4, 6, 7, 8)

# # Estas funciones sirven para calcular valores de caracteres indefinidos


# def es_numero(titulo, *seire):
#     print(titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit():
#             print(f'{i} es numero')
#         else:
#             print(f'{i} no es numero')


# es_numero('Numeros', '1', '2', '3')
# es_numero('Letras', 'a', 'b', 'c')

# nombre = 'Mezcla'
# lista_varios = ['a','2',3,'f', 5 ]
# es_numero(nombre, *lista_varios)

########################################################

# Parametros de tipo diccionario, *kwargs
# * para parametros de tipo tupla
# ** para parametros de tipo diccionario

def area(**dato):
    """ Calcula el area de una figura geometrica y la imprime en pantalla"""

    if dato['figura'] == 'Rectangulo':
        return(dato['base']*dato['altura'])
    elif dato['figura'] == 'Triangulo':
        return(dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        return(3.1415*dato['radio']**2)
    else:
        print('Figura desconocida')


area(figura='Triangulo', base=10, altura=6)
area(figura='Circulo', radio=3, color='Rojo')
area(figura='Dodecaedro', lado=10)
