import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(0, 1.0, 1000)

plt.hist(datos)
plt.show()
