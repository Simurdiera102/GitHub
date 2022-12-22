###Modulo de m_retosemanal(m_retosemanal.py)

def diccionario_listas(n):
    diccionario = {}
    
    for i in range(1, n + 1):
        diccionario[i] = []


def agregar_datos(lista, valor):
    """
    Funcion que agrega un dato a una lista especificada
    """
    if valor == ' ':
        valor = 'No especificado'
    lista.append(valor)
    return lista


def comparar_listas(lista1, lista2):
    """
    Funcion que compara elementos de ambas listas y encuentra los elementos que se repiten
    """
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    return list(conjunto1 & conjunto2)


def array_diff(lista1, lista2):
    """
    Funcion que extrae los elementos comunes entre la lista 1 y la lista 2 de la lista 1 y los imprime
    """
    return [i for i in lista1 if i not in lista2]


# lista1 = []
# lista2 = []

# nombres1 = int(input('¿Cuantos elementos desea registrar en la lista 1?: '))
# nombres2 = int(input('¿Cuantos elementos desea registrar en la lista 2?: '))

# for i in range(nombres1):
#     elemento1 = input(
#         f'Ingrese el nombre del elemento {i + 1} de la lista 1: ').title()
#     lista1 = agregar_datos(lista1, elemento1)

# for j in range(nombres2):
#     elemento2 = input(
#         f'Ingrese el nombre del elemento {j + 1} de la lista 2: ').title()
#     lista2 = agregar_datos(lista2, elemento2)

# print('Las listas originales son:')
# print(f'La lista 1 es: {lista1}')
# print(f'La lista 2 es: {lista2}')

# print('Los elementos que se extrajeron de la lista 1 son: ')
# print(comparar_listas(lista1, lista2))

# print('La lista filtrada sin los elementos repetidos en ambas listas es: ')
# print(array_diff(lista1, lista2))
