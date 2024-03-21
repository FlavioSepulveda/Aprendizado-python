# MODULO 39 - Módulo Python Pandas
import pandas as pd
# Biblioteca focada em analise de dados
# (https://github.com/pandas-dev/pandas) base de codigos do pandas

# Criando uma tabela com o metodo "Data Frame"
mydataset = {
    'carros': ['BMW', 'Volvo', 'Ford'],
    'passageiros': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)