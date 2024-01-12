# MODULOS 13 - Programação Orientada a objetos (POO)

'''
    Classes são construtores de objetos.
'''
class MyClass:
    x = 5

print(MyClass) # Retorna o tipo do objeto
# Criando um objeto derivado desta classe:
p1 = MyClass()
p1.x # Acessando o valor dentro da classe.
print(p1.x) # vai imprimir o x de dentro da classe.

# A função interna init que acompanha as classes em sua criação;
# A função init starta junto com a classe servindo para delimitar certas caracteristicas dentro da classe.

    # As funções dentro da classe sempre iniciam com Self.
class MinhaClasse:

    def __init__(self, nome_user, idade_user) -> None:
        self.nome = nome_user
        self.idade = idade_user


# Classes são como seções em livros de receitas.
client = MinhaClasse("Antonio", 21)

print(client.nome, client.idade)

# Métodos de objetos - são funções que pertencem a um objeto

# Criando uma classe pessoa;
class Pessoa:
    def __init__(self, _nome, _idade, _genero) -> None:
        self.Nome = _nome
        self.Idade = _idade
        self.Genero = _genero
    # métodos de uma classe são as coisas que aquela classe pode fazer.
    def myFunc(self):
        print('Ola, meu nome é ', self.Nome)

pessoa1 = Pessoa("Flavio", 21, "Masc")
pessoa1.myFunc()

pessoa2 = Pessoa("Antonio", 21, "Masc")
pessoa2.myFunc()

# O parametro self
'''
    Self - Vem do ingles, e significa "A mim mesmo", dentro das classes seria algo do tipo:
    "A mim mesmo darei o atributo idade."
'''
# Ele não precisa necessariamente ser chamado de self.
# Ele sempre é o primeiro parametro da função.

class Exemplo:
    def __init__(exemplo, parametro1, parametro2) -> None:
        exemplo.p1 = parametro1
        exemplo.p2 = parametro2
        # Neste exemplo temos uma mudança no self para "Exemplo" onde todas as vezes que eu o referenciar dentro da função init ele deve ser chamado por "Exemplo", No entanto quando de trata de outra função dentro de uma classe.
    def idade(self):
        print(self.p2)

pessoa3 = Exemplo("2","4")
pessoa3.idade()

# Declaração de passagem - evita erros de sintaxe

# class Passagem:
#     def __init__(self) -> None:
#         pass

# Modificando propriedades de um objeto.

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def firstFunc(self):
        print("Ola meu nome é: ", self.nome)


# para mudar o valor de uma variavel do objeto usamos o operador de atribuição
p1 = Pessoa("Gabriel", 21)
p1.firstFunc()
p1.nome = "Lucas"
p1.firstFunc()

# Excluindo propriedades de um objeto, ou um objeto inteiro:
class Pessoa1:
    def __init__(self, nnome, iidade) -> None:
        self.nome = nnome
        self.idade = iidade
    def firstFunc(self):
        print("Ola meu nome é: ", self.nome)

p1 = Pessoa1("Gabriel", 21)
print("Nome: ", p1.nome)
print("Idade: ", p1.idade)
# Excluimos com o metodo del
# del p1.idade
# print("Nome: ", p1.nome)
# print("Idade: ", p1.idade) # Ira gerar um erro por tentar referenciar a idade.

# Buscando o objeto e deletando ele
# print(p1)
# del p1
# print(p1) # Gera um erro pq o objeto não existe mais

# Herança - A classe main/pai/base >> A classe filha/derivada
class Heranca:
    def __init__(self, _nome, _idade) -> None:
        self.nome = _nome
        self.idade = _idade

    def imprimeDados(self):
        print("Sou ", self.nome, "E tenho ", self.idade)

p1 = Heranca("Gabriel", 22)
p1.imprimeDados()

# Para criar a herança precisamos criar a classe e passar a main como parametro da classe;
# A função init na classe derivada
class Estudante(Heranca):
    def __init__(self, _nome, _idade) -> None: # Quando colocamos essa função dentro de uma função derivada ela sobrescreve a anterior.
        # Pessoa.__init__(self, _nome, _idade) # Aqui defino oque ele faz referenciando a classe main.
        # A função super faz com que a herança seja a mesma da main.
        super().__init__(_nome, _idade)
        pass

p2 = Estudante("Arthur", 17)
# Principal intuito da herança é tornar reaproveitavel um código, e tornar mais facil desenvolver alguns sistemas como o de cadastro por exemplo.
p2.imprimeDados()
# Como Add metodos e proprieadades na nossa nossa função herdada:
class Heranca:
    def __init__(self, _nome, _idade) -> None:
        self.nome = _nome
        self.idade = _idade

    def imprimeDados(self):
        print("Sou ", self.nome, "E tenho ", self.idade)

p1 = Heranca("Gabriel", 22)
p1.imprimeDados()

class Estudante(Heranca):
    def __init__(self, _nome, _idade, _anoGrad) -> None: 
            super().__init__(_nome, _idade)
            self.anoGrad = _anoGrad # Add uma nova propriedade
# Add Metodos na nossa classe
    def bemVindo(self):
        print("Bem vindo ", self.nome, 'ao ano', self.anoGrad)

x = Estudante("Flavio", 21, 1999)
x.imprimeDados()
# Referenciando a função.
x.bemVindo()
     