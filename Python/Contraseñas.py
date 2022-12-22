# Se hara un programa que pida la contraseña al usuario y que muestre error cuando el primer
# caracter no sea un numero, ademas , una vez la ingrese correctamente se le pedira que la ingrese nuevamente
# tendra un maximo de 3 intentos para cada ingreso de la contraseña antes de que finalice el programa.

# Programa que pide contraseña y no te deja entrar hasta que la pongas correcta (Limite de intentos)

print('Bienvenido al sistema')

contador = 1
contador2 = 1
fin = 'Fin del programa'

password = input('Por favor introduce la contraseña: ')
while contador <= 2:
    if password[0].isnumeric():
        print('contraseña valida')
        break
    else:
        password = input('Por favor introduce la contraseña: ')
    if contador == 2:
        print(fin)
        exit()
    contador = contador + 1


while contador2 <= 3:
    intento = input("ingrese nuevamente la contraseña: ")
    if intento == password:
        print('contraseña correcta')
        print(fin)
        exit()

    else:
        print('Las contraseñas no coinciden')
        if contador2 == 3:
            print(fin)
            exit()
    contador2 = contador2 + 1
