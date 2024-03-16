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

# indexação de uma matriz no numpy

# arr = np.array([1,2,3,4])
# # print(arr[1]) # Se acessa o indice igual nas listas
# som = arr[1] + arr[2]  #deve imprimir 5
# print(som)

# # Matriz 2d acesso aos indices -
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # Temos que pensar em linhas e colunas -
# print(f'segundo elemento da 1° linha é: {arr[0,1]}')
# nomeDoArray[numeroDaLinha, indexDoValor]

# Matriz 3D
# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0, 1, 2])

# Ele permite a indexação negativa
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # Para acessar o numero 10 podemos determinar um valor negativo apos determinar em qual linha ele se encontra
# print(arr[1,-1])

# # fatiamento de matrizes -
# arr = np.array([1,2,3,4,5,6,7])
# # O fatiamento é realizado apresentando o inicio da fatia e o ate onde ela vai 
# # exemplo:
# '''
#     array = np.array([1,2,3,4,5,6,7])
    
# > Para fatiar fazemos assim:
# array[inicio da fatia:final da fatia]
# '''
# # Fatiamento normal -
# print(arr[1:5])
# # Fatiamento sem indice inicial -
# print(arr[:4])
# # Fatiamento sem indice final -
# print(arr[1:])
# # Fatiamento negativo normal -
# print(arr[-4:-1])
# # Fatiamento negativo sem indice final -
# print(arr[:-1])
# # Fatiamento negativo sem indice inicial -
# print(arr[-4:])
# # Fatiamento com salto de 2 -
# print(arr[1:5:2])
# # Fatiando com salto de 2 sem dois indices iniciais;
# print(arr[::2])


# # Fatiando Matrizes do tipo 2d -
# arr = np.array([[1,2,3], [4,5,6]])

# # fatia norrmal -
# print(arr[1, 1:4])
# print(arr[0:2, 2])
# # Podemos pegar o fatiamento das duas linhas da seguinte maneira -
# print(arr[0:2, 1:4])

# Tipos de dados no Numpy

# arr = np.array([1,2,3,4,5,6,7], dtype='S')
arr = np.array([1,2,3,4,5,6,7], dtype='i4')
arr2 = np.array(['maçã', 'banana', 'cereja'])
# arr3 = np.array(['a', '2', '3'], dtype='i')

# Gerando um erro que so é gerado ao receber um valor inesperado dentro do array.
# print(arr3.dtype) 
print(arr.dtype)
print(arr2.dtype)

# No python existem apenas os seguintes tipos de dados:
# strings, inteiros, float, boleanos e complex

# No numpy temos:
'''
    i = inteiro
    b = boolean
    u = inteiro sem sinal
    f = float
    c = float (complex)
    m = timedelta
    M = Data  Hora
    O = objeto
    S = String
    U = Sequencia Unicode
    V = Pedaço fixo de memoria para outro tipo (void)
    * A propriedade dtype retorna o tipo de dado presente no array
'''

# convertendo o tipo de matriz para outro
# isso so pode ser feito criando uma copia da matriz

arrConv = np.array([1.1, 2.1, 3.1])
novoArr = arrConv.astype('i')

print(arrConv)
print(novoArr.dtype)
print(novoArr)


# Array booleano =

arrBool = np.array([1, 0, 3])

novoArr2 = arrBool.astype(bool)

print(arrBool)
print(arrBool.dtype)

print(novoArr2.dtype)
print(novoArr2)
