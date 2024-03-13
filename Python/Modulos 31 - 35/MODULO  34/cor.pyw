# pizza e cores
import matplotlib.pyplot as plt


x = [35, 40, 20, 55]
ml = ['banana', 'macas', 'uvas', 'laranja']
colors = ['yellow', 'red', 'purple', 'orange']

plt.pie(x, colors=colors)
plt.legend(labels=ml, title='Frutas')
plt.show()