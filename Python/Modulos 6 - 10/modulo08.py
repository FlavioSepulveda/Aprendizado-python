# MODULO 08 - Estruturas condicionais

# If  e Else -
'''
    As estruturas condicionais são esttruturas que vão executar um codigo dependendo do resultado de uma expressão.
    # Os operadores são:
    # Igual a: a == b
    # Difefrente de: a != b
    # Menor que: a < b
    # Menor ou igual a: a <= b
    # Maior que: a > b
    # Maior ou igual a: a >= b
'''
a = 33
b = 200

# Estrutura condicional;
# Se B for maior que a:
if b > a:
    print('B é maior que A.') # Deve sempre haver uma identação de tabulação que é um espaço de 4 caracteres
    print('Outra instrução no if.')
elif a == b: # Similar ao else if
    print('Sim, A é igual a B.')
elif a + 150 != b: # Similar ao else if
    print('A é diferente de B.') # o programa não executa essa por parar na primeira execução verdadeira.
else: # Executa se nenhuma for verdadeira
    print('Todas as verificações anteriores são falsas.')
# podemos tter quantos elifs forem nescessarios no programa e durante sua execução.
print('Fim da Execução.')

# Short Hand If Else -

# Operadores lógicos -

# Estruturas condicionais aninhadas -

# A declaração de passagem -