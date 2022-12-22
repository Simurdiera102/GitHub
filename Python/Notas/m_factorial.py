# Modulo m_factorial(m_factorial.py)

""" Modulo que contiene la funcion recursiva del factorial"""


def factorial(num):
    """Calcular el factorial de un numero"""

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
