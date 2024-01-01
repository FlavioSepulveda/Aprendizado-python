# MODULO 01 - VARIÁVEIS
'''
    Variáveis são espaços reservados dentro da memoria do computador para armazenar dados.
    Estes espaços iremos utilizar para a construção dos nossos programas e algoritimos.
'''

# As variaveis em python são criadas a partir do momento que atribuimos um valor a elas:
'''
    Para criar estas variaveis etribuimos a elas um nome e logo em seguida um valor.
    o valor é atribuido pelo sinal de igual (=) como operador de atribuição, conforme no exemplo:
    var1 = 1
'''

# Desta maneira seguindo o exemplo temos:
variavel1 = 1

# As variaveis podem guardar valores de texto, que são atribuidos atraves de aspas duplas e/ou aspas simples;
texto1 = 'Atribuição com aspas simples'
texto2 = "Atribuição com aspas duplas"

# Podemos chamar a variavel atravez do comando "Print", da seguinte forma:
print(texto1)

# Vale lembrar que as variaveis podem ter alterações no seu tipo:
# Por exemplo:
variavel2 = 3 # Esta variavel tem valor inteiro (int)

# Ela tem o valor inteiro, mas posso atribuir a ela qualquer valor de forma subsequente, desta maneira:
variavel2 = 7 # Este novo valor pode ser de qualquer tipo
variavel2 = "Agora é do tipo string"

'''
    A tipagem de dados pode ser feita por meio de casting;
    Casting é a mudança de tipagem de um objeto por meio de uma tecnica de conversão;
    Tomando o exemplo da primeira variavel:
    # var1 = 1 
    Para fazer o casting, é preciso o nome da variavel, e atribuir um tipo a ela da seguinte maneira
    # var1 = int(1) # Assim o python vai ler o valor como um valor do tipo "int", inteiro.
'''


# O mesmo valor possui varias formas de se apresentar:
variavel3 = "3" # Este tres é uma string, pois esta entre aspas.
variavel3 = 3   # Este tres é um valor inteiro, pois esta fora das aspas e sem ponto flutuante
variavel3 = 3.0 # Este tres é um valor decimal, pois apresenta o ponto flutuante.

'''
    OS VALORES DO CASTING SÃO:
    str - Para valores de texto, Strings.
    float - Para valores decimais, Float.
    int - Para valores inteiros, int.

    OBS.: Cada tipo de casting é utilizado em situações especificas.
    O tipo "Float" por exemplo pode ser usado para montar uma calculadora de IMC, na coleta de altura e peso.
'''

# Criando variaveis com casting:
variavel4 = str(3) # É o mesmo que "3"
variavel5 = int(3) # É o mesmo que 3
variavel6 = float(3.0) # É o mesmo que 3.0 (Os numeros em ingles são separdos com ponto e nao virgula.)

# Pra saber o tipo de dado de uma variavel utilizamos a função type:
print(type(variavel4)) # Ela vai devolver o tipo de dado - String
print(type(variavel5)) # Ela vai devolver o tipo de dado - Inteiro
print(type(variavel6)) # Ela vai devolver o tipo de dado - Float

'''
    O python é case sensitive:
    Significa que ele diferencia maiusculo e minusculo.
'''

variavel7 = 4
Variavel7 = "Bem vindo à 2024"

print(variavel7) # Esta retorna 4
print(Variavel7) # Esta retorna uma frase.

# No modulo 2, Tipos de dados.