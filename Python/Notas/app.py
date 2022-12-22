from m_area import area as a
import m_area as ma

# modulo.nombre #Permite llamar un parametro de un modulo
# from modulo1 import objeto1 #Permite importar un objeto de un modulo
import m_factorial2 as mf

fact5 = mf.factorial(5)
print(f'El factorial de 5 es: {fact5}')


area = a(figura='Triangulo', base=10, altura=8)
print(f'El area del triangulo es: {area}')
