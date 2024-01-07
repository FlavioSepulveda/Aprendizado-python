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


# Remover itens da lista

# Utilização de loops com listas

# Compreensão de listas

# Classificação de listas

# Copiando listas

# Juntando listas

