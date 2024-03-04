# MODULO 29 - Caixas de Dialogos e Menus
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de mensagens')
        self.geometry('700x500')
        
        options = {'padx':5,'pady':5}
        
        ttk.Button(
            self,
            text='Informação',
            command=lambda: showinfo(title='Informação', message='Voce foi informado :)')
        ).pack(**options,expand=True)
        ttk.Button(
            self,
            text='Aviso',
            command=lambda: showwarning(title='Aviso', message='Voce foi avisado :)')
        ).pack(**options,expand=True)
        ttk.Button(
            self,
            text='Erro',
            command=lambda: showerror(title='Erro encontrado', message='Voce foi errado ;)')
        ).pack(**options,expand=True)
        
if __name__=='__main__':
    app=App()
    app.mainloop()