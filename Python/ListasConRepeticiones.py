# El reto de esta semana es una variante del reto de la semana pasada:
# un programa que permita crear listas y elimine los valores existentes en otras listas,
# pero ligeramente diferente.
# 1. Todas las funciones que emplees deberán estar en un archivo diferente, llamado m_retosemanal.py.
# 2. Esta vez, se podrán crear varias listas; el usuario del programa especificará cuántas.
# 3. La longitud de cada lista la definirá el usuario.
# 4. Imprime las listas e indica que son las originales.
# 5. Se eliminarán los elementos de una lista que estén también en las listas posteriores.
# 6. Imprime las listas indicando que se eliminaron los elementos que estaban, también, en las listas posteriores.
# from Tareas.m_retosemanal import diccionario_listas
from DiccionarioListas import agregar_datos as agregar
#from m_retosemanal import diccionario_listas as diccionario


listas = []
lista = []

numero_listas = int(input('¿Cuantas listas desea agregar?: '))

for i in range(numero_listas):
    numero_elementos = int(
        input(f'Cuantos elementos desea en la lista {i + 1}?: '))

    for j in range(numero_elementos):
        elementos = input(
            f'Por favor ingrese el elemento {j + 1} de la lista {i + 1}: ')
        lista = agregar(lista, elementos)
    listas = agregar(listas, lista)

print('Las listas originales son: ')
print(listas)
