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
box2 = tk.Label(root, text="Box1", bg='red', fg='white')
box2.pack(ipadx=10, ipady=10)
'''
    As funções ipadx e ipady servem para criar um espaçamento entre o conteudo e a borda do objeto.
'''
# Alterando a ordem dos packs ela vai mudar a ordem que os objetos são colocados na pagina da aplicação.


root.mainloop()