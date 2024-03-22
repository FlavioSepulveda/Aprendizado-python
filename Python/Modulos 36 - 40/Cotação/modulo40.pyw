# MODULO 40 - Projeto: App cotação Dolar com PI JSON, Tkinter, Matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib
import requests
from datetime import datetime as dt

matplotlib.use('TkAgg')


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cotação do dolar')

        # Criando uma figura -
        self.figure = Figure(figsize=(15, 6), dpi=100)

        # Criando um objeto FigureCanvasTkAgg -
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        # Criando a barra de ferramentas -
        NavigationToolbar2Tk(self.figure_canvas, self)

        # Criando um grafico
        self.chart = self.figure.add_subplot()

        self.current_value = tk.StringVar(value=10)
        self.cmdExecutar()

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Spinbox -
        self.spinRange = ttk.Spinbox(
            self,
            from_=1,
            to=60,
            textvariable=self.current_value,
            wrap=True,
            font=('Arial 18 bold')
        )
        self.spinRange.pack(fill='x', side='left', expand=True, padx=5)

        # Botão -
        # Atualizando o grafico.
        ttk.Button(
            self, text='Atualizar',
            command=self.cmdExecutar
        ).pack(fill='x', side='left', expand=True, padx=5)

    def cmdExecutar(self):
        # Obtendo os dados do gráfico
        # https://economia.awesomeapi.com.br/json/daily/USD-BRL/10

        cotacoes = requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{
                                self.current_value.get()}")  # Carregando API json
        xData = []
        yData = []
        yData2 = []
        yData3 = []
        yData4 = []

        for x in cotacoes.json():
            ts = int(x['timestamp'])
            # Formatando como data
            xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData.insert(0, xEixo)
            yData.insert(0, float(x['bid']))
            yData2.insert(0, float(x['ask']))
            yData3.insert(0, float(x['low']))
            yData4.insert(0, float(x['high']))

        self.chart.clear()

        self.chart.plot(xData, yData, marker='o', label='Compra')
        self.chart.plot(xData, yData2, marker='o', label='Venda')
        self.chart.plot(xData, yData3, marker='o', label='Minimo')
        self.chart.plot(xData, yData4, marker='o', label='Maxima')

        self.chart.set_title(cotacoes.json()[0]['name'])
        self.chart.set_xlabel('Datas')
        self.chart.set_ylabel('BRL')
        self.chart.grid()
        self.chart.legend()

        self.figure_canvas.draw()


if __name__ == '__main__':
    app = App()
    app.mainloop()
