import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Abertura de arquivos')
        self.geometry('700x500')

        ttk.Button(
            self,
            text='Carregar arquivo',
            command=self.select_file
        ).pack(expand=True)

    def select_file(self):
        filetypes = (('Text Files', '*.txt'),
                     ('All Files', '*.*'))
        filename = fd.askopenfilename(
            title='Abrir arquivo',
            initialdir="/",
            filetypes=filetypes
        )
        if filename:
            showinfo(title='Arquivo selecionado', message=filename)


if __name__ == '__main__':
    app = App()
    app.mainloop()
