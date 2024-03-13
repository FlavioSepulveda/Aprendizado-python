# pizza e sombas
import matplotlib.pyplot as plt


x = [35, 40, 20, 55]
ml = ['banana', 'macas', 'uvas', 'laranja']
myExplode = [0.2, 0.1, 0.1, 0.1]

plt.pie(x, labels=ml, startangle=90, explode=myExplode, shadow=True)

plt.show()