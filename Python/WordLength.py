# Para entender con mayor facilidad los dos programas del proyecto, se dividiran en dos partes
# La primera parte contendra el programa para identificar la longitud de una palabra ingresada, mientras que
# la segunda parte contendra el programa que identificara la pertenencia a un cuadrante especifico
# de los datos ingresados por el usuario.

# Parte 1 - Programa que identifica la longitud de una palabra ingresada por el usuario

# En esta parte del codigo decidi incluir un validador de texto para evitar que el usuario
# ingrese datos numericos o que haga entradas vacias, no le puse contador ya que solo al poner
# una letra el usuario puede salir del bucle, e inclui dentro del input instrucciones de solo ingresar texto

while True:
    palabra = input('Por favor ingrese una palabra (solo texto): ')
    if palabra.isalpha():
        break
    else:
        print('No ha ingresado un valor valido, intentelo nuevamente')

# En la segunda parte del codigo decidi definir la variable longitud para evitar errores de sintaxis
# dentro de los condicionales.

longitud = len(palabra)

# Aqui es la verdadera funcion del programa, en la cual se verifica la cantidad de caracteres
# que tiene la palabra y de esta forma le dice al usuario si los datos ingresados
# cumplen o no con las condiciones de tener entre 4 y 8 palabras.

if 4 <= longitud <= 8:
    print('La palabra ingresada es correcta')


elif longitud > 8:
    print(f'Sobran palabras, {palabra} tiene {longitud} palabras')

else:
    print(f'Hacen falta palabras, {palabra} solo tiene {longitud} palabras')

print('Fin del programa')
