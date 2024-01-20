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
encontre = re.search("Õ.*Miguel$", txt) # Neste caso o retorno é negativo para o inicio e para o fim da string.
if encontre:
    print('Sim, Encontrei uma sequencia equivalente.')
else:
    print('Não, não existe correspondencia alguma.')