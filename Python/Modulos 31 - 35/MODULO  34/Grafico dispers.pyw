# Grafico de dispersão
import matplotlib.pyplot as plt


cores = ['red', 'green', 'blue', 'black', 'hotpink','yellow', 'orange', 'pink', 'gray', 'brown', 'gold', 'purple', 'silver']

# Dia 1 - Idade e Velocidade de 13 carros
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y, c=cores)

# Dia 2 - Idade e Velocidade de 15 carros
x = [2,2,8,1,15,8,12,9,7,3,11,4,7,14,12]
y = [100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]
# plt.scatter(x, y, color='green')

# Função scatter -

plt.show() 