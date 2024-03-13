# Histogramas
import matplotlib.pyplot as plt
import numpy as np

x = [35, 40, 20, 55]
ml = ['banana', 'macas', 'uvas', 'laranja']
plt.pie(x, labels=ml, startangle=90)

'''
    O parametro start angle muda o local onde o grafico se inicia.
'''

plt.show()

