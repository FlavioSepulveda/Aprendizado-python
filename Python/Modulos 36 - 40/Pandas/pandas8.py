import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('C:/Users/flavi/OneDrive/Desktop/Py/Aprendizado-python/Python/Modulos 36 - 40/Pandas/data.csv')
# data.plot()
# data.plot(kind='scatter', x='Duração', y='Calorias')
# data.plot(kind='scatter', x='Duração', y='Maxpulso')
data.plot(kind='hist', x='Duração', y='Maxpulso')

plt.show()

print(data.to_string())