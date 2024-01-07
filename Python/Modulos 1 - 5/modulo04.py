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
'''
    Os indices das listas começam a partir do 0, assim como num array.
    tendo em vista isso podemos chamar o item de dentro da lista por meio de seu indice.
'''
# Chamando um indice

quarta_lista = ['Flavio', 'Ricardo', 'Gabriel']

# Caso eu queira ter acesso ao primeiro nome da lista 'Flavio', devo chamar pelo indice 0 da seguinte forma:
print(quarta_lista[0]) # Ira imprimir 'Flavio' no terminal.

'''
    *OBS.: Em python possuimos uma funcionalidade que permite a utilização de valores negativos, pois ao chamar por -1, por exemplo ele ira retornar o ultimo item da lista, que no caso do exemplo é 'Gabriel'. 
    Esta funcionalidade percorre a lista a partir do -1 Referenciando o ultimo item, de trás pra frente.
'''

print(quarta_lista[-1]) # Imprime gabriel no terminal.

# Criando um quinta lista de objetos domesticos:
quinta_lista = ['Colher', 'Tesoura', 'Prato', 'Geladeira', 'Ventilador', 'Relógio de parede', 'Livro']

# Com essa funcionalidade podemos acessar intervalos dentro da lista 
print(quinta_lista[2:5]) # acessando o indice 2 a 5 (Prato ate ventilador), o indice 5 é excluso
print(quinta_lista[:4]) # Podemos indicar desta maneira caso precise iniciar o indice 0
print(quinta_lista[3:]) # Podemos indicar que queremos ate o final da lista
# indexação negativa:
print(quinta_lista[-4:-1]) # Ele ira acessar de Geladeira a relogio relogio de parede, sempre excluindo o ultimo intem.

# LEMBRETE - Para checar se um item esta ou não dentro de uma lista, utilizamos o 'in'
if 'Colher' in quinta_lista:
    print('Sim, Colher esta na lista.') # Lembre-se, O python verifica letras maiusculas de minusculas
else:
    print('Não, colher não esta na lista.')

# Adicionando itens na lista
sexta_lista = ['Colher', 'Tesoura', 'Prato', 'Geladeira']

# Pra alterar o indice de um objeto
# primeiro referenciamos o indice e o novo valor dele
sexta_lista[0] = 'Garfo'
print(sexta_lista)
# Podemos alterar com base no intervalo
# sexta_lista[2:3] = ['Relógio de parede', 'Livro']
# print(sexta_lista)

sexta_lista[1:3] = ['Relógio de parede', 'Livro', 'Brinquedo'] # Ele vai adcionar mais um lugar na fila
print(sexta_lista)
print(len(sexta_lista)) # Vai printar 5 indices
# Quando temos apenas 1 valor ao imprimirla ele vai excluir
sexta_lista[1:4] = ['Livro']
print(sexta_lista)
print(len(sexta_lista)) # Vai printar 5 indices

# Para inserir valores na lista podemos utilizar do método insert
sexta_lista.insert(1, 'Garrafa') # Ele pede dois valores e os adiciona antes do indice estipulado.
# Isso sem alterar os itens da lista
print(sexta_lista)


# Remover itens da lista
# Primeiramente temos o metodo remove:
setima_lista = ['Carro', 'Moto', 'Avião', 'Caminhão'] # LISTA DE EXEMPLO
print(setima_lista)
setima_lista.remove('Carro') # Ele remove um valor de dentro da lista, caso seja uma string lembre-se letras maiusculas e minusculas fazem diferencia
print(setima_lista)
# Método pop
setima_lista.pop(1) # ele remove com base no index
print(setima_lista)

setima_lista.pop() # Quando sem o indice ele sempre irá remover o ultimo item da lista.
print(setima_lista)
#  Método del
del setima_lista[2]
print(setima_lista)
# Pro del apagar a lista inteira é so utilizar-lo sem indice porem causa um erro na execução do codigo.
# Para gerar uma execução sem erro e mantendo a existencia da lista, ao inves de utilizar o método del, utiliza-se o metodo clear.
setima_lista.clear()
print(setima_lista) # Ira imprimir uma lista vazia
# Utilização de loops com listas

'''
    A utilização de estruturas de repetição em uma lista.
    Podemos utilizar os tipos for e while.
'''
# Criando uma lista para o exemplo:
oitava_lista = ['Minecraft', 'League of legends', 'Undertale', 'Terraria']

# Primeiro caso com o loop for:

for x in oitava_lista:
    # Imprima o item que voce obter dentro de x.
    print(x)


# Utilizando o loop for para percorrer pelo indice usando as funções len e range
for i in range(len(oitava_lista)):
    print(oitava_lista[i]) # Quando mandamos imprimir desta maneira: (print(i)) ele ira imprimir o indice.

# Segundo caso com o loop while:
# Para utilizarmos o While precisamos de uma varivael auxiliar, onde nesse caso sempre usamos a variavel "i".
i = 0
while i > 4:
    print(oitava_lista[i])
    i = i + 1 # Usar *i += 1* irá resultar na mesma coisa.
print('Fim da execução 1.')

# Uso da compreensão de loops - Uma sintaxe mais simples que resulta  na mesma coisa.
[print(x) for x in oitava_lista] # Criando uma compreensão de listas pro loop for.

# Compreensão de listas

# Classificação de listas

# Copiando listas

# Juntando listas

