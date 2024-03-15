# MODULO 35 - Módulo  Python NumPy
import numpy as np

# # O numpy é uma biblioteca que visa o trabalho com arrays no python sendo melhor que as listas que visam ter um objetivo parecido com um array mas sendo mais lento, ja o numpy oferece uma velocidade 50x maior com o objeto 'nparray'

# # Ele serve para trabalhos com algebra linear em python por isso o nome NumPy

# # arr = np.array([1,2,3,4,5])
# # print(arr)

# # print(np.__version__)

# # Criação de matrizes -

# arr = np.array([1,2,3,4,5])
# # print(arr) # imprimindo o array na tela
# # print(type(arr)) # retorna um objeto <class 'numpy.ndarray'>
# # O array é uma matriz de dados
# #  As matrizes podem ser de varios tipos por terem mais de uma dimensão
# # A matriz 0-D apresenta apenas 1 valor fora de um array por isso o nome de matriz 0D
# # Exemplo de matriz 0-d:
# matriz0D = np.array(42)

# # A matriz 1-D possui um array de itens dentro de sua estrutura assim como o exemplo 'arr' la do inicio
# # Exemplo de matriz 1d:
# matriz1D = np.array([1,2,3,4])

# # Matriz 2d, é um array que dentro de si guardam arrays do tipo 1d, este tipo de matriz é usado para tabalhar com tensores de 2° ordem.
# # Exemplo de matriz 2d:
# matriz2D = np.array([[1,2,3], [4,5,6]])

# # Matrizes 3d, são comumente utilizados para representar tensores de 3° ordem
# # são representados da seguinte maneira:
# matriz3D = np.array(
#     [
#         [
#             [1, 2, 3], [4, 5, 6]
#             ], 
#         [
#             [1, 2, 3], [4, 5, 6]
#             ]
#         ]
#     )
# # print(matriz0D)
# # print(matriz1D)
# # print(matriz2D)
# # print(matriz3D)

# # print(type(matriz0D)) ->> Todas retornam: <class 'numpy.ndarray'> como tipo mas usamos o atributo ndim (number dimensions) para escrever qual o numero de dimensões da matriz na tela.
# # Exemplo do uso do ndim:
# # print(matriz0D.ndim)    # Retona 0 dimensões; 
# # print(matriz1D.ndim)    # Retona 1 dimensões;
# # print(matriz2D.ndim)    # Retona 2 dimensões;
# # print(matriz3D.ndim)    # Retona 3 dimensões;
 
# val = [1,2,3,4,5]
# e = np.array(val, ndmin=5) # ndmin é o numero minimo de dimensões. 

# print(f'O numero de dimensões presente na variavel "e" é de: {e.ndim}.')

