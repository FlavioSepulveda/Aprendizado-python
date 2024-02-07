# MODULO 26 - Gerenciadores de Geometria Tkinter (GUI)
# Importando as bibliotecas/frameworks -
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Iniciando o modulo Tkinter
root = tk.Tk()
root.title("Gerenciadores de Geometria")

root.geometry('700x500+350+150')

# Criando os assuntos do módulo -
# Criando o box 1 -
box1 = tk.Label(root, text="Box1", bg='green', fg='white')
box1.pack(ipadx=10, ipady=10)
# Criando o box 2 -
box2 = tk.Label(root, text="Box2", bg='red', fg='white')
box2.pack(ipadx=10, ipady=10)
'''
    As funções ipadx e ipady servem para criar um espaçamento entre o conteudo e a borda do objeto.
'''
# Alterando a ordem dos packs ela vai mudar a ordem que os objetos são colocados na pagina da aplicação.

# Preenchimento de geometria pack.
# Criando o box 3 -
box3 = tk.Label(root, text="Box3", bg='blue', fg='white')
box3.pack(ipadx=10, ipady=10, fill='x')
# Criando o box 4 -
box4 = tk.Label(root, text="Box4", bg='black', fg='white')
box4.pack(ipadx=10, ipady=10, fill="x")
# O metodo fill preenche o espaço com base no eixo x ou y.
#  As opções desse método são: 'x', 'y' e 'both'


root.mainloop()