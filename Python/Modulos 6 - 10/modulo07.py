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

# Alteração de itens dentro dos dicionarios
nami = {
    'Anime' : 'One Piece',
    'Alcunha' : 'Gata Ladra',
    'Comida Favorita' : 'Laranja'
}

# Para alterar valores podemos fazer da seguinte forma:
nami['Anime'] = 'One piece'
print(nami)

# Podemos modificar com objetos diferentes com o metodo update como o metodo interavel.
nami.update({'Arco' : 'Arlong Park'})
print(nami)
# Adição de itens dentro dos dicionarios
# Podemos adicionar chaves da mesma maneira que adcionamos valores:

sanji = {
    'Anime': 'One Piece',
    'Ocupação': 'Pirata',
    'Arco': 'Baratier'
}
# Para adcionar fazemos da seguinte forma:
sanji['Cargo'] = 'Cozinheiro'
print(sanji)
# Ou podemos usar o método Update:
sanji.update({'Nacionalidade' : 'Frances'})
print(sanji)

# Remoção de itens dentro dos dicionarios
chopper = {
    'Anime':'One Piece',
    'Ocupação':'Pirata',
    'Arco':'Reino de drum'
}
# Para remover podemos fazer da seguinte maneira:
# Podemos usar o metodo pop - Pra remover com base no nome da chave;
# chopper.pop('Arco')
# O popitem remove o ultimo item, diferente do pop
# chopper.popitem()
# O método del remove de maneira parecida com o pop
del chopper['Anime'] # Se eu não passar a chave do item, a função del deleta o dicionario todo

# Para apenas limpar os valores, podemos usar o metodo clear.
chopper.clear()
print(chopper)


# Percorrendo os dicionarios com loops
# Agora vou usar outros exemplos chega de one piece.
livros = {
    'Investigação':'Sherlock Holmes',
    'Terror':'LoveCraft',
    'Misterio':'Biblioteca da Meia Noite'
}

# Percorrendo com o loop for
# for x in livros:
    # print(x) # Aqui ele so ira imprimir apenas as chaves.

# Da maneira correta fica assim:
for x in livros:
    print(livros[x])

# Podemos usar o metoso value
for x in livros.values():
    print(x)
# Podemos usar o metoso keys para retornar o nome das chaves:
for x in livros.keys():
    print(x)

# fazendo com o metodo items:
for x, y in livros.items():
    print(x,y)
# Copiando dicionarios
comidas = {
    'Doce':'Sorvete',
    'Salgado':'Lasanha'
}
# Para copiar usamos:
# Não podemos criar uma variavel e atribuir o dicionario.
# Devemos fazer da seguinte maneira:
comidas2 = comidas.copy()
print(comidas2)
# Podemos usar o construtor da classe pra criar o dicionario passando outro como parametro
comidas3 = dict(comidas)
print(comidas3)

# Aninhando dicionarios

# Um dicionario pode conter outros dicionarios;
myFamily = {
    'Filho 1': {
        'Nome':'Flavio',
        'Idade': 21
    },
    'Filho 2': {
        'Nome':'Ricardo',
        'Idade': 17
    },
    'Filho 3': {
        'Nome':'Pedro',
        'Idade': 21
    }
}

# Podemos criar dicionarios de fora e atribuir dentro de outros dicionarios:
Filho4 = {
        'Nome':'Gabriel',
        'Idade': 12
    }
Filho5 = {
        'Nome':'Marcos',
        'Idade': 20
    }
# Atribuindo esses valores a um dicionario;
myFamily2 = {
    'filho4' : Filho4,
    'filho5' : Filho5
}

print(myFamily)
print(myFamily2)