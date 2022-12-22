# Que pueda extenderse a cierta cantidad de alumnos
# Que pueda tener hasta 3 calificaciones, como minimo debe existir una
# Al finalizar, debe mostrar una linea por cada alumno y su calificacion promedio

# Programa que permite ingresar nombres de alumnos y sus calificaciones
# y que muestra sus calificaciones en listas y ademas de su promedio final

lista = []

alumnos = 1
deseados = int(input('¿Cuantos alumnos desea agregar?: '))
while alumnos <= deseados:
    opcion = input(
        'Para agregar alumno escoja (1) , para terminar el programa escoja (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        opcion2 = input(
            'Para agregar calificaciones escoja (1), Para continuar escoja otro numero diferente: ')
        if opcion2 == '1':
            calificacion1 = int(
                input(f'Ingrese la primera calificacion de {nombre}: '))
            calificacion2 = int(
                input(f'Ingrese la segunda calificacion de {nombre}: '))
            calificacion3 = int(
                input(f'Ingrese la tercera calificacion de {nombre}: '))
            calificaciones = [calificacion1, calificacion2, calificacion3]
            promedio = int(calificacion1 + calificacion2 +
                           calificacion3)/len(calificaciones)
            alumno = [nombre, calificacion1,
                      calificacion2, calificacion3, promedio]
            lista.append(alumno)
            alumnos += 1
        else:
            print('Debe agregar al menos una calificacion')
            continue
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opcion invalida.')
        continue

print('La lista de alumnos, con sus calificaciones y promedio es: ')
print(lista)
