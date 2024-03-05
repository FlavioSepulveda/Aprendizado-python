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
        file_menu.add_command(label="Novo")
        file_menu.add_command(label="Abrir")
        file_menu.add_command(label="Salvar")
        file_menu.add_command(label="Sair", command=lambda: self.destroy())
        file_menu.add_separator()
        
        sub_menu = tk.Menu(file_menu, tearoff=False)
        sub_menu.add_command(label='Atalhos')
        sub_menu.add_command(label='Temas')
        file_menu.add_cascade(label='Preferences', menu=sub_menu, underline=0)
        
        file_menu.add_separator()
        # Adcionando o menu na barra de menu-
        menubar.add_cascade(
            label='File',
            menu=file_menu,
            underline=0
        )

if __name__ == '__main__':
    app = App()
    app.mainloop()
