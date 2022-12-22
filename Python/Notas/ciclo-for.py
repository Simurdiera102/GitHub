# Para correr el codigo debes descomentar las lineas seleccionandolas y aplicando ctrl+k+u
# O correrlo en modo debug python file definiendo lineas de inicio seleccionandolas manualmente desde donde quieres que inicie el codigo

# for i in 1, 1, 3 :
#     print(i)

# for i in range(3) :
#     print(i)

# for i in ['Ale', 'Ivan', 'Manuel', 'Luis', 'Rafa', 'Lucas']:
#     print(i)

# for i in 'Hola Mundo':
#     if i == 'M':
#         pass
#     else:
#         print(i, end='')

# Ejercicio de la semana

# for i in range(2, 100):
#     primo = True
#     for j in range(2, i):
#         if i == j:
#             break #proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa.
#         elif i % j == 0:
#             primo = False
#         else:
#             continue
#     if primo == True:
#         print(i, end=' ')

# Ejercicios adicionales

# Programa que pide un numero de inicio y otro final,
# y que suma todos los multiplos de 3 que hay entre ellos

# inicio = int(input('introduce un numero de inicio: '))
# final = int(input('Introduce un numero final: '))
# suma = 0

# while inicio <= final:
#     if inicio % 3 == 0:  # Resto de la division es igual a 0
#         suma += inicio
#     inicio += 1
# print('El resultado es: ', suma)

# Programa que pide contraseña y no te deja entrar hasta que la pongas correcta (Sin limite de intentos)

# print('Bienvenido al programa')

# password = input('Introduce tu contraseña: ')

# intento = input('Introduce de nuevo la contraseña: ')

# while intento != password:
#     print('Las contraseñas no coinciden')
#     intento = input('Intentalo nuevamente: ')

# print('Contraseña correcta')
