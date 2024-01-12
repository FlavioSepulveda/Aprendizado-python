# MODULOS 12 - Arrays e Coleções de Dados

# No python não temos suporte para arrays, então usamos listas em seu lugar:
cars = ['Ford', 'Volvo', 'BMW']
print(cars)

# Para acessar um item numa matriz usamos um indice
x = cars[0]
print(x)
# Ele ira imprimir 'Ford'

# Para trocar o valor funciona assim;
cars[0] = 'Toyota'
print(cars)

# Para saber o tamanho do array:
print(len(cars))

# Trabalhando listas como arrays:
comidas = ['Uva', 'Goiaba', 'Morango']

for x in comidas:
    print(x)

# Adicionando itens.
# Usamos o metodo append:
    comidas.append('Abacaxi')
# Em algumas linguagens não se é permitido modificar arrays, ja no python é pelo simples fato dele ser uma lista;
    
comidas.pop(1) # Vai remover o valor do indice 1.
comidas.remove('Uva') # remove um item pelo nome e não pelo indice.
