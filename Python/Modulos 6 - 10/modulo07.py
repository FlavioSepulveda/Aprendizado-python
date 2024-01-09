# MODULO 07 - Coleções - DICTIONARY

# Dicionarios em python
'''
    # Os dicionarios assim como os dados do tipo set se encontram dentro de chaves, porem apresentando 2 informações sendo elas 'A chave' : 'O valor', sendo o valor separado de sua chave por dois pontos e de outras chaves com virgula.
    # Cada Key (Chave), Representa um valor dentro do dicionario.
    # Os Dicionarios não permitem itens duplicados.
'''
# Seguindo com um exemplo onde pegamos um personagem de anime pra apresentar ele.
luffy = {
    'Anime' : 'One Piece',
    'Comida favorita' : 'Carne',
    'Nacionalidade' : 'Brasileiro'
}
# Os itens dentro de um dicionario podem ser de varios tipos, inclusive podem de numeros inteiros e float, inclusive eles podem ser utilizados como chaves. 

# Acesso a itens dentro dos dicionarios
zoro = {
    'Anime' : "One Piece",
    'Onde esta' : 'Perdido',
    'Comida Favorita': 'Pinga'
}


# Podemos pegar o valor de uma chave usando uma variavel para quardar um valor.
x = zoro['Anime']
print(x)
# Ira reproduzir o valor daquela chave.
# Outra forma é com o metodo get
print(zoro.get('Onde esta'))
# Podemos criar uma variavel e atribuir o get dentro dela.
z = zoro.get('Onde esta')

# O Método keys retorna todas as chaves na forma de uma lista
chaves = zoro.keys()
print(chaves)
# Qualquer alteração ira refletir na keys
# Exemplo:
zoro['Quantidade de espadas'] = 3
print(chaves)

# Método values
chaves = zoro.values()
print(chaves)

zoro['Altura'] = 1.90
print(chaves)

# Metodo itens - Retorna uma tupla
s = zoro.items()
print(s)
zoro['Altura'] = 1.95
print(s)
# Esse metodo mostra todas as alterações;
# Para checar a existencia de determinado item dentro do dicionario, usamos o metodo in.
# EXEMPLO -
if 'Comida Favorita' in zoro:
    print('Sim, ele gosta de cachaça.')

# Adição de itens dentro dos dicionarios

# Remoção de itens dentro dos dicionarios

# Percorrendo os dicionarios com loops

# Copiando dicionarios

# Aninhando dicionarios