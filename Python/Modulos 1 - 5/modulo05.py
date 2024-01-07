# MODULO 05 - Coleções - TUPLAS
# Tuplas python - Regras

# As tuplas são usadas para armaenar varios itens em uma so variavel, uma tupla é um dos 4 tipos de dados do python referentes a coleções de dados.
# Uma tupla é uma coleção de dado imutavel escrita entre parenteses.
tupla1 = ('X-man', 'Vingadores', 'Iluminati', 'Shield')

# Para ser sonsiderada uma tupla, é preciso conter um item seguido de virgula.
# Podem ser chamadas da mesma maneira que as listas.
print(tupla1)
# São itens indexados, e a ordem de itens dentro ddelas é imutavel.
# Elas permitem itens duplicados, pois apenas os itens são duplicados, o indice continua o mesmo.
print(len(tupla1)) # Verificando quantos itens tem na tupla
# Verificando o tipo de dado
print(type(tupla1))
# Podemos criar uma tupla com apenas um item da seguinte maneira:
exTupla = ('Liga da justiça',)  #   Esta é uma tupla pois contem uma virgula.
exTupla2 = ('Liga da justiça')  #   Esta não é uma tupla pois não contem virgula para separar itens logo o proprio python classifica como uma string.

# Verificando o tipo
print(type(exTupla))      #   Retorna Class - tuple
print(type(exTupla2))     #   Retorna Class - string

# Podemos ter tuplas de varios tipos de dados, com strings, com numeros float, com strings ou ate mesmo valores booleanos.

# O python as define como objetos de tipo 'tuple' - Tupla
# Podemos usar o construtor Tuple pra criar uma tupla
exTupla3 = tuple(('Maçã', 'banana'))
print(exTupla3)
print(type(exTupla3))


# Acessando itens de uma tupla
tupla2 = ('Arroz', 'Pure', 'Carne', 'Feijão')

# Atualizar tuplas
tupla3 = ('Cachorro', 'Gato', 'Passarinho', 'Borboleta')

# Descompactando tuplas
tupla4 = ('Maçã', 'Banana', 'Uva', 'Abacaxi')

# Loops atravez de uma tupla
tupla5 = ('HTML', 'CSS', 'JavaScript', 'Python')

# Juntar Tuplas 
tupla6 = ('Cavaleiro da Lua', 'Loki', 'Homem de ferro', 'Capitão America')
tupla7 = ('Constantine', 'Batman', 'Flash', 'Arqueiro Verde')