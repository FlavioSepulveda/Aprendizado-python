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

'''
    Self - Vem do ingles, e significa "A mim mesmo", dentro das classes seria algo do tipo:
    "A mim mesmo darei o atributo idade."
'''
    # As funções dentro da classe sempre iniciam com Self.
class MinhaClasse:

    def __init__(self, nome_user, idade_user) -> None:
        self.nome = nome_user
        self.idade = idade_user


# Classes são como seções em livros de receitas.
client = MinhaClasse("Antonio", 21)

print(client.nome, client.idade)
    