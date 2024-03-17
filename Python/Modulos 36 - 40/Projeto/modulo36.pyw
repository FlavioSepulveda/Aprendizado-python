# MODULO 36 - Projeto: Aplicação Tkinter com Base de Dados
import tkinter as tk
from tkinter import ttk
import mysql.connector
import re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Criando variavel que controla o label.
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self, textvariable=self.varResultado,
            font=('Arial', 18),
            background='#DDDDDD'
        )
        self.lblResultado.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky='nsew')
        
        # Nome -
        self.lblNome = ttk.Label(
            self,text='Nome: ',
            font=('Arial', 18, 'bold')
        )
        self.lblNome.grid(row=1, column=0, sticky='w', padx=20, pady=5)
        self.varNome = tk.StringVar(self)
        self.txtNome = ttk.Entry(
            self, textvariable=self.varNome,
            font=('Arial', 18)
        )
        self.txtNome.grid(row=1, column=1, sticky='we', padx=20, pady=5)
        self.txtNome.focus()
        
        # Email -
        self.lblEmail = ttk.Label(
            self, text='E-mail: ',
            font=('Arial', 18, 'bold')
        )
        self.lblEmail.grid(row=2, column=0, sticky='w', padx=20, pady=5)
        self.varEmail = tk.StringVar(self)
        self.txtEmail = ttk.Entry(
            self, textvariable=self.varEmail,
            font=('Arial', 18)
        )
        self.txtEmail.grid(row=2, column=1, sticky='we', padx=20, pady=5)
if __name__ == '__main__':
    app = App()
    app.mainloop()
