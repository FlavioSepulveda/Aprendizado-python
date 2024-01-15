# MODULO 19 - Linguagem JSON e Phython
# Trabalho com JSON no python

import json
# Convertendo um objeto json para python por meio do metodo Loads()
x = '{"Nome": "Flavio", "Idade": 21, "Cidade": "Teresina"}'

y = json.loads(x)
print(y)
print(type(y))
print(y["Nome"])
print(y["Idade"])
print(y["Cidade"])