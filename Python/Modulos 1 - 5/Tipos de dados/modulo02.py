#Importando modulos
import random

# MODULO 02 - TIPOS DE DADOS
'''
    Anteriormente falei sobre a utilização e os tipos de casting, e oque cada método apresente.
    Então recapitulando os tipos de dados que apresentei lá:
'''

# Tipos de dado Textual - str (String)
# Tipos de dado numérico - int, float, complex(novo)

# --------------------------------------------------

# Os novos que vou apresentar são:
# Tipos de dados de sequencia - list, tuple, range
# Tipos de dados de mapeamento - dict
# Tipos de dados de conjunto - set, frozenset
# Tipos de dados boleanos - bool (Verdadeiro ou Falso/True ou False/1 ou 0)
# Tipos binarios - Bytes, Bytearray, Memoryview

# Para definir e exemplificar cada tipo de dado:

var1 =  'Hello World' # Tipo String (str)

var2 = 20             # Tipo inteiro (int)
var3 = 20.5           # Tipo float (float)
var4 = 1j             # Tipo complex

var5 = ['maca', 'banana', 'cereja'] # Tipo de sequencia - lista
var6 = ('maca', 'banana', 'cereja') # Tipo de sequencia - Tupla
var7 = range(3) # Tipo de sequencia - Range

var8 = {"Nome": "Jhon", "Idade" : 36} # Tipo de mapeamento - Dict

var9 = {"Banana", "maca", "Cereja"}  # Tipos de conjunto - Set
var10 = frozenset({'banana', 'maca', 'cereja'}) # Tipo de conjunto - Frozenset

var11 = True                 # Tipo boolean

var12 = b"range"             # Tipo byte
var13 = bytearray(5)         # Tipo Bytearray
var14 = memoryview(bytes(5)) # Tipo memoryview

# CONFIGURAÇÃO DE TIPOS DE DADOS ESPECIFICOS:
# Casting dos tipos de dados:

var1 = str('Hello World') # Tipo String (str)
var2 = int(20)             # Tipo inteiro (int)
var3 = float(20.5)           # Tipo float (float)
var4 = complex(1j)             # Tipo complex

var5 = list(['maca', 'banana', 'cereja']) # Tipo de sequencia - lista
var6 = tuple(('maca', 'banana', 'cereja')) # Tipo de sequencia - Tupla
var7 = range(3) # Tipo de sequencia - Range

var8 = dict(Nome = "Jhon", Idade = 36) # Tipo de mapeamento - Dict

var9 = set(("Banana", "maca", "Cereja"))  # Tipos de conjunto - Set
var10 = frozenset(('banana', 'maca', 'cereja')) # Tipo de conjunto - Frozenset

var11 = bool(5)                 # Tipo boolean

var12 = bytes(5)             # Tipo byte
var13 = bytearray(5)         # Tipo Bytearray
var14 = memoryview(bytes(5)) # Tipo memoryview

# Estas funções a cima servem para configurar tipos especificos;

# Exemplos -
teste1 = '20'       # Tipo de dado string
print(teste1)
print(type(teste1)) # retornando o tipo de dado da variavel acima


teste2 = 20         # Tipo de dado inteiro
print(teste2)
print(type(teste2)) # retornando o tipo de dado da variavel acima

'''
    Tipos numericos e manipulações deles -
    int - float - complex
'''
# Variavel do tipo inteiro -

a = 1
b = 6589085832690
c = -1342

print(type(a)) # A variavel A é  do tipo inteiro
print(type(b)) # A Variavel B é  do tipo inteiro
print(type(c)) # A Variavel C é  do tipo inteiro

# Variavel do tipo float -

d = 1.10
e = 1.0293029
f = -39.279201
g = 35e3 # O e maiusculo ou minusculo significa notação cientifica
h = 12E4 # O e maiusculo ou minusculo significa notação cientifica

print(type(d)) # A variavel D é  do tipo float
print(type(e)) # A Variavel E é  do tipo float
print(type(f)) # A Variavel F é  do tipo float
print(type(g)) # A Variavel G é  do tipo float
print(type(h)) # A Variavel H é  do tipo float

# Variaveis do tipo complex -

i = 3+5j # Este j evidencia a existencia de um numero complexo
j = 5j
l =-5j

print(type(i)) # A Variavel I é  do tipo complex
print(type(j)) # A Variavel J é  do tipo complex
print(type(l)) # A Variavel L é  do tipo complex

'''
    Podemos converter os tipos de numericos utilizando as funções
    int - float - complex
'''

# Convertendo de inteiro pra float
exemplo1 = float(1)
# Convertendo de float pra int
exemplo2 = int(2.8)
# Convertendo de float pra complex
exemplo3 = complex(exemplo2)

print(type(exemplo1))
print(type(exemplo2))
print(type(exemplo3))

# OBS.: Não é possivel converter números complexos para outros tipos apenas de outros tipos para complexos.

# Gerando numeros aleatorios em python, com a importação da biblioteca random
num = random.randrange(1, 10) # Gera um numero aleatorio entre 1 e 10

print(num)
# Este modulo pode ser chamado dentro do metodo print tambem;

print(random.randrange(1, 20)) # Gera um numero aleatorio entre 1 e 20
print('\n') # caractere de escape - gera uma quebra de linha


# Cating 2.0
# Ato de converter/definir tipos de dados 
# Os tipos de dados e tipos primitivos em python podem ser modificados com os construtores.

# int() - Constroi um numero inteiro a partir de um literal inteiro, um literal inteiro, um literal flutuante (removendo todos os decimais) ou um literal de string (desde que a string represente um numero inteiro).

# float() - Constroi um numero flutuante a partir de um literal flutuante ou um literal de string(desde que a string represent um flutuante ou um inteiro)

# str() - Cosntroi uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais innteiros e literais flutuantes.

# EXEMPLOS 01:
variavel_ex1 = int(1)   # Resultado é 1
variavel_ex2 = int(2.4) # Resultado é 2
variavel_ex3 = int('3') # Resultado é 3

print(variavel_ex1)
print(variavel_ex2)
print(variavel_ex3)


# EXEMPLOS 01:
variavel_ex4 = float(1)   # Resultado é 1.0
variavel_ex5 = float(2.4) # Resultado é 2.4
variavel_ex6 = float('3') # Resultado é 3

print(variavel_ex4)
print(variavel_ex5)
print(variavel_ex6)


# EXEMPLOS 01:
variavel_ex7 = str('1s')   # Resultado é 1
variavel_ex8 = str(2.4) # Resultado é 2
variavel_ex9 = str('3') # Resultado é 3

print(type(variavel_ex7))
print(type(variavel_ex8))
print(type(variavel_ex9))



