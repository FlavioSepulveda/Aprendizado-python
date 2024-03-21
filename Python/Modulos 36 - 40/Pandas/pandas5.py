# Abrindo Arquivos json no pandas
import pandas as pd

data = pd.read_json('C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/data.json')

# print(data.to_string())
# print(data)

df = pd.DataFrame(data)
print(df)