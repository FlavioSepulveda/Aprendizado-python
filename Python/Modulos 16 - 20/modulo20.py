# MODULO 19 - RegEx (Expressões Regulares) em Python
# Serve para verificar a String contem um formato de pesquisa especifico.
import re

txt = "O seu nome é Flávio"

# Verificar se uma string começa com 'é' e termina com "Flavio"
x = re.search("^O.*Flávio.$", txt)
if x:
    print("Sim encontramos.")
else:
    print("Nenhuma encontrada.")

# Expressoes regulares em uma string - Search();

texto = "O calor do motor da moto"

var1 = re.search("\s", texto)

print(var1)
print("O primeiro espaço em branco esta em: ", var1.start())
var1 = re.search("Brasil", texto)
print(var1)

# Função findall()
# Retorna todas as correspondencias em uma lista.

txt1 = "O calor do motor da moto"

x = re.findall("or", txt1)
print(x)
if x:
    print('Foram encontradas 2 correspondencias.')
else:
    print("Nenhuma combinação encontrada.")

# x = re.findall("Brasil", txt1) # retorna uma lista vazia
print(x)