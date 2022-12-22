# Manejo de errores +, **, -

numerador = 10

denominador = 0
cadena = '3'
numerico = 5

print(numerador/denominador)
print(cadena + numerico)

try:
    print(numerador / denominador)

except (ZeroDivisionError, TypeError):
    print('Ha ocurrido un error')

print('Fin del programa')

# Se puede hacer esto mismo para cualquier tipo de error

#Error1:  ZeroDivisionError
# Error 1: TypeError

##########################################################

# Manejo de errores con excepciones y ciclos

while True:
    try:
        dividendo = int(input('Ingrese el dividendo: '))
        divisor = int(input('Ingrese el divisor: '))
        print('El resultado es: ', dividendo/divisor)
        break
    except ValueError:
        print('Debe ser un valor numerico')
    except ZeroDivisionError:
        print('No se puede dividir por cero')

print('Fin del programa')


######################################################

# Ejercicio de la semana
while True:
    nombre = input('Introduce tu nombre')
    apellido = input('Introduce tu apellido: ')
    if nombre == '':
        print('No has ingresado tu nombre')
    elif apellido == '':
        print('No has ingresado tu apellido')
    else:
        break

while True:
    try:
        edad = int(input('Introduce tu edad: '))
        break
    except ValueError:
        print('Debes introducir un numero')

correo = input('Introduce tu telefono: ')

while True:
    try:
        telefono = input('Introduce tu telefono: ')
        int(telefono)
        break
    except ValueError:
        print('Debes introducir un numero')

print('Nombre: ' + nombre)
print('Apellido: ' + apellido)
print('Tengo ' + str(edad) + 'años')
print('Correo: ' + correo)
print('Telefono: ' + telefono)
