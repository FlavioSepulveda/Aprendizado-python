# Módulo 08 - Estruturas Condicionais

# Estruturas Condicionais:
'''
    Executam código baseado no resultado de uma expressão.
    Operadores: 
    ==, !=, <, <=, >, >=
'''

# Variáveis de exemplo:
a = 33
b = 200

# If e Else:
if b > a:
    print('B é maior que A.')
    print('Outra instrução no if.')
elif a == b:
    print('A é igual a B.')
elif a + 150 != b:
    print('A é diferente de B.')
else:
    print('Todas as verificações anteriores são falsas.')
print('Fim da Execução.')

# Short Hand If Else:
a = 200
b = 50

# If em uma linha:
if a > b: print('A é maior que B.')

# Else em uma linha:
print("A") if a < b else print("B")

# Operadores Ternários:
print(" a ") if a < b else print(" = ") if a == b else print(" b ")

# Operadores Lógicos - and e or:
a = 200
b = 33
c = 500

# Este operador retorna verdadeiro quando todas as condições são verdade.
if a > b and c > a:
    print('A é maior que B.')
    print('E C é maior que A.')

# Este operador retorna verdadeiro quando uma das condições são verdade.
if a < b or c > a:
    print("Pelo menos uma é verdadeira.")

# Estruturas Condicionais Aninhadas:
# Declaração 'pass':
# Evita erros de sintaxe em estruturas ainda não implementadas.
