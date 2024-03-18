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
        self.lblResultado.grid(row=0, column=0, columnspan=3,
                               padx=20, pady=10, sticky='nsew')

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
        self.frameLista.grid(row=3, column=0, columnspan=2,
                             rowspan=4, sticky='nsew', padx=20, pady=10)

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
        self.btnConectar = ttk.Button(
            self, text='Conectar',
            command=self.btnConectar_Click
        )
        self.btnConectar.grid(
            row=1, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnCriar = ttk.Button(
            self, text='Criar Tabela',
            command=self.btnCriarTabela_Click
        )
        self.btnCriar.grid(row=2, column=2, sticky='nsew',
                           padx=20, pady=6, ipadx=20)
        self.btnInserir = ttk.Button(
            self, text='Inserir',
            command=self.btnInserir_Click
        )
        self.btnInserir.grid(row=3, column=2, sticky='nsew',
                             padx=20, pady=6, ipadx=20)
        self.btnProcurar = ttk.Button(
            self, text='Procurar',
            command=self.btnProcurar_Click
        )
        self.btnProcurar.grid(
            row=4, column=2, sticky='nsew', padx=20, pady=6, ipadx=20)
        self.btnExcluir = ttk.Button(
            self, text='Excluir',
            command=self.btnExcluir_Click
        )
        self.btnExcluir.grid(row=5, column=2, sticky='nsew',
                             padx=20, pady=6, ipadx=20)
        self.btnEditar = ttk.Button(
            self, text='Editar',
            command=self.btnEditar_Click
        )
        self.btnEditar.grid(row=6, column=2, sticky='nsew',
                            padx=20, pady=6, ipadx=20)

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
        # O metodo strip remove espaços no  começo e fim das strings
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()

        reNome = re.fullmatch(r'\b[A-Za-z ]+\b', nome)
        reEmail = re.fullmatch(
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)

        if reNome is None:
            self.varResultado.set('O campo "Nome" é obrigatorio.')
            self.lblResultado.configure(background='#FF9999')
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set('O campo "Email" é obrigatorio.')
            self.lblResultado.configure(background='#FF9999')
            self.txtEmail.focus()
        else:
            try:
                conexao = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='curso_db'
                )
                cursor = conexao.cursor()
                sql = 'INSERT INTO pessoas (nome, email) VALUES (%s, %s)'
                values = (nome, email)
                cursor.execute(sql, values)
                conexao.commit()

                self.varResultado.set(str(cursor.rowcount) + 'registro(s) inserido(s).')
                self.lblResultado.configure(background='#99FF99')
                self.varNome.set('')
                self.varEmail.set('')
                self.txtNome.focus()
                self.btnProcurar_Click()
                
            except:
                self.varResultado.set('O registro não foi inserido.')
                self.lblResultado.configure(background='#FF9999')
    
    def btnProcurar_Click(self):
        self.txtLista.delete(*self.txtLista.get_children())
        
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='curso_db'
            )
            cursor = conexao.cursor()
            sql = 'SELECT * FROM pessoas ORDER BY nome ASC'
            
            if self.varNome.get() != '':
                sql = 'SELECT * FROM pessoas WHERE nome LIKE %s'
                val = (self.varNome.get(),)
                cursor.execute(sql, val)
            elif self.varEmail.get() != '':
                sql = 'SELECT * FROM pessoas WHERE email LIKE %s'
                val = (self.varEmail.get(),)
                cursor.execute(sql, val)                
            else:
                cursor.execute(sql)
            myresult = cursor.fetchall()
            for contato in myresult:
                self.txtLista.insert('', tk.END, values=contato)
                
            self.varResultado.set('')
            self.lblResultado.configure(background='#99FF99')
            self.txtNome.focus()
            
        except:
            self.varResultado.set('Erro ao buscar resultado.')
            self.lblResultado.configure(background='#FF9999')
    
    def btnExcluir_Click(self):
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()
        
        if nome == '' or email == '':
            self.varResultado.set('Por favor selecione um registro para a exclusão.')
            self.lblResultado.configure(background='#FF9999')
            self.txtNome.focus()
        else:
            try:
                conexao = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='curso_db'
                )
                cursor = conexao.cursor()
                sql = 'DELETE FROM pessoas WHERE nome = %s AND email = %s'
                values = (nome, email)
                cursor.execute(sql, values)
                conexao.commit()
                
                self.varNome.set('')
                self.varEmail.set('')
                self.btnProcurar_Click()
                # Verificando se o registro foi excluido
                if cursor.rowcount > 0:
                    self.varResultado.set('Registo apagado.')
                    self.lblResultado.configure(background='#99FF99')        
                    self.txtNome.focus()        
                else:
                    self.varResultado.set('Insira o registro que deseja excluir.')
                    self.lblResultado.configure(background='#FF9999')                          
                
            except:
                self.varResultado.set('Erro ao excluir registo.')
                self.lblResultado.configure(background='#FF9999')
                
    def btnEditar_Click(self):
        # nome = self.varNome.get().strip()
        # email = self.varEmail.get().strip()
        
        # reNome = re.fullmatch(r'\b[A-Za-z ]+\b', nome)
        # reEmail = re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
        
        # if len(self.txtLista.selection()) < 1:
        #     self.varResultado.set('Selecione um valor para editar.')
        #     self.lblResultado.configure(background='#FF9999')
        #     self.txtNome.focus()
        #     return
        
        # if reNome is None:
        #     self.varResultado.set('Digite um nome para editar.')
        #     self.lblResultado.configure(background='#FF9999')
        #     self.txtNome.focus()
            
        # elif reEmail is None:
        #     self.varResultado.set('Digite um email para editar.')
        #     self.lblResultado.configure(background='#FF9999')
        #     self.txtEmail.focus()
        # else:
        #     try:
        #         registro = self.txtLista.selection()[0]
        #         dadosRegistro = self.txtLista.item(registro) #retorna o item salvo em registro
        #         nomeRegistro = dadosRegistro['values'][0]
        #         emailRegistro = dadosRegistro['values'][0]
                
        #         conexao = mysql.connector.connect(
        #             host='localhost',
        #             user='root',
        #             password='',
        #             database='curso_db'
        #         )
        #         cursor = conexao.cursor()
        #         sql = 'UPDATE pessoas SET nome = %s AND email = %s WHERE nome = %s AND email = %s'
        #         values = (nome, email, nomeRegistro, emailRegistro)
        #         cursor.execute(sql, values)

        #         self.varNome.set('')
        #         self.varEmial.set('')
        #         self.btnProcurar_Click()
                
        #         self.varResultado.set('Registro editado com sucesso.')
        #         self.varLabel.configure(background='#99FF99')
        #         self.txtNome.focus()
                
        #     except:
        #         self.varResultado.set('Erro ao editar Registro.')
        #         self.lblResultado.configure(background='#FF9999')
                
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()

        reNome = re.fullmatch(r"\b[A-Za-z ]+\b", nome)
        reEmail = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

        if len(self.txtLista.selection()) < 1:
            self.varResultado.set("Selecione um registro para editar.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
            return
        
        if reNome is None:
            self.varResultado.set("O campo nome é obrigatório.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Insira um email válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtEmail.focus()
        else:
            try:
                registro = self.txtLista.selection()[0]
                dadosRegistro = self.txtLista.item(registro)
                nomeRegistro = dadosRegistro["values"][0]
                emailRegistro = dadosRegistro["values"][1]

                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="curso_db"
                )
                mycursor = conexao.cursor()
                sql = "UPDATE pessoas SET nome = %s, email = %s WHERE nome = %s AND email = %s"
                val = (nome, email, nomeRegistro, emailRegistro)
                mycursor.execute(sql, val)
                conexao.commit()

                self.varNome.set("")
                self.varEmail.set("")

                self.btnProcurar_Click()

                self.varResultado.set("Registro alterado com sucesso.")
                self.lblResultado.configure(background="#99FF99")
                self.txtNome.focus()
            except:
                self.varResultado.set("Erro ao editar registro.")
                self.lblResultado.configure(background="#FF9999")
                
if __name__ == '__main__':
    app = App()
    app.mainloop()
