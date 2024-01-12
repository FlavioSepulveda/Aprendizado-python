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