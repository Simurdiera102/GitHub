# Ejercicio de validador de edad

entrada = input('Por favor introduce tu edad: ')

edad = 0

if entrada.isnumeric():
    edad = int(entrada)

else:
    print('Dato incorrecto, debes introducir un numero')
    exit()

if edad <= 0:
    print('Imposible, no puedes tener esa edad')

elif edad > 115:
    print('Eres muy viejo, no te creo')

elif edad < 18:
    print('Eres menor de edad')

else:
    print('Eres mayor de edad')
