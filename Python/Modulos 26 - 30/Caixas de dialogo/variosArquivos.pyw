import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Abertura de varios arquivos')
        self.geometry('700x500')

        ttk.Button(
            self,
            text='Open',
            command=self.select_file
        ).pack(expand=True)

    def select_file(self):
        filetypes = (('Txt files', '*.txt'),
                     ('PDF files', '*pdf'),
                     ('All files', '*.*'))
        filename = fd.askopenfilenames(
            title='Open file',
            initialdir='/',
            filetypes=filetypes
        )

        for i in filename:
            print(i)

        if filename:
            showinfo('Arquivo selecionado', message=filename)


if __name__ == '__main__':
    app = App()
    app.mainloop()
