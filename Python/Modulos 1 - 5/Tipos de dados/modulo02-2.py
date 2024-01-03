# Strings

'''
    *String é um tipo de dado que representa uma cadeia de caracteres alfan numericos.
        -> Ela pode conter:
            - Letras
            - Numeros
            - Caracteres especiais
'''

# Em python as strings podem se encontrar de duas maneiras, dentre aspas simples ou duplas, da seguinte maneira:

a = "Meu nome é Flávio"
A = 'Meu apelido é Sunny'

# Ambas as maneiras estão corretas.
# Colocando a string entre 3 aspas simples ou 3 aspas duplas ela entende que é um texto a ser declarado como variavel, conforme o exemplo:

# O texto do exemplos esta presente no site lorem ipsum
b = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas est arcu, tempus at neque ut, tincidunt facilisis tortor. Aenean a mi in nisl dignissim condimentum placerat vitae turpis. Pellentesque ligula lorem, varius sit amet ipsum in, semper commodo quam. Aliquam augue nibh, ornare eget tortor at, semper dictum felis.'''

# O texto do exemplos esta presente no site lorem ipsum
B = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas est arcu, tempus at neque ut, tincidunt facilisis tortor. Aenean a mi in nisl dignissim condimentum placerat vitae turpis. Pellentesque ligula lorem, varius sit amet ipsum in, semper commodo quam. Aliquam augue nibh, ornare eget tortor at, semper dictum felis."""

# Estas strings a cima são strings multi lines.
# print(B)

# As strings de python são matrizes
# Para acessar caracteres individualmente dentro de uma string usamos colchetes (Brackets)

C = "Ola mundo!"

print(C)
 # Para utilizar o endereçamento dentro de strings, devemos lembrar que o indice de uma matriz começa em 0, logo quando quero acessar a letra "l" na string 'Ola mundo!', uso o indice 1 dentro dos colchetes.
# Espaços contam no indice tambem.
print(C[1])

# As strings são percorriveis pelo loop for, pois são arrays;

# Enquanto a string não chegar ao fim
for x in "Flavio":
    # Escreva as letras da mesma
    print(" - " + x + " - ")

# O metodo len busca e retorna ao usuario o tamanho de uma string
D = len(C)
# Imprimindo o a quantidade
print(D)

# Verificando se existe um caractere dentro da string
# Utiliza-se o metodo in

txt = 'Ola, meu nome é Antônio Fávio, muito prazer!' # Texto a ser verificado
var1 = 'muito' in txt                                # Fazendo a verificação com o uso da função in

print(var1)                                          # Demonstrando se a verificação é verdadeira ou falsa 
# Exemplo que resulta em falso:
print("Carro" in txt)

if 'meu' in txt:                # Se "Meu" estiver em txt
    print('Sim, esta presente') # Se "Meu" estiver dentro de txt, retorna a mensagem

# Verificando se não esta em txt:
if 'meu' not in txt:
    print("'meu', não esta em txt.") # Se "Meu" não estiver dentro de txt, retorna a mensagem

# FATIAMENTO DE STRINGS EM PYTHON
    '''
        O Fatiamento ocorre quando você traves de um determinado codigo pode tirar uma parte de uma string.
    ''' 
nome = "Antonio Flavio"     # Fatiando meu nome
print(nome[2:5])         # A criação de fatias funciona colocando o indice a ser fatiado dentro de colchetes 
# Pegando apenas o sobrenome:
print(nome[8:15])
# pegando do inicio
print(nome[:8])
# Pegando do meio ate o final
print(nome[8:])

# INDEXAÇÃO NEGATIVA É PERMITIDA;
print(nome[-5:-2])

# MODIFICAÇÃO DE STRINGS

sTeste = "Antonio Flavio"
teste2 = sTeste.upper() # O método upper coloca todas as letras em maiusculas

print(teste2) # Exibindo o exemplo

# Fazendo a mesma coisa so que tornando todos em minusculas
print(sTeste.lower())   # Exibindo resultados



sTeste2 = "  Antonio Flavio  "
print(">"+sTeste2.strip()+"<")  # Strip remove espaçamentos do inicio e fim