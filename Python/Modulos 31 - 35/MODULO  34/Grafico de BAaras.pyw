# Grafico de dispersão
import matplotlib.pyplot as plt
import numpy as np


x = ['Carros', 'Motos', 'Bicicletas', 'Onibus']
y = [3, 8, 1, 10]
plt.title('Veiculos')
# plt.bar(x, y)
# plt.barh(x, y)
# cor = ['blue', 'red', 'green', 'hotpink'] -> Funciona desta maneira tambem
# Cor da barra -
# plt.barh(x, y, color=cor)
# Largura e altura das barras -
plt.bar(x, y, width=0.1) # height se for o barh


plt.show() 