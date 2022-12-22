# Modulo m_area(m_area.py)
"""Modulo que contiene la funcion area"""


def area(**dato):
    """
    Recibe como parametro un diccionario con los datos de una figura
    Calcula el area de la figura
    """
    if dato['figura'] == 'Rectangulo':
        return(dato['base']*dato['altura'])
    elif dato['figura'] == 'Triangulo':
        return(dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        return(3.1415*dato['radio']**2)
    else:
        print('Figura desconocida')
