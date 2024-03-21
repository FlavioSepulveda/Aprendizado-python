import pandas as pd

# C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/dirtydata.csv

# Limpeza de dados
# Apagando celulas vazias, dados ruins ou incorretos -

data = pd.read_csv('C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/dirtydata.csv')

# print(data.to_string)

# Iniciando a limpeza 
# Utilizamos o argumento 'Inplace' alteramos o dataframe original.
# new_data = data.dropna() # Criando uma copia, removendo as celulas vazias
# print(new_data.to_string())
# data.fillna(130,inplace=True)
# Fazendo ele rodar apenas em uma coluna -
# data.fillna(130,inplace=True)
# data['Calorias'].fillna(130,inplace=True)
# print(data.to_string())

# #Calculando a media trocando os valores vazios por ela

# x = data['Calorias'].mean() # Calcula a media somando todos os valores e dividiando-os pela quantidade
# x = data['Calorias'].median() # Retorna a media dos valores
# mode retorna o valor que aparece com mais frequencia especifica-se um indice
x = data['Calorias'].mode()[0]
data['Calorias'].fillna(x, inplace=True)
# Podemos converter todas as celulas para o mesmo formato-
# Corrigindo erro das datas -
data['Data'] = pd.to_datetime(data["Data"], errors='coerce') # Retorna um erro referente a linha 26 a a qual ele deveria corrigir
data.dropna(subset=['Data'], inplace=True)
# Corrigindo dados errados
# data.loc[7, 'Duração'] = 45 # Não é recomendado para esse para grands dados

# for x in data.index:
#     if data.loc[x, 'Duração'] > 120:
#         data.loc[x, 'Duração'] = 120
for x in data.index:
    if data.loc[x, 'Duração'] > 120:
        data.drop(x, inplace=True)
# Removendo linhas duplicadas -


data.drop_duplicates(inplace=True)
# print(data.to_string())
print(data.corr()) # Retorna a correlação entre as linhas

# uma boa correlação varia do uso
# Este metodo retorna a correlação entre os dados do arquivo.


