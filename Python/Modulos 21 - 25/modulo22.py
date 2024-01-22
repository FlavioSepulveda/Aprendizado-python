# MODULO 22 - Manipulação de erros ou exceção
# 
# Tratamentos de exceção
# x = 'ola mundo.'

# A variavel não estando definida deve gerar um erro e qualquer codigo abaixo não ira continuar.
try:
    print(x)
except:
    print('Significo exceção')

print('Continuando o programa.')
# O bloco try trata qualquer erro de código
# Podemos executar multiplas exceções definidas para tipos de erros diferentes
y = "ola mundo"
try:
    print(y)
except NameError:
    print('Variavel inexistente.')
except:
    print('Significo exceção')
else:
    # Os except são executados para erros em especifico, mas podemos usar um else pra executar algo fora do try.
    print('Tudo certo por aqui.')
finally:
    # o finally executa dequalquer forma dentro do bloco de codigos
    print('O try except foi finalizado.')

# Gerando uma exceção

x = 5
# criando uma exceção/lançando uma exceção - métoddo raise
if x < 0:
    raise Exception('Numero invalido.')
# Exceções definidas
y1 = "Ola mundo"
if not type(y1) is int:
    raise TypeError("Somente numeros")

print('Fim do programa.')