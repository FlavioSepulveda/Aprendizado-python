import pandas as pd

# Data frames sao bidimensionais com linhas e colunas
data = {
    'Calorias': [420, 380, 390],
    'Duração': [50, 40, 45]
}

# df = pd.DataFrame(data)
df = pd.DataFrame(data, index=['dia1', 'dia2', 'dia3'])
print(df)
print('-------------------------------------------')
print(df.loc['dia1'])
# Podemos usar o loc para localizar a linha pelo nome que criamos no data frame

# print('-------------------------------------------')
# # O pandas usa o atributo loc para criar as linhas
# print(df.loc[0]) # Retorna uma serie pandas
# print('-------------------------------------------')
# print(df.loc[[0,1]]) # retorna um data frame pandas
# print('-------------------------------------------')
