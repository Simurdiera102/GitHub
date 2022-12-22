# Este programa calcula cuantos años hacen falta o cuantos años han pasado desde el año que introduce el usuario hasta el año acual

actual = input('Por favor introduce el año actual: ')
actualyear = 0

if actual.isnumeric():
    actualyear = int(actual)
else:
    print('Debes introducir un valor numerico')
    exit()

entrada = input('Ahora introduce otro año para calcular: ')
yeartocal = 0

if entrada.isnumeric():
    yeartocal = int(entrada)
else:
    print('Debes introducir un valor numerico')
    exit()


if yeartocal < 2021:
    resta1 = actualyear - yeartocal
    print('Hacen falta ' + str(resta1) + ' años para el 2022')

elif yeartocal == 2021:
    print('Falta solo 1 año para el 2022')

elif yeartocal == 2023:
    print('Ha pasado solo 1 año desde el 2022')

elif yeartocal > 2023:
    resta2 = yeartocal - actualyear
    print('Han pasado ' + str(resta2) + ' desde el año 2022')
else:
    print('Introdujiste el mismo año que el actual, por favor intenta con un año diferente')
    exit()
