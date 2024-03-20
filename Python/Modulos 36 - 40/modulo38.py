# MODULO 38 - Módulo Python NumPy ufuncs (Funções Universais)
import numpy as np
from math import log

# São funções universais que funcionama e são muito uteis na programação.
# A vetorização é permitida com as unfuncs;

# a = [1,2,3,4]
# b = [5,6,7,8]

# z = []

# for i, j in zip(a, b):
#     z.append(i+j)
    
# print(z)

# Fazendo com o numpy -
# a = [1,2,3,4]
# b = [5,6,7,8]

# z = np.append(a, b)
# print(z)


# Criando minha propria função universal -
# def myadd(x, y):
#     return x+y

# # O nome da função é determinado pelo nome da variavel.
# myadd = np.frompyfunc(myadd, 2, 1)

# x = [1,2,3,4]
# y = [5,6,7,8]

# z = myadd(x, y)
# print(z)
# print(type(np.add)) # Retorna uma unfunc
# print(type(np.concatenate))

# # Verificando se uma função é universal-

# if type(np.concatenate) == np.ufunc:
#     print('E uma ufunc')
# else:
#     print('Não não é')
    
# Aritimetica simples -
# Aritimetica condicional -
#  Parametro where especifica a situação.

# arr1 = np.array([10, 11, 12, 13, 14, 15])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# # Adição -
# newarr = np.add(arr1, arr2)
# print(newarr)
# # Subtração -
# newarr = np.subtract(arr1, arr2)
# print(newarr)
# # Multiplicação -
# newarr = np.multiply(arr1, arr2)
# print(newarr)
# # Divisão -
# newarr = np.divide(arr1, arr2)
# print(newarr)
# # Potencia -
# newarr = np.power(arr1, arr2)
# print(newarr)
# # Resto -
# newarr = np.mod(arr1, arr2)
# print(newarr)
# newarr = np.remainder(arr1, arr2)
# print(newarr)
# # Quociente e Módulo -
# newarr = np.divmod(arr1, arr2)
# print(newarr)
# # Absolute e ABS-
# # Recomendavel usar o Absolute pra evitar conflito com o abs do math do python.
# arr = np.array([-1, -2, 1, 2, 3, -4])
# newarr = np.absolute(arr)
# print(newarr)
# # Evitar confusão com o "abs" do math
# newarr = np.abs(arr)
# print(newarr)

# print('#####################################################################################')


# x = np.array([10,11,12,13,14,15])
# y = np.array([20,21,22,23,24,25])

# z = np.add(x,y, where=x>12)
# print(z)

# Arredondamento de decimais -
# Existem 5 Maneiras de arredondar com o numpy,e são as seguintes:

# Eles removem os decimais e devolvem a parte inteira.

# Truncated -
# arr = np.trunc([-3.1666, 3.6667])
# print(arr)

# # Fix -
# arr = np.fix([-3.1666, 3.6667])
# print(arr)

# # Around - Arredonda somando o ultimo digito
# arr = np.around([-3.1666, 2])
# print(arr)

# # Floor - Arredonda pro numero inteiro inferior mais proximo, retornando numeros de ponto flutuante.
# arr = np.floor([-3.1666, 3.6667])
# print(arr)

# # Ceil - Arredonda pro superior mais proximo.
# arr = np.ceil([-3.1666, 3.6667])
# print(arr)

# Log numpy
# Ele oferece funções para calculo de logaritimo na base 2 e na base 10

# OBS.: É possivel criar funções universais que irão fazer o calculo de logaritmos de qualquer base.

# arr = np.arange(1, 10) # Criando uma matriz de 1 a 9.
# print(arr)
# print(np.log2(arr))
# print(np.log10(arr))
# print(np.log(arr)) # log na base de todos os elementos

# # Defnindo uma função universal para qualquer base de logaritimo -
# nplog = np.frompyfunc(log, 2, 1)
# print(nplog(100, 15))

# Soma numpy -
# A diferença entre soma e adição...

# Adição (metodo 'add') é feita entre dois argumentos;
# Soma é feita em N argumentos.
# arr1 = np.array([1,2,3])
# arr2 = np.array([1,2,3])

# addArr = np.add(arr1, arr2)
# print(addArr)

# sumArr = np.sum([arr1, arr2]) # Ele soma os valores de todos os arrays 
# print(sumArr)
# sumArr = np.sum([arr1, arr2], 1) # Este um retorna a soma dos numeros em cada array
# print(sumArr)

# newarr = np.cumsum(arr1) # Retorna a soma acumulativa.
# print(newarr)

# Produtos de uma  matriz
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# # x=np.prod(arr)
# # x=np.prod([arr1, arr2]) # Ele vai retornar a multiplicação de todos os numeros dentro de cada matriz
# # x=np.prod([arr1, arr2], axis=1) # Retorna o produto dos elementos de cada matriz.

# x = np.cumprod(arr1)
# newarr = np.cumprod(arr2)

# print(x)
# print(newarr)

# 