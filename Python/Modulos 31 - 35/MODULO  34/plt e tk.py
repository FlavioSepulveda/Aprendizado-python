import tkinter as tk
from tkinter import ttk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Linguagens de Programação - tk e plt')
        self.resizable(0, 0)

        data = {
        'Python' : 11.27,
        'C' : 11.16,
        'Java' : 7.46,
        'C++' : 15.5,
        'C#' : 17.26
        }
        
        languages = data.keys()
        popularity = data.values()
        
        # Criando a figura -
        figure = Figure(figsize=(6,4), dpi=100)
        
        # Criando um Objeto figure canvas tk agg -
        figure_canvas = FigureCanvasTkAgg(figure, self)
        
        # Barra de navegação -
        # NavigationToolbar2Tk(figure_canvas, self)
        
        # Criando os eixos -
        axis = figure.add_subplot()
        
        axis.bar(languages, popularity)
        axis.set_title('Top 5 Linguagens populares')
        axis.set_ylabel('Popularidade')
        axis.set_xlabel('Linguagens')
        
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Button(self,text='sair', command= self.destroy).pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()
    




# plt.title('Langs Popularity')
# plt.bar(languages,popularity)

# plt.show()