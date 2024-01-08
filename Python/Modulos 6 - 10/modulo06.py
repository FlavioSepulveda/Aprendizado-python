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

# Adcionando itens do set

# Remover itens do set

# Loop Atraves de um set

# Juntando coleções do tipo set 