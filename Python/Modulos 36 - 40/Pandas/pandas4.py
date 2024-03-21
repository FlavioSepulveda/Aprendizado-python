# Carregando um arquivo csv no pandas
import pandas as pd

# Csv - é um formato amigavel a quase todos os metodos
pd.options.display.max_rows=70
df = pd.read_csv('C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/data.csv')
# print(df.to_string())

print(df) # imprimindo apenas as 5 primeiras e 5 ultimas
# pd.options.display.max_rows = 999
print(pd.options.display.max_rows) # Printa 60 linhas