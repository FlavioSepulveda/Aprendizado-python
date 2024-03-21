import pandas as pd

# Serie pandas -
# É um array unidimesional que guarda dados de todos os tipos.

# a = [1,7,2]
# # myvar = pd.Series(a)
# myvar = pd.Series(a, index=['X', 'Y', 'Z'])

# # print(a)
# # print(myvar[0])
# print(myvar)
# print(myvar['Y'])

# calorias = {
#     'Dia 1 -> ': 420,
#     'Dia 2 -> ': 380,
#     'Dia 3 -> ': 390
# }
# # myvar = pd.Series(calorias)
# myvar = pd.Series(calorias, index=['Dia 1 -> ', 'Dia 2 -> '])
# print(myvar)

# Uma serie é uma coluna de dados - Um data frame é uma tabela inteira

# Criando um data frame (introduçã)-
data = {
    'Calorias': [420, 380, 390],
    'Duração': [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
