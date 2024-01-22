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
