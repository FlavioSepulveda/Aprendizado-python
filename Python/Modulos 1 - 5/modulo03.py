# MODULOS 03 - OPERADORES 

# Os operadores aritimeticos em python são responsaveis por realozar operações matematicas.

'''
    São eles:
    + - Operador de adição
    - - Operador de subtração
    * - Operador de multiplicação
    / - Operador de Divisão
    % - Operador de Modulo(Resto da divisão)
    // - Operador de Arredondamento de divisão
    ** - Operador de exponenciação
'''
# Exemplos:
a = 5
b = 2

# print(a + b) # Deve retornar 7
# print(a - b) # Deve retornar 3
# print(a * b) # Deve retornar 10
# print(a / b) # Deve retornar 2.5
# print(a % b) # Deve retornar 1
# print(a // b) # Deve retornar 2
# print(a ** b) # Deve retornar 25

# Operadores de atribuição
# O Sinal de igual é um operador de atribuição simples:
x = 5
y = 5
z = 5
w = 5
u = 5
v = 5
p = 5
print(x)
# Dentre os operadores de atribuição é tambem conhecido como operadores de incrmento e decremento:

x += 5 # É o mesmo que x = x + 5
print(x)
y -= 1 # É o mesmo que y = y - 1
print(y)
z *= 2 # É o mesmo que z = z * 2
print(z)
w /= 2 # É o mesmo que w = w / 2
print(w)
u %= 2 # É o mesmo que u = u % 2
print(u)
v //= 2 # É o mesmo que v = v // 2
print(v)
p **= 2 # É o mesmo que p = p ** 2
print(p) 

# Operadores de comparação
# Os operadores logicos trabalham dentro das logicas condicionais fazendo algo similar a uma pergunta:
# Por exemplo: Três é maior que cinco? (3 > 5)? 
'''
    Os operadores de comparação retornam valores booleanos - True/False.
    Estes operadores são comuns em estruturas condicionais (Ex.: if's, while...)
'''
# São utilizados para definir o fluxo de um programa por meio de condições.

# OS OPERADORES COMPARATIVOS SÃO:
_xx = 5 # Variavel 1
_yy = 3 # Variavel 2

# Exemplos:
# Operador de Igualdade:
print(_xx == _yy)

# Operador de Diferente de...
print(_xx != _yy)

# Operador Maior que...
print(_xx > _yy)

# Operador Menor que...
print(_xx < _yy)

# Operador Maior ou igual a...
print(_xx >= _yy)

# Operador Menor ou igual a...
print(_xx <= _yy)

# Operadores lógicos

'''
    Os operadores logicos funcionam combinando condições:
    and - Se as duas condições são duplamenta verdadeiras (Similar a porta logica "And");
    or - se uma condição ou outra é verdadeira (Similar a porta logica "ou");
'''
# EXEMPLOS:
xx = 5
print(x > 3 and 15 < 10) # As duas irão retornar falso pois o "And" retorna verdadeiro apenas quando as duas são verdadeiras.

# EXEMPLOS2:
print(x > 3 or x < 4) # Ele retorna verdadeiro quando pelo menos uma das expressoes retorna verdadeiro.

# Operador "Not" - Similar a porta logica "NOT":
print(not(x > 3 and 15 < 10)) # Ele ira inverter qualquer resultado booleano.
print(not(False)) # Ele ira inverter qualquer resultado booleano ate mesmo que seja direto.

# Operadores de identidade
# Verificam a identidade de um objeto.

# Exemplos
# Os objetos a baixo são objetos com o mesmo conteudo, mas com endereçamento diferente então, não são iguais.
xxx = ['maca', 'banana']
yyy = ['maca', 'banana']
# Já neste caso estamos atribuindo a um objeto um objeto criado anteriormente.
zzz = xxx

print(xxx is zzz) # Perguntando se "xxx" é "zzz", então o retorno sera true.
print(xxx is yyy) # Perguntando se "xxx" é "yyy", então o retorno sera false.
print(xxx == yyy) # Perguntando se "xxx" contem o mesmo conteudo e são do mesmo tipo de objeto "yyy", então o retorno sera true.

# Juntamente do "Is" temos o "Is not", ele verifica o contrario do "Is".
print(xxx is not zzz) # Perguntando se "xxx" não é "zzz", então o retorno sera false.
print(xxx is not yyy) # Perguntando se "xxx" não é "yyy", então o retorno sera true.
# Perguntando por meio de um operador de comparação se os objetos são iguais:
print(xxx != yyy) # Resulta false - por serem diferentes em endereço, mas iguais em questão de conteudo.

# Operadores de Associação
# São usados para checar se um valor é apresentado dentro de um objeto

objeto1 = ['maca', 'banana']
# objeto2 = []
# Operador "in" verifica se dentro do objeto está o valor que você procura.
print('banana' in objeto1) # Ele ira retornar verdadeiro porque banana esta dentro do objeto.

# Operador "not in" verifica se o valor não esta dentro do objeto.
print('banana' not in objeto1) # Irá resultar em false poque o valor existe dentro do objeto.
print('abacaxi' not in objeto1) # Irá resultar em true poque o valor não existe dentro do objeto.

# O mesmo funciona com numeros: 
_xxxx = [348, 45, 150]
print(34 in _xxxx)      # Nesta o retorno é falso porque este valor não existe dentro do objeto.
print(34 not in _xxxx)  # Nesta o retorno é verdadeiro, porque o valor não existe la dentro.