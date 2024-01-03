# VALORES BOOLEANOS
# Os valores booleanos são valores que se apresentam em 2 valores (1 ou 0) (True or False) (Verdadeiro ou Falso).

True    # Verdadeiro
False   # Falso

# As expressões booleanas 
# Estas expressoes são como perguntas a lunnguagem.

# Exemplo1 -
print(10>9) # Dez é maior que nove? - Verdadeiro
print(10<9) # Dez é menor que nove? - Falso
print(10==9) # Dez é igual que nove? - Falso

# São normalmente usadas para definir o fluxo do programa.

a = 200
b = 33

# Podemos utilizar-las em estruturas condicionais conforme o exemplo:
if (b > a): # Se b for maior que a escreva "Sim, b é maior que a."
    print("Sim, b é maior que a.")
else:       # Se b não for maior que a escreva "Sim, b não é maior que a."
    print("Não, b não é maior que a.")

# Retornos booleanos decidem qual parte do codigo executar.
    
# Metodo Bool - Verifica valores booleanos
print(bool("Ola"))
# A maioria dos valores retornam true listas são um exemplo:
print(bool(['Carro', 'caminhão', 'moto']))

# Estes são os unicos exemplos que irão retornar 0
x = 0
y = ""
z = [] # Dicionarios, listas, tuplas vazias retornam falso.

print(bool(x))
print(bool(y))
print(bool(z))

# Trabalhando com funçôes;

def myFunction():
    return 10 > 5

print(myFunction())

# Podemos utilizar nas expressoes condicionais

if (myFunction()):
    print("Sim")
else:
    print("Não")

# Insistancia - esta função verifica e retorna o valor sendo ele verdadeiro ou falso

x = 200
print(isinstance(x, int))