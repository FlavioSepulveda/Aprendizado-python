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