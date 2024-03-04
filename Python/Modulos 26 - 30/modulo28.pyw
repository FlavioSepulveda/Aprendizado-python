# MODULO 28 - Tkinter POO
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Mainframe(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        # Configurações -
        options = {'padx': 5, 'pady': 5}
        
        # Label -
        self.label = ttk.Label(self, text='Ola mundo')
        self.label.pack(**options)
        
        # Button -
        self.btn = ttk.Button(self, text='Click me!')
        self.btn['command']=self.button_clicked
        self.btn.pack(**options)
        
        self.pack(**options)
    
    def button_clicked(self):
        showinfo(title='Informações', message='Ola mundo!')    

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configurações da janela principal -
        # Titulo -
        self.title('Minha aplicação em POO')
        # Geometria da tela -
        self.geometry('400x200')
        # Resize -
        self.resizable(0, 0)


if __name__ == '__main__':
    app = App()
    frame = Mainframe(app)
    app.mainloop()
    
# Tkraise