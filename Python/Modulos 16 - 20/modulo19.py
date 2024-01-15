# MODULO 19 - Linguagem JSON e Phython
# Trabalho com JSON no python

import json
# Convertendo um objeto json para python por meio do metodo Loads()
x = '{"Nome": "Flavio", "Idade": 21, "Cidade": "Teresina"}'

y = json.loads(x)
print(y)
# print(type(y))
# print(y["Nome"])
# print(y["Idade"])
# print(y["Cidade"])
# Convertendo python pra json por meio do metodo dumps
x1 = {
      "Nome": "Flavio", 
      "Idade": 21, 
      "Cidade": "Teresina"
      }
# Realizando a conversão
y1 = json.dumps(x1)
print(y1)
print(type(x1)) # Python
print(type(y1)) # JSON
# Exemplos de objetos python que retornam dados json
print(json.dumps({"Nome": "Flavio", "Idade": 21, "Cidade": "Teresina"}))
print(json.dumps(['Maçã', 'Banana']))
print(json.dumps(('Maçã', 'Banana')))
print(json.dumps('Ola, mundo'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))