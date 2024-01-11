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
