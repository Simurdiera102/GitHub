# Manejo de archivos

# Abrir y escribir en el archivo

# se pone f al principio por buenas practicas. w = escribir en el archivo

# f_archivo = open('archivo1.txt', 'w')
# print(f_archivo)
# f_archivo.write('Hola mundo!')
# f_archivo.close()  # Siempre se debe cerrar el archivo

# f_archivo = open('archivo.txt', 'w')
# f_archivo.write('Este es mi primer archivo')
# f_archivo.close()

# # Abrir en modo lectura

# f_lectura = open('archivo.txt', 'r')
# print(f_lectura.read())
# f_lectura.close()

# print(f_archivo)
# print(f_lectura)

# ######################################################

# # Sentencias with y as

# f_lectura = open('archivo.txt', 'r')
# print(f_lectura.closed)
# f_lectura.close()
# print(f_lectura.closed)

# with open('archivo.txt', 'r') as f_lectura:
#     print(f_lectura.closed)
# print(f_lectura.closed)

# with open('archivo.txt', 'a') as f_archivo:  # a = append (agregar texto)
#     f_archivo.write('\este es mi primer archivo 2')
#     f_archivo.write('Este es mi primer archivo 3')
#     f_archivo.write('\n')
#     f_archivo.write('\tEste es mi promer archivo 4')
# with open('archivo.txt', 'r') as f_lectura:
#     # print(f_lectura.read())
#     contenido = f_lectura.read()
#     print(f'"""{contenido}"""')
#     contenido = f_lectura.read()
#     print(f'"""{contenido}"""')

# ######################################################################

# # Lectura de archivos linea por linea

# with open('archivo.txt', 'r') as f_lectura:
#     numero_de_lineas = 0
#     for i in f_lectura:
#         numero_de_lineas += 1
#         print(f'Linea {numero_de_lineas}: {i}')
#     print(f'El archivo tiene {numero_de_lineas} lineas')

# # Creando una lista a partir de un archivo

# with open('archivo.txt', 'r') as f_archivo:
#     lista_archivo = f_archivo.readlines()
#     print(lista_archivo)

# print(lista_archivo)

# lista_archivo[1] = 'Este es mi primer archivo 2\n'
# lista_archivo.insert(2, 'Este es mi primer archivo 3\n')

# print(lista_archivo)

# with open('archivo.txt', 'w') as f_archivo:
#     f_archivo.writelines(lista_archivo)

#########################################################

# Ejercicio de la semana 14

# Con el ejercicio de la semana anterior pero para multiples personas

personas = []


while True:
    print("""
    1. Agregar persona a la agenda
    2. Guardar datos en un archivo.
    """)

    opcion = input(
        'Por favor ingrese una opcion: ')

    if opcion == '1':

        contacto = []  # Agregar todos los datos al contacto de la semana pasada 13
        while True:
            nombre = input('Introduce tu nombre: ')
            apellido = input('Introduce tu apellido: ')
            if nombre == '':
                print('No has ingresado tu nombre')
            elif apellido == '':
                print('No has ingresado tu apellido')
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break

        while True:
            try:
                edad = int(input('Introduce tu edad: '))
                contacto.append(edad)
                break
            except ValueError:
                print('Debes introducir un numero')

        correo = input('Introduce tu correo: ')
        contacto.append(correo)

        while True:
            try:
                telefono = input('Introduce tu telefono: ')
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print('Debes introducir un numero')

        personas.append(contacto)

    elif opcion == '2':
        with open('agenda.txt', 'w') as f_agenda:
            for persona in personas:
                f_agenda.write(
                    f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n')
        print('Datos guardados en agenda.txt')

        with open('agenda.txt', 'r') as f_agenda:
            print(f_agenda.readlines())
        f_agenda.close()

        break
    else:
        print('Opcion invalida')
        print('Volver a intentar')
