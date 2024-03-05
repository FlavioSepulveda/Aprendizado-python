import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Abertura de arquivos')
        self.geometry('700x300')

        self.text = tk.Text(self, height=12)
        self.text.pack(expand=True)

        ttk.Button(
            self,
            text='Open',
            command=self.select_file
        ).pack(expand=True)

    def select_file(self):
        filetypes = (('Txt files', '*.txt'),
                     ('All files', '*.*'))
        file = fd.askopenfile(
            title='Open file',
            initialdir='/',
            filetypes=filetypes
        )
        self.text.delete("1.0", "end")
        # self.text.insert('1.0', file.readlines())
        for i in file.readlines():
            self.text.insert("1.0",i)

if __name__ == '__main__':
    app = App()
    app.mainloop()
