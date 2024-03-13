# mapa de cores
import matplotlib.pyplot as plt

# Dia 1 - Idade e Velocidade de 13 carros
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

cores = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]
plt.scatter(x, y, c=cores, cmap='Blues_r')
plt.colorbar()

plt.show() 