# # MODULO 37 - Módulo Python NumPy.Random

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# # Gerando numeros aleatorios com numpy.

# # Aleatorio - Algo que não pode ser previsto logicamente
# x = random.randint(100)
# y = random.rand()  # Gera um numero float entre 0 e 1
# print(x)
# print(y)

# # Gerando Matriz aleatoria -
# # Gera uma matriz aleatoria de 5 elementos
# matriz = random.randint(100, size=(3, 5))
# # Podemos modificar da seguinte maneira (numero de matrizes, numero de elementos dentro das matrizes)
# matriz2 = random.rand(3, 5)
# # Metodo choice escolhe um valor dentro de uma matriz
# matriz3 = random.choice([1, 2, 3, 4])
# # O choice tambem recebe o size
# matriz4 = random.choice([1, 2, 3, 4], size=(3, 5))


# print(matriz)
# print(matriz2)
# print(matriz3)
# print(matriz4)

# # Distribuição de dados aleatorios -
# # Gerando numeros aleatorios com base na probabilidade de valores predefinidos
# arr = [1, 2, 3, 4]
# prob = [0.1, 0.2, 0.6, 0.1]
# # A soma total das probabilidades deve dar 1.0
# proba = random.choice(arr, p=prob, size=100)

# proba2 = random.choice(arr, p=prob, size=(3, 2, 5))

# print(proba)
# print(proba2)
# # Permutaçoes - Embaralhar

# arr = np.array([1,2,3,4,5])
# random.shuffle(arr) # modifica o original

# print(arr)

# arr2 = random.permutation(arr) # retorna um novo array com os valores do original
# print(arr2)

# # Seaborn - plotagem de graficos
# # Derivado do matplotlib que funciona na plotagem de dados com matplotlib e pyploy em conjunto com numpy random

# # sns.displot([0, 1, 2, 3, 4, 5])
# # sns.distplot([0, 1, 2, 3, 4, 5], hist=False)


# # plt.show()

# # Distribuição gauciana -

# # Essa distribução se ajusta a coisas como batimentos cardiacos e medições de QI.

# # distribuicao = random.normal(loc=1, scale=2 ,size=(2,3))
# # dist = random.normal(size=(1000))

# # # print(distribuicao)
# # sns.distplot(dist, hist=False)
# # plt.show()

# # Distribuição binomial

# # Descreve aleatoriedade em cenarios onde ocorrem apenas 2 resultados tipo cara ou coroa
# # x = random.binomial(n=10, p=0.5, size=1000)
# # sns.distplot(x, hist=True, kde=False)
# # print(x)
# # plt.show()

# # a=random.normal(loc=50, scale=5, size=1000)
# # sns.distplot(a, hist=False, label='Normal')
# # b=random.binomial(n=100, p=0.5, size=1000)
# # sns.distplot(b, hist=False, label='Binomial')
# # plt.show()

# distribuição de poisson
# x = random.poisson(lam=2, size=1000) # poisson é mais discreta que as normal
# # print(x)
# sns.distplot(x, kde=False)
# plt.show()

# distNormal = random.normal(loc=50, scale=7, size=1000)
# sns.distplot(distNormal, hist=False,label="Normal")
# distPoisson = random.poisson(lam=50, size=1000)
# sns.distplot(distPoisson, hist=False, label='Poisson')
# distBinomial= random.binomial(n=1000, p=0.01, size=1000)
# sns.distplot(distBinomial, hist=False,label="Normal")
# plt.show()

# Distribuição uniforme -
# Usada para descrever a probabilidade de alguns fenomenos tem de acontecer

x = random.uniform(low=-1, high=0,size=1000)
sns.distplot(x, hist=False)
plt.show()