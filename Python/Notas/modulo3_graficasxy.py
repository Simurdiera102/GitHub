#Graficas de dispersion

from random import random


import random
import matplotlib.pyplot as plt

eje_x = [random.randint(1,100) for n in range(100)]

eje_y = [random.randint(1,100) for n in range(100)]

plt.scatter(eje_x, eje_y)

plt.tittle('Grafica de dispersion')

plt.show()
