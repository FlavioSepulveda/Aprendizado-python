import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry('700x500')

        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=False)
        
        # ---------------------------------------------------------------------
        
        file_menu.add_command(label="Novo", command=lambda: self.destroy())
        file_menu.add_command(label="Abrir", command=lambda: self.destroy())
        file_menu.add_command(label="Salvar", command=lambda: self.destroy())
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=lambda: self.destroy())
        menubar.add_cascade(label='Arquivo', menu=file_menu, underline=0)
        
        # ---------------------------------------------------------------------
        
        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(label='Bem vindo')
        help_menu.add_command(label='Sobre', command=self.sobre)
        menubar.add_cascade(label='Ajuda', menu=help_menu, underline=1)
        
    def sobre(self):
        showinfo(
            title='Sobre',
            message='Desenvolvido por Flavio'
        )
        

if __name__ == '__main__':
    app = App()
    app.mainloop()
