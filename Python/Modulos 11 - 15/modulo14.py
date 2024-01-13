# MODULOS 14 - Interadores Python

# Os interadores são - Objetos que contem numeros contados de valores.
# Inter & Next
# As listas, tuplas e sets - Sao interadores.

myTuple = ('Flavio', 'Caio', 'Carlos')
myInt = iter(myTuple)

# O metodo next pega sempre o proximo codigo de um interavel.
print(next(myInt)) 
print(next(myInt))
print(next(myInt))
# As strings tbm são interaveis, elas possuem um interador tbm.

fruta = 'Banana'
myInt2 = iter(fruta)

print(next(myInt2))
print(next(myInt2))
print(next(myInt2))
print(next(myInt2))
print(next(myInt2))
print(next(myInt2))

# Um método for cria algo semelhante a um iterator 
for x in myTuple:
    print(x)

# Criando um interador que aumenta em um
    
class MeusNumeros:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = MeusNumeros()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))