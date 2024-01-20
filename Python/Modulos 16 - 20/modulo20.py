# MODULO 19 - RegEx (Expressões Regulares) em Python
'''
    Os RegEx são expressões que permitem a localização de padrões de pesquisa dentro de strings codigos ou afins, servindo tambem para validação de emails, numeros telefonicos e numeros de cpf, as regex tambem conhecidas como Expressões regulares, em python são trabalhadas com a utilização da biblioteca RE.
'''
# Importando módulo nescessario.
import re

txt = "O Gabriel amigo do Miguel"

# Verificando se a string começa com O e termina com migel.
# Método search

encontre = re.search("^O.*Miguel$", txt)
# print(encontre)
# Verificando se essa correspondencia existe dentro de um if
if encontre:
    print('Foi encontrada uma correspondencia.')
else:
    print('Nenhuma correspondencia foi encontrada.')
    
# Exemplo 2 - Método search.
txt2 = "A Gabriela é amiga de Miguel?"
encontre = re.search("^O.*Miguel$", txt) # Neste caso o retorno é negativo para o inicio e para o fim da string.
if encontre:
    print('Sim, Encontrei uma sequencia equivalente.')
else:
    print('Não, não existe correspondencia alguma.')
    
# A função search busca uma correspondencia dentro de um objeto especifico, se houver mais de uma correspondencia ela retorna apenas a primeira a ser encontrada.

txt3 = "O calor do motor da moto."
x = re.search("\s", txt3)
# O "\s" localiza espaços em branco dentro da string.
print(f'O primeiro espaço em branco esta na posição: {x.start()}')
# Buscando o nome brasil dentro da string:
x = re.search("Brasil", txt3)
print(x)
# Método Search - Pesquise("Correspondencia", String)

# Função findall - Ela retorna uma lista com todas as correspodencias encontradas dentro de uma string.
txt4 = 'O calor do motor da moto'

# Este metodo retorna um objeto que guadamos numa variavel que nesse caso é y
y = re.findall("or", txt4)

print(y) # Retornará uma lista com todas as correspondencias.
# Se nenhumma for encontrada ele retorna uma lista vazia... Por Exemplo
z = re.findall("ar", txt4)
# print(z)
if z:
    print("Sim existe correspondencia.")
else:
    print("Não existe correspondencia.")
    
# Função split - Retorna uma lista onde a string foi dividida em cada correspondencia encontrada.

txt5 = "O calor do motor da moto"

corr = re.split("\s",txt5) # Ao colocarmos um 3° parametro, numerico ele ira separar de acordo com a quantidade de ocorrencias.
print(corr)

# 