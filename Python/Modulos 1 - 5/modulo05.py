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
# Para acessar um indice da tupla referenciando o indice dentro do print.
print(tupla2[1])    # Deve devolver o valor pure
# Podemos fazer isso por meio da indexação negativa assim como nas listas
print(tupla2[-1]) # Ira retornar o valor Feijão.
# Podemos acessar com base em intervalos.
print(tupla2[1:3]) # ira retornar Pure e carne, o ultimo valor é excluso
# Omitindo o indice inicial ele iniciara do primeiro e ira parar no indice final.
print(tupla2[:4]) 
# Desta mesma maneira podemos fazer com a indexação negativa e omitindo o ultimo indice tambem
print(tupla2[1:])       # O mitindo o ultimo item 
print(tupla2[-4:-1])    # Utilizando intervalo de indexação negativa 
print(tupla2[:-1])      # Omitindo o index negativo inicial
print(tupla2[-4:])      # Omitindo o index negativo final

# É Possivel verificar se um item esta dentro da tupla
print("Suco" in tupla2) # Ele ira retornar falso.

# Podemos criar condicionais mediante isso
if 'Suco' in tupla2:
    print('Sim, pertence a tupla.')
else:
    print('Não, não pertence a tupla.')

# Atualizar tuplas
tupla3 = ('Cachorro', 'Gato', 'Passarinho', 'Borboleta')
# A tuplas não podem ser alteradas, mas podemos fazer outras coisas
# Podemos converter a tupla em lista e logo apos em tupla novamente
# da seguinte maneira:
print(tupla3)
# tupla_3 = list(tupla3) # Convertendo a gambiarra em tupla
# tupla_3[1] = 'Leão'
# tupla3 = tuple(tupla_3)
# print(tupla3)
#  Podemos utilizar o metodo append utilizando a mesma gambiarra anterior
# tupla_3 = list(tupla3)
# tupla_3.append("Formiga")
# tupla3 = tuple(tupla_3)
# print(tupla3)

# Uma alternativa de adição
tupla_3 = ('Lemori',)
tupla3 += tupla3
print(tupla3)

# Na tupla podemos remover itens utilizando a conversão de tupla em lista para modificar-la
tupla = list(tupla3)
tupla.remove("Cachorro")
tupla3 = tuple(tupla)

print(tupla)
# Podemos remover com o método del

del tupla3
# print(tupla3)

# Descompactando tuplas
tupla4 = ('Maçã', 'Banana', 'Uva', 'Abacaxi') # A forma que esta é chamada de compactada
print(tupla4)

(fruta1, fruta2, fruta3, fruta4) = tupla4 # Cada variavel ira receber um valor da tupla.

print(fruta1) # Imprime maçã
print(fruta2) # Imprime banana
print(fruta3) # Imprime Uva
print(fruta4) # Imprime abacaxi

'''
    No exemplo acima a descompactação da tupla ocorre com base na quantidade de variaveis que são apresentadas a ela.
    Para que seja feita a extração com menos valores, utilizamos um asterisco ( * ), para fazer a coleta de dados remanecentes e por em uma lista.
'''
#  Desta maneira
tuplaQuatro = ('Morango', 'Pessego', 'Goiaba', 'Laranja', 'Abacate')

(Fruta1, Fruta2, * Fruta3) = tuplaQuatro 

print(Fruta1) # Imprime Morango
print(Fruta2) # Imprime Pessego
print(Fruta3) # Imprime uma Lista com ['Goiaba','Laranja','Abacate']

# Loops atravez de uma tupla
tupla5 = ('HTML', 'CSS', 'JavaScript', 'Python')

# Juntar Tuplas 
tupla6 = ('Cavaleiro da Lua', 'Loki', 'Homem de ferro', 'Capitão America')
tupla7 = ('Constantine', 'Batman', 'Flash', 'Arqueiro Verde')