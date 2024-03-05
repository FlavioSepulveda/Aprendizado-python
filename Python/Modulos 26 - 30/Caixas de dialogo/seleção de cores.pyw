import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.colorchooser import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Abertura de varios arquivos')
        self.geometry('700x500')

        ttk.Button(
            self,
            text='Color change',
            command=self.change_color
        ).pack(expand=True)
        
    def change_color(self):
        cor = askcolor(title='Seletor de cores')
        self.configure(background=cor[1])
        print(cor)

if __name__ == '__main__':
    app = App()
    app.mainloop()
