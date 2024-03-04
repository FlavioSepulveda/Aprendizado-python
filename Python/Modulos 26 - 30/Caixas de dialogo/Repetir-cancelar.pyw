import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Repetir cancelar')
        self.geometry('700x500')
        
        ttk.Button(
            self,
            text='Conectar-se ao servidor',
            command=self.confirm
        ).pack(expand=True)
        
    def confirm(self):
        result = askretrycancel(title='Falha encontrada', message='Tente novamente mais tarde')
        if result:
            # Código para tentar novamente
            showinfo(title='Informação', message='Tentando conectar-se novamente.')

if __name__=="__main__":
    app = App()
    app.mainloop()