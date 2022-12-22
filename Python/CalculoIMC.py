# Este programa consiste en un formulario en el cual se le pedira al usuario que ingrese informacion personal
# la cual sera utilizada para calcular su indice de masa corporal (IMC).
# Una vez obtenidos los datos, se le mostrara los resultados del formulario al usuario incluido su IMC.

print('A continuacion te pediremos algunos datos personales')
nombre = input('Por favor introduce tu nombre: ')
apellido1 = input('Por favor introduce tu apellido paterno: ')
apellido2 = input('Por favor introduce tu apellido materno: ')
try:
    edad = int(input('Por favor introduce tu edad: '))
except:
    print('Debes ingresar un valor numerico entero')
try:
    peso = float(input('Por favor introduce tu peso (kilos): '))
except:
    print('Debes ingresar un valor numerico')
try:
    estatura = float(input('Por favor introduce tu estatura (metros): '))
except:
    print('Debes ingresar un valor numerico')

print('Tus datos personales son:')
print('Tu nombre completo es: ' + nombre + ' ' + apellido1 + ' ' + apellido2)
print('Tu edad es: ' + str(edad) + ' años')
print('Tu peso es: ' + str(peso) + ' kilos (kg)')
print('Tu estatura es: ' + str(estatura) + ' metros (m)')

print('Ahora calcularemos tu masa corporal')

print(f'Tu indice de masa corporal es: ' {peso/estatura**2} 'kg/m2')

print('Muchas gracias por utilizar este programa, saludos!')
