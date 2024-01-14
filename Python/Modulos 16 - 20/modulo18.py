# MODULO 18 - Matemática em Python
import math as mp
# O conjunto de funções matematicas do python
# Funções min e max
# Função min retorna o valor minimo
x = min(5, 10, 52, 89,100)
print(x)

# Funciona pra listas tbm
a = [7,15,25,32,4,18]
y = min(a)
print(y)
# Função max retorna o valor maximo
x = max(5, 10, 52, 89,100)
y = max([7,15,25,32,4,18])
print(x)
print(y)

# Função que retorna valores absolutos 
#  A função abs retorna o valor absoludo de um numero

x = abs(-7.25)
print(x)

# método pow
x = pow(4, 3) # mesmo que dizer 4 elevado a 3
print(x)
# Modulo matematico

# Pegando os metodos do modulo:
x = dir(mp)
print(x)
# Rais quadrada
raiz_quadrada = mp.sqrt(49)
print(raiz_quadrada)

# Arredondando valores pra cima
arredonde = mp.ceil(1.4)
print(arredonde)

# Arredondando valores pra baixo
arredonde2 = mp.floor(1.4)
print(arredonde2)

# Constantes matematicas
x = mp.pi
print(x)