# Programa que simula una Maquina de Galton

# En esta seccion se importan las librerias
import matplotlib.pyplot as plt
import numpy as np

# En esta seccion se definen las variables, por defeecto el experimento se hara con 3000 canicas
# como lo establecen las instrucciones.

n = 3000
pasos = 12

# En esta seccion del programa se establecen las funciones que sse utilizan en la simulacion

# La primera funcion define el proceso logico que sigue la simulacion de las canicas en los 12 niveles


def random_galton(pasos):
    """
    Funcion que simula la distribucion de 3000 canicas si se sueltan una a una sobre 12 columnas,
    estableciendo una distribucion propia de una maquina de Galton la cual establece que si cada 
    canica se suelta teniendo una probabilidad del 50% de irse hacia la derecha o hacia la izquierda, 
    el resultado de n canicas sobre 12 columnas sera distribucion que tienda hacia la distribucion
    normal. 

    """
    x = np.random.randint(0, 2, n)
    pasos = x * 2 - 1
    posicion = np.cumsum(pasos, axis=0)
    plt.hist(posicion,  edgecolor='black')

# La segunda funcion define las caracteristicas del grafico que se utiliza para mostrar los resultados
# de la simulacion


def grafica_dalton():
    """
    Funcion que da las caracteristicas del histograma respecto a los datos obtenidos 
    en la funcion random_galton

    """
    plt.xlabel('Numero de columnas')
    plt.ylabel('Numero de canicas')
    plt.title('Simulador Maquina de Galton')
    plt.show()


# En esta seccion se llaman las funciones

random_galton(pasos)
grafica_dalton()

# Fin del programa
