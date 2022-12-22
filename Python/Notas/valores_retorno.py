# #Valores de retorno, sentencia return

# # def promedio(*numeros):
# #     return sum(numeros)/len(numeros)

# # x = promedio(4,5,6)
# # print(x)

# def area(**dato):
#     """ Calcula el area de una figura geometrica y la imprime en pantalla"""

#     if dato['figura'] == 'Rectangulo':
#         return(dato['base']*dato['altura'])
#     elif dato['figura'] == 'Triangulo':
#         return(dato['base']*dato['altura']/2)
#     elif dato['figura'] == 'Circulo':
#         return(3.1415*dato['radio']**2)
#     else:
#         print('Figura desconocida')


# triangulo = area(figura='Triangulo', base=10, altura=6)
# print(f'El area del trianngulo es: {triangulo}')
# circulo = area(figura='Circulo', radio=3, color='Rojo')
# print(f'El area del circulo es: {circulo}')
# dodecaedro = area(figura='Dodecaedro', lado=10)
# print(f'El area del dodecaedro es: {dodecaedro}')

# #############################################################

# Recursividad de funciones en python

# def factorial(numero, intentos=0):
#     if numero == 0:
#         return 1
#     else:
#         intentos += 1
#         print(intentos)
#         return numero*factorial(numero - 1, intentos)


# print('El factorial de 0 es (0!): ', factorial(0))
# print('El factorial de 1 es (1!): ', factorial(1))
# print('El factorial de 3 es (3!): ', factorial(3))

#########################################################

# Funciones lambda o funciones anonimas

# def suma(x, y): return x + y


# print(suma('Hola', 'mundo'))
# print(suma(2, 6))

# lista_numeros = [1, 0, 8, -3]
# lista_numeros = sorted(lista_numeros, key=lambda n: abs(n))
# print(lista_numeros) #Ordenar la lista con el valor absoluto

########################################################

# Funcion ZIP

paises = ['Kenia', 'Francia', 'Japon']
capitales = ['Nairobi', 'Paris', 'Tokio']
poblacion = [54, 66, 110]

for i in zip(paises, capitales, poblacion):
    print(i)  # Sirve para hacer emparejamientos entre tuplas que tengamos definidas, pero solo con valores que estan definidos
