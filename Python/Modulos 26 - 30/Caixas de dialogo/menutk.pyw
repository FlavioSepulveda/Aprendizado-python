import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry('700x500')
        # Criando a barra do menu
        menubar = tk.Menu(self)
        self.configure(menu=menubar)
        # Criando um menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(
            label='Exit',
            command=lambda: self.destroy()
        )
        # Adcionando o menu na barra de menu-
        menubar.add_cascade(
            label='File',
            menu=file_menu,
            underline=0
        )

if __name__ == '__main__':
    app = App()
    app.mainloop()
