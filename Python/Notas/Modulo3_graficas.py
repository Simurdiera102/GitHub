import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0) #Numero pseudo aleatorio

numeros = np.random.rand(10) #Genera lista de 10 valores

np.random.normal(media_distribucion, desviacion_estandar, tamaño_muestras)

print(numeros)

plt.plot(numeros)
plt.show()
