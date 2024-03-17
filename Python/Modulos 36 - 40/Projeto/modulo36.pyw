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
        self.lblResultado.grid(row=0, column=0, columnspan=3,padx=20, pady=10, sticky='nsew')

        # Nome -
        self.lblNome = ttk.Label(
            self, text='Nome: ',
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
        
        # Lista de resultados -
        self.frameLista = ttk.Frame(self)
        self.frameLista.grid(row=3, column=0, columnspan=2, rowspan=4, sticky='nsew', padx=20, pady=10)
        
        self.txtLista = ttk.Treeview(
            self.frameLista, columns=('nome', 'email'),
            show='headings', height=7
        )
        self.txtLista.heading('nome', text='Nome')
        self.txtLista.heading('email', text='Email')
        
        def item_selected(event):
            for selected_item in self.txtLista.selection():
                item = self.txtLista.item(selected_item)
                record = item['values']
                self.varNome.set(record[0])
                self.varEmail.set(record[1])
                
        self.txtLista.bind('<<TreeviewSelect>>', item_selected)
        self.txtLista.grid(row=0, column=0, sticky='nwes')
        
        scrollbar = ttk.Scrollbar(
            self.frameLista, orient=tk.VERTICAL,
            command=self.txtLista.yview)
        self.txtLista.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Botões -
        self.btnConectar=ttk.Button(
            self, text='Conectar',
            command=self.btnConectar_Click
        )
        self.btnConectar.grid(row=1, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnCriar=ttk.Button(
            self, text='Criar Tabela',
            command=self.btnCriarTabela_Click
        )
        self.btnCriar.grid(row=2, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnInserir=ttk.Button(
        self, text='Inserir'
        )
        self.btnInserir.grid(row=3, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnProcurar=ttk.Button(
        self, text='Procurar'
        )
        self.btnProcurar.grid(row=4, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnExcluir=ttk.Button(
        self, text='Excluir'
        )
        self.btnExcluir.grid(row=5, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnEditar=ttk.Button(
        self, text='Editar'
        )
        self.btnEditar.grid(row=6, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
    
    def btnConectar_Click(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conexao.cursor()
            sql = 'CREATE DATABASE IF NOT EXISTS curso_db'
            cursor.execute(sql)
            self.varResultado.set('Base de dados criada com sucesso.')
            self.lblResultado.configure(background='#99FF99')
        except:
            self.varResultado.set('Erro ao conectar com a base de dados.')
            self.lblResultado.configure(background='#FF9999')

    def btnCriarTabela_Click(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='curso_db'
            )
            cursor = conexao.cursor()
            sql = '''
                CREATE TABLE IF NOT EXISTS pessoas(
                    nome VARCHAR(50),
                    email VARCHAR(50),
                    PRIMARY KEY(email)
                )
            '''
            cursor.execute(sql)
            self.varResultado.set('Tabela criada com sucesso.')
            self.lblResultado.configure(background='#99FF99')
        except:
            self.varResultado.set('Erro ao criar tabela.')
            self.lblResultado.configure(background='#FF9999')
    def btnInserir_Click(self):
        
        pass
                
if __name__ == '__main__':
    app = App()
    app.mainloop()