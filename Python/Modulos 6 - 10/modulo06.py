# MODULO 06 - Coleções - SET

# Set Python -
'''
    Os dados de tipo set são usadas pra armazenar dados assim com as dos tipos anteriores.
    Os Dados do tipo set não são Indexados e não são ordenados. 
    Os Dados do tipo set são escritos entre chaves.
'''
set1 = {'Flávio', 'Marcos', 'Samuel', 'Pedro'}

print(set1) # A ordem sempre muda ao chamar o mesmo item.
# Os dados dentro do set podem ser adcionados mas nao podem ser modificados ou duplicados durante sua criação.
# Ele ignora os itens repetidos
print(len(set1)) # Podemos ter o tamanho do set
s2 = {1,2,3,4} # Podemos ter dados do tipo inteiro.
s2 = {True, False, True, False} # Podemos ter dados do tipo booleano.
s2 = {1,"ola",3.0,True} # Podemos ter dados Mesclados.

# Podemos usar o cosntrutor do tipo set para criar um set;
set2 = set(('Carro', 'Moto', 'Caminhão', 'Barco')) # Dois parenteses lembre-se
print(set2)

# Acessando os itens do set
'''
    Como os itens do Set não são indexados, posso percorrer ele usando um loop for ou usando o metodo in.
'''
set3 = {'Bolo', 'Café', 'Lasanha', 'Arroz'}
print(set3)

# Criando o loop for para percorrer um set

for x in set3:
    print(x)

print('Bolo' in set3) # Com o metodo in


# Adcionando itens do set
set4 = {'Liandri', 'Eco De Luden', 'Orb do Infinito'}
print(set4)

# Como o metodo append não funciona neste tipo, utilizamos um metodo add
set4.add('Runaan')
print(set4)

# Podemos juntar, mais um set no set anterior da seguinte maneira
set5 = {'Força do vendaval', 'Mata crakens'}
# O método update funciona pra mesclar sets
set4.update(set5)

print(set4)
# Pode ser qualquer tipo de uniao podendo ser com listas, tuplas ou dicionarios.

# Remover itens do set
set6 = {'Gato', 'Cachorro', 'Papagaio'}

# Para remover podemos usar o metoro remove da seguinte forma
# set6.remove('Papagaio')
print(set6)
# Este metodo quando não encontra o item referido ele gera um erro.

# Metodo discard
# set6.discard('Cachorro') # Este metodo quando não encontra o item referido ele não gera um erro.
print(set6)

# Método pop - Remove sempre o ultimo item do set
set6.pop()
print(x)
x = print(set6)

# Tambem podemos usar o metodo clear, porem ele apaga todos os itens do set.
# Tambem podemos usar o metodo del, porem ele apaga todo o set.

# Loop Atraves de um set

# Juntando coleções do tipo set 