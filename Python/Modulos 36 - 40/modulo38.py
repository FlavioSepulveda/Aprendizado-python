# MODULO 38 - Módulo Python NumPy ufuncs (Funções Universais)
import numpy as np

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

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
# Adição -
newarr = np.add(arr1, arr2)
print(newarr)
# Subtração -
newarr = np.subtract(arr1, arr2)
print(newarr)
# Multiplicação -
newarr = np.multiply(arr1, arr2)
print(newarr)
# Divisão -
newarr = np.divide(arr1, arr2)
print(newarr)
# Potencia -
newarr = np.power(arr1, arr2)
print(newarr)
# Resto -
newarr = np.mod(arr1, arr2)
print(newarr)
newarr = np.remainder(arr1, arr2)
print(newarr)
# Quociente e Módulo -
newarr = np.divmod(arr1, arr2)
print(newarr)
# Absolute e ABS-
# Recomendavel usar o Absolute pra evitar conflito com o abs do math do python.
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
# Evitar confusão com o "abs" do math
newarr = np.abs(arr)
print(newarr)

print('#####################################################################################')


x = np.array([10,11,12,13,14,15])
y = np.array([20,21,22,23,24,25])

z = np.add(x,y, where=x>12)
print(z)