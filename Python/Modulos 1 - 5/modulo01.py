# MODULO 01 - VARIÁVEIS

# Comentários explicativos sobre variáveis e atribuição
'''
    Variáveis são espaços reservados na memória do computador para armazenar dados.
    Estes espaços utilizamos para a construção de nossos programas e algoritmos.
'''

# Exemplo de criação de variável
variavel1 = 1

# Exemplos de variáveis de texto e uso do comando "print"
texto1 = 'Atribuição com aspas simples'
texto2 = "Atribuição com aspas duplas"
print(texto1)

# Demonstração de alteração de tipo de variável e casting
variavel2 = 3
variavel2 = 7
variavel2 = "Agora é do tipo string"

# Descrição dos tipos de casting disponíveis
'''
    OS VALORES DO CASTING SÃO:
    str - Para valores de texto, Strings.
    float - Para valores decimais, Float.
    int - Para valores inteiros, int.

    OBS.: Cada tipo de casting é utilizado em situações específicas.
'''

# Exemplos de criação de variáveis com casting
variavel4 = str(3)
variavel5 = int(3)
variavel6 = float(3.0)

# Uso da função type para verificar o tipo de dado
print(type(variavel4))
print(type(variavel5))
print(type(variavel6))

# Python é case sensitive
variavel7 = 4
Variavel7 = "Bem vindo à 2024"
print(variavel7)
print(Variavel7)

# Mandamentos para nomear variáveis em Python
'''
    OS MANDAMENTOS DAS VARIÁVEIS - Estreando variáveis em Python:
        1 # Nomes de variáveis sempre devem começar com letras ou underline;
        2 # Embora possam conter números, nunca nomeie uma variável com um número no início;
        3 # Variáveis podem conter dígitos alfanuméricos (Letras e Números);
        4 # Os nomes diferenciam maiúsculas e minúsculas;
        5 # Os nomes não devem conter acentos;
'''

# Exemplos de variáveis seguindo os mandamentos
minhavariavel = "Flavio"
minha_variavel = "Flavio"
_minha_variavel = "Flavio"
minhaVariavel = "Flavio"
MINHAVARIAVEL = "Flavio"
minhavariavel2 = "Sepulveda"

# Exemplos de erros ao nomear variáveis
'''
    2minhavariavel = "Flavio" (Não pode iniciar com número)
    minha-variavel = "Flavio" (Traço não é separação)
    minha variavel = "Flavio" (Não pode ter espaçamento vazio)
'''

# Formas de escrever nomes de variáveis extensas
'''
    Existem varias formas de se escrever nomes de variáveis extensas.
    Aqui temos alguns exemplos das mais utilizadas:
    Camel case - A separação das palavras, exceto as primeiras, é feita com letras maiúsculas;
    Pascal case - As primeiras letras, inclusive da primeira palavra, são maiúsculas;
    Snake case - A separação das palavras é feita por meio de underline.
'''

# Atribuição de valores às variáveis
'''
    Python permite a atribuição de valores a diferentes variáveis sem a necessidade de saltar várias linhas;
'''

# Exemplos de atribuição de valores em uma linha
var1, var2, var3 = 1, 2, 3
print(var1)
print(var2)
print(var3)

# Atribuição do mesmo valor a várias variáveis em uma linha
var4 = var5 = var6 = "Antonio"
print(var4)
print(var5)
print(var6)

# Descompactação de valores de um array em diferentes variáveis
frutas = ['maça', 'banana', 'cereja']
frutas1, frutas2, frutas3 = frutas
print(frutas1)
print(frutas2)
print(frutas3)

# Operador de concatenação
palavra1 = "Mundo"
print("Ola, " + palavra1)

# Exemplo de soma de variáveis de texto e numéricas
nome = "Antonio"
sobrenome = "Flavio"
nomeCompleto = nome + sobrenome
print(nomeCompleto)

valor1 = 1
valor2 = 3
soma = valor1 + valor2
print(soma)

# Concatenação de string e número com casting
num = 20
var = "K"
juncao = str(num) + var
print(juncao)

# VARIAVEIS GLOBAIS E VARIAVEIS LOCAIS

# Definição e chamada de uma função
def myFunc():
    print("Ola, mundo!!!!!!!!!")

myFunc()  # Servem para reaproveitamento de código;

# Exemplo de criação de variável global e função
pal1 = "Antonio"

def meuNome():
    print(pal1 + " Flavio")

meuNome()
print("Meu nome é: " + pal1)

# Exemplo de variáveis globais e locais
nick = "sunny"  # Variável global

def meuNick():
    nick = "hallsey"  # Variável local
    print(nick)

meuNick()

# Exemplo de erro ao tentar imprimir variável local fora da função
print(nick)  # Ira imprimir sunny;

# Exemplo de criação e modificação de variável global dentro de uma função
def anoNovo():
    global ano
    ano = str(2024)
    print("Diga olá ao ano novo")

anoNovo()
print("Olá " + ano)

# Exemplo de modificação de variável global usando a palavra chave Global
varTeste = "Cubo Mágico"

def exemplo():
    global varTeste
    varTeste = "Enigma"
    print("Resolvi o " + varTeste)

exemplo()
print("Resolvi o " + varTeste)
