# Organização de arquivos: 25.3
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title()

# Centralzando a tela --------------------------------
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

largura_janela = 700
altura_janela = 500

centro_x = int(largura_tela/2 - largura_janela/2)
centro_y = int(altura_tela/2 - altura_janela/2)

root.geometry(f"{largura_janela}x{altura_janela}+{centro_x}+{centro_y}")

# Funções do botão -------------------------------------------
def log(event):
    print(event)
    # Mostrando chave do sistema
    print(f'KeySym...: {event.keysym}')
    # Mostrando o key code
    print(f'KeyCode...: {event.keycode}')
    # Mostrando o key sym num
    print(f'Keysym_num...: {event.keysym_num}')
    # Mostrando o char
    print(f'Char...: {event.char}')

# Criando botão ----------------------------------------------
# bot1 = ttk.Button(root, text='Botao!')
# bot1.bind("<Return>", log) 
# bot1.focus()
# bot1.pack() 

# # <modificador-tipo-detalhe>
# # <KeyPress-A>
# # <Alt-Control-KeyPress-KP_Delete>

# # Criando botão de ctrl ----------------------------------------
# bot2 = ttk.Button(root, text='Botão 2!')
# bot2.bind("<Any-KeyPress>", log)
# bot2.focus()
# bot2.pack()

# # Vinculando eventos na janela raiz
# root.bind("<Any-KeyPress>", log)

# Niveis de ligaçao -------------------------------------------------
# root.bind_class("Button", "<Any-KeyPress>", log)
# # Tres botões teste:
# btn1 = tk.Button(root, text="First Button!")
# btn1.focus()
# btn1.pack()

# btn2 = tk.Button(root, text="Second Button!")
# btn2.focus()
# btn2.pack()

# btn3 = ttk.Button(root, text="Third Button!")
# btn3.bind("<Any-KeyPress>", log)
# btn3.focus()
# btn3.pack()

# Desvinculação de eventos ----------------------------------------
botao1 = ttk.Button(root, text="Executar.")
botao1.bind("<Any-KeyPress>", log)
botao1.focus()
botao1.pack()
  
botao2 = ttk.Button(
    root,text="Desv.",
    command=lambda: botao1.unbind("<Any-KeyPress>")
)
botao2.pack()
  
botao3 = ttk.Button(root,text="Vinc.",command=lambda: botao1.bind("<Any-KeyPress>",log))
botao3.pack()
    
# Label ttk
label = ttk.Label(
    root,
    text="Label1 \nCurso de python tkinter.",    
    background='orange',
    foreground='blue'
)
label.pack()
# Propriedades da label
label2 = ttk.Label(
    root,
    text="Label2",
    background='red',
    padding=20,
    width=15,
    justify=tk.CENTER, # LEFT RIGHT CENTER
    anchor='center' # Posicionamento segundo a rosa dos ventos
).pack()

label3 = ttk.Label(
    root,
    text="Fontes",
    # font= "Arial 12 bold"
    font=("Verdana", 22, "bold")
)
label3.pack()
# imagem na label
# foto = tk.PhotoImage(file="Exercicios-python/arquivo-python.png")

# labelima = ttk.Label(
#     root,
#     image=foto
# ).pack()

# Bordas de labels
labelTeste = ttk.Label(
    root,
    text="Primeira",
    font="Arial 24",
    border=10,
    relief="groove"
).pack()

labelTeste2 = tk.Label(
    root,
    text="Segunda",
    font="Arial 24",
    borderwidth=10,
    relief='groove'
).pack()

'''
    Assim como o background o border pode ser declarado como bd.
'''
# Implicações de altura, largura e quebra de linhas.

estudo = tk.Label(
    root,
    text="0123456789",
    font='Arial 22',
    bd=5,
    relief='solid',
    width=5,
    height=2
).pack()
# No modulo ttk não temos o height então utilizamos o warplength pra criar outra linha
estudo2 = ttk.Label(
    root,
    text="0123456789",
    font='Arial 22',
    border=5,
    relief='solid',
    # width=5,
    wraplength=200 
    # Esta propriedade tambem existe no modulo tk.
).pack()

root.mainloop()