import pandas as pd

# Analizando data frames -
# Visão rapida
df = pd.read_csv('C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/data.csv')
print(df.head(10)) # Quando não especificado ele imprime as 5 primeiras linhas
print(df.tail(10)) # Quando não especificado ele imprime as 5 ultmimas linhas

# Info - Retorna informações sobre o conjunto de dados.
print(df.info())


