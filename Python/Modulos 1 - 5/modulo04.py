# MODULO 04 - Coleções - LISTAS

# Listas são dados do tipo coleção de dados, mas ainda sendo objetos deste tipo, elas obedecem algumas regras basicas para existir.

# REGRA NUMERO 1 - As listas são criadas dentro de colchetes.
# Ex.: lista = ['exemplo1', 'exemplo2', 'exemplo3']
# REGRA NUMERO 2 - Cada item da lista é separado por virgula, e entre aspas simples quando se for uma string.

'''
    Observações -
    * Nas listas os itens são: Mutaveis e é permitido valores duplicados.
    * As listas são indexadas ou seja os itens dentro dela obedecem a contagem que começa a partir do 0.
    * Apos a criação da lista a ordem dos itens dentro do indice não pode ser alterada.
'''

primeira_lista = ['Bolo', 'Lasanha', 'Cafe']

print(primeira_lista)
# Para saber o comprimento da lista usamos a função len
print(len(primeira_lista)) # Esta lista tem 3 itens

# As listas podem ser de varios tipos por exemplo itens inteiros:
segunda_lista = [1, 2, 3, 4]

print(segunda_lista)
print(len(segunda_lista)) # Esta lista tem 4 itens
# Acessando itens da lista
# Usando a função type podemos ver que a classe das listas é 'list'
print(type(segunda_lista))

# Método construtor de listas;
# O método list()
terceira_lista = list(('Sherlock Holmes', 'H.P Lovecraft', 'Edgar Alan Poe'))
print(terceira_lista)

# Alterando itens da lista

# Adicionando itens na lista

# Remover itens da lista

# Utilização de loops com listas

# Compreensão de listas

# Classificação de listas

# Copiando listas

# Juntando listas

# 