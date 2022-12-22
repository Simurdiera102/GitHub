# En esta segunda parte se hara un programa que verifique la pertenencia de los datos ingresados dentro de un cuadrante
# especifico tomando en cuenta el plano cartesiano, siendo (-,+) el cuadrante 1, (+,+) el cuadrante 2,
# (-,-) el cuadrante 3 y (+,-) el cuadrante 4.
# se le pedira al usuario que ingrese  dos datos numericos y despues de esto el programa le dira
# a que cuadrante pertenece dicho par numerico.

# Parte 2 - Programa que verifica la existencia de x & y dentro de un cuadrante especifico

# En esta primera parte se le pide que por favor ingrese valores tanto para X como para Y.

print('Bienvenido al programa!')

# Se define una lista vacia para agrupar posteriormente a los valores x, y ademas de las
# variables que utilizare durante el programa

lista = []
fin = ('Fin del programa')

# Quise poner un verificador de valores para que en caso de no agregar un valor numerico no deje
# correr el programa hasta que el usuario ingrese los datos correctos

while True:
    try:
        x = int(input('Por favor ingrese un valor numerico entero para x: '))
        y = int(input('Por favor ingrese un valor numerico entero para y: '))
        break
    except ValueError:
        print('No ha ingresado datos numericos enteros, por favor intente nuevamente')
        continue

# Agrupo los valores de (x, y) dentro de la lista vacia

lista.append(x)
lista.append(y)

# En este primer bloque de condicionales defino si los valores estan sobre un eje, el origen o algun cuadrante

if x == 0 and y == 0:
    print(f'Los valores {lista} se encuentran en el origen ')
    print(fin)
    exit()
if x == 0:
    print(f'Los valores {lista} estan sobre el eje Y')
    print(fin)
    exit()
elif y == 0:
    print(f'Los valores  {lista} estan sobre el eje X')
    print(fin)
    exit()
else:
    print(f'Los valores  {lista} pertenecen a un cuadrante')

# En este segundo bloque en caso de que (x,y) pertenezcan a algun cuadrante, se define a cual de ellos
# pertenece

if x < 0 and y > 0:
    print(f'Los valores {lista}  pertenecen al cuadrante 1')
if x > 0 and y > 0:
    print(f'Los valores {lista} pertenecen al cuadrante 2')
elif x < 0 and y < 0:
    print(f'Los valores {lista} pertenecen al cuadrante 3')
else:
    print(f'Los valores {lista} pertenecen al cuadrante 4')

print(fin)

# Fin del programa
