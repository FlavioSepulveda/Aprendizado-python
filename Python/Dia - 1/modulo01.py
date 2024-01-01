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

# Existem regras pra nomear uma variavel.

'''
    OS MANDAMENTOS DAS VARIAVEIS - Estreando variaveis em python:
        1 # Nomes de variaveis sempre devem começar com letras ou underline;
        2 # Embora possam conter numeros, nunca nomeie uma variavel com um numero no inicio;
        3 # Variaveis podem conter dígitos alfanuméricos  (Letras e Números);
        4 # Os nomes diferenciam de maiúsculas e minusculas;
        5 # Os nomes não devem conter acentos;
'''

# Exemplos -
minhavariavel = "Flavio" # Todas as letras minusculas
minha_variavel = "Flavio" # Um underline no meio da varivel
_minha_variavel = "Flavio" # Iniciando o nome com underline
minhaVariavel = "Flavio" # Iniciando o nome da variavel com minuscula e colocando letras maiusculas no meio (Camel case)
MINHAVARIAVEL = "Flavio" # Todas as letras maiusculas
minhavariavel2 = "Sepulveda" # Numero ao fim do nome

# As formas citadas anteriormente são corretas porem aqui alguns exemplos de erros;
'''
    2minhavariavel = "Flavio" (Não pode iniciar com número)
    minha-variavel = "Flavio" (Traço não é separação)
    minha variavel = "Flavio" (Não pode ter espaçamento vazio)
'''

'''
    Existem varias formas de se escrever nomes de variaveis extensas.
    Aqui temos alguns exemplos das mais utilizadas:
    Camel case - A separação das palavras exceto as primeiras, se faz com letra maiusculas;
        * EX.: minhaVariavelExemplo = "Camel Case"
    Pascal case - As primeiras letras inclusive da primeira palavra são maiusculas;
        * EX.: MinhaVariavelExemplo = "Pascal Case"
    Snake case - A separação das palavras é feita por meio de underline aqui;
        * EX.: minha_variavel_exemplo = "Snake Case"
'''

# Atribuição de valores as variavveis

# Python permite atribuição de valores a diferentes variaveis sem a nescessidade de saltar varias linhas;
'''
    Em outras linguagens as variaveis devem ser feitas em linhas separadas, assim:
    var1 = 1
    var2 = 2
    var3 = 3
'''

# Em python esta atribuição pode ser feita de maneira mais simples e em apenas uma linha;
# POR EXEMPLO -
var1, var2, var3 = 1, 2, 3 # Esta forma de atribuição é mais simples mas prioriza a ordem a qual você que atribuir alguns valores.

# As reproduzindo com um comando print o resultado sera o mesmo da sequencia
print(var1) # Imprime 1
print(var2) # Imprime 2
print(var3) # Imprime 3

# Podemos tambem, atribuir o mesmo valor a varias variaveis
# var4 = "Antonio"
# var5 = "Antonio"
# var6 = "Antonio"

# Porem a formas mais simples de se fazer isso, como esta:
var4 = var5 = var6 = "Antonio"
# Ao imprimir estas variaveis, o mesmo valor no caso "Antonio", será atribuido as 3
print(var4) 
print(var5) 
print(var6)

# DESCOMPACTAR - O ato de separar os trechos de um array em diferentes variaveis;
# desta maneira:
frutas = ['maça', 'banana', 'cereja'] # Coleção de frutas
frutas1, frutas2, frutas3 = frutas # Cada variavel ira receber um dado de uma coleção

print(frutas1)
print(frutas2)
print(frutas3)

# Operador de concatenação
palavra1 = "Mundo"

# Juntando variaveis as frases
print("Ola, " + palavra1)
# Podemos somar variaveis dessa maneira
nome = "Antonio"
sobrenome = "Flavio"
# A soma de nome e sobrenome deve resultar em nome completo
nomeCompleto = nome + sobrenome
print(nomeCompleto)

# Este metodo de soma tambem serve para valores numericos
valor1 = 1
valor2 = 3

soma = valor1 + valor2 # A soma dos valores resulta em 4
print(soma) 

# Obs.: Tentar somar uma string com um numero inteiro ou float, ira resultar em um erro.
# Pra somar uma string e um numero, devemos utilizar o casting

num = 20
var = "K"
juncao = str(num) + var
print(juncao) # Esta forma ira resultar em calgo que não dara erro.

# VARIAVEIS GLOBAIS E VARIAVEIS LOCAIS

# A funções sao blocos de codigo que são chamados sempre que as funções são referenciadas
# As funções são referenciadas por meio do comando def

def myFunc():
    print("Ola, mundo!!!!!!!!!!")
# Pra executar a função deve executar-la
myFunc() # Servem pra reaproveitamento de código;


# Criando variaveis de escopo global:
pal1 = "Antonio"
# Criando a função:
def meuNome():
    print(pal1 + " Flavio")

meuNome()
print("Meu nome é: " + pal1)

# As variaveis locais
nick = "sunny"    # Esta é uma variavel global.

def meuNick():
    nick = "hallsey"  # Esta é uma variavel Local.
    print(nick)

meuNick()

# Obs: Porque o nome da variavel mudou de sunny pra hallsey?
'''
    * As variaveis quando fora de uma função são denominadas de variaveis globais estas podem ser referenciadas de qualquer lugar do código, diferente das variaveis locais.
    *As variaveis locais tem sua origem e uso dentro de suas respectivas funções, e as funções por mais que saibam da existencia de uma função global, dão prioridade as  funções locais, estas por sua vez só existem dentro de suas respectivas funções, similares as variaveis temporarias que criamos na    GML.
    E se... eu printar a variavel do exemplo fora da função?
'''
print(nick) # Ira printar sunny;

'''
    Existe uma forma de criar uma variavel global dentro de uma funçao?
    Sim, por meio do uso da palavra chave global.
    As definimos como global, depois damos o valor delas.
'''

# Criação de variaveis globais dentro de uma função:
def anoNovo():
    global ano
    ano = str(2024)
    # Diga olá ao ano novo
    print("Diga ola à " + ano)

# chamando a função:
anoNovo()
# Chamando a variavel global dentro da função;
print("ola " + ano)

# A palavra chave Global tambem serve para trocar o valor da variavel

varTeste = "Cubo Mágico"     # Esta é a variavel que deve ser alterada

def exemplo():
    # Modificando o valor da variavel de teste:
    global varTeste
    varTeste = "Enigma"
    # Imprimindo o novo valor dado á variavel:
    print("Resolvi o " + varTeste)

exemplo()
# Chamando a variavel que foi modificada:
print("Resolvi o " + varTeste)