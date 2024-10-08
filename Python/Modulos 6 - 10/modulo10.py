# MODULO 10 - Funções Python
# Funções são blocos de codigos chamados sempre que as funções são chamadas

def myFunc():
    # Esta função escreve a mensagem abaixo na tela.
    print('Esta é minha primeira função.')

myFunc()
# Os parametros indicam oque a função recebe.
def myFunc2(nome):
    print('Ola', nome,' !')

myFunc2("Flavio")

# As funções retornam valores:
def myFunc3(x):
    return x * 5

resultado = myFunc3(2)
print(resultado)

# Parametros dentro da função;
def nomeCompleto(nome, sobrenome):
    print(nome + sobrenome)

nomeCompleto("Antonio", "Flavio") # A ordem dos parametros auteram os resultados.

# Criando uma func que cria uma lista que recebe uma tupla como parametro:
def listaNomes(*nomes):
    for x in nomes:
        print(x)

listaNomes('Gabriel', 'Danny', 'Arthur')
# Argumentos de palavra chave

def chamada(primeiro, segundo, terceiro):
    print('Este é o primeiro: ', primeiro)
    print('Este é o segundo: ', segundo)
    print('Este é o terceiro: ', terceiro)

# Quando passamos uma informação para uma função devemos passar os parametros na ordem correta a menos que usemos as keys de cada parametro.
chamada(terceiro='Gabriel', primeiro='Flavio', segundo='Ricardo')

# Quando não se sabe a quantidade de itens a função vai receber. Usa-se um dicionario.

def NomeCompleto(**nome):
    # print(nome)
    for x in nome.values():
        print(x)

NomeCompleto(pri='Gabriel', seg = 'Silva')

# Valor padrão de parametro:
def myFunc4(pais = 'Brasil'):
# Atribui-se o padrão com o sinal de igual logo apos o parametro.
    print('Eu sou do ' + pais)

myFunc4()

# Passando uma lista como argumento
def minhaFuncao(alimentos):
    for x in alimentos:
        print(x)

frutas = ['Maçã', 'Banana', 'Abacaxi']
# A lista pode ser repassada de forma literal tambem.
minhaFuncao(frutas)
# Utilização da Declaração de passagem numa função:

def miFuc():
    pass # Evitando erro de sintaxe.
print('Fim da execução.')    

# Função recursiva
# Quando uma função chama por ela mesma dentro de si:
# Sem recursividade
def repetir(n):
    for x in range(n):
        print('Ola, mundo.')

repetir(4)
# Com recursividade:
def repetirRecursive(n):
    if n > 0:
        print('Ola mundo.')
        repetirRecursive(n-1)

repetirRecursive(5)

# Funções lambda
# é uma função anonima que pode receber infinitos argumentos mas so retorna um resultado.
x = lambda a : a + 10

# Metodo de uso
result = x(5)
print(result)

# As expressoes lambda recebem qualquer numero de argumento so precisam se encontrar antes do dois pontos:

y = lambda a, b : a * b
print(y(5,2))

# Criando uma função que sempre duplica numeros que enviamos:
def myFunct(n):
    return lambda a: a * n

meuDuplicador = myFunct(2)

print(meuDuplicador(11))