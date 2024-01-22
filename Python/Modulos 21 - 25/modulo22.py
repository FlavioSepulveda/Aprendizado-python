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
    print('Tudo certo por aqui.')
finally:
    print('O try except foi finalizado.')
# o finally executa dequalquer forma dentro do bloco de codigos

# Os except são executados para erros em especifico, mas podemos usar um else pra executar algo fora do try.

print('Continuando o programa.')