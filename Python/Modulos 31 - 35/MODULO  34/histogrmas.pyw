# Histogramas
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250) # gera um array com valores de ponto flutuante aleatorios
plt.hist(x)

plt.show()

