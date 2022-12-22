# Realizar un diccionario, pero esta  vez,  en  lugar  de  emojis,
# con  colores  del  arcoíris  (rojo,  naranja, amarillo, verde, azul y violeta)
# y en dos idiomas diferentes.

# Al iniciar el programa, debes indicar al usuario cuáles son los dos idiomas a los que puede traducir tu programa.
# El usuario debe elegir a cuál de los idiomas quiere traducir.
# Al ingresar una oración en español que incluya uno de los colores del arcoíris,
# debe desplegar en la pantalla una frase que indique cómo se dice ese color en el idioma seleccionado.

# Este programa podra traducir los colores que esten incluidos en las frases que ud ingrese,
# Podra ser en ingles o español, depende de su necesidad.

dicionario_colores = {'red': 'rojo', 'rojo': 'red', 'naranja': 'orange', 'amarillo': 'yellow',
                      'verde': 'green', 'azul': 'blue', 'violeta': 'violet', 'morado': 'purple',
                      'orange': 'naranja', 'yellow': 'amarillo', 'green': 'verde', 'blue': 'azul',
                      'violet': 'violeta', 'purple': 'morado'}

print('Please choose input language/Por favor escoja el lenguaje de entrada')
eleccion = input('English (1), Español (2): ')

if eleccion == '1':
    frase = input('Please write a sentence: ')
    frase.lower()
    palabras = frase.split()

elif eleccion == '2':
    frase = input('Por favor escriba una frase: ')
    frase.lower()
    palabras = frase.split()

else:
    print('You have not selected any valid option/No ha seleccionado ninguna opcion valida')
    print('End of program/Fin del programa')
    exit()

respuesta = ' '

for palabra in palabras:
    if palabra in dicionario_colores:
        respuesta = respuesta + dicionario_colores[palabra] + ' '
    else:
        respuesta = respuesta + palabra + ' '

print(respuesta)
