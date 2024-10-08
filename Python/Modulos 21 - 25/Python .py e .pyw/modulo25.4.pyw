import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("25.4")

# Centralizando 
root.geometry('700x500+350+100') # Medidas da minha tela que rezultam no meio da tela

# Underline 
label = ttk.Label(root, text="Cursor e label.",font="Arial 12 underline",cursor="hand2")
label.pack()

def Executar():
    root.quit()
    pass



botao = ttk.Label(root,text="Widget de botão.", font='Arial 12 underline', foreground='red').pack()
bot1  = ttk.Button(root, text="Click me.", command=Executar,)
bot1.state(['!disabled'])
bot1.pack()
bot2  = ttk.Button(root, text="Click me Lambda.", command=lambda: Executar()).pack()

# O botão pode entrar em estado de desabilitado
# Podemos acessar esse estado pelo metodo state.
bot3  = ttk.Button(root, text="Estados.", command=lambda: Executar())
bot3.state(['!disabled']) # pra reabilitar bot3.state(['!disabled'])
bot3.pack()

# Linakando o metodo de desabilitar a um botão
desbilitando = ttk.Button(root, text="Desabilitar", command=lambda: bot1.state(["disabled"])).pack()
abilitando = ttk.Button(root, text="Abilitar", command=lambda: bot1.state(["!disabled"])).pack()

# Criando botão de imagem
# botIcon = tk.PhotoImage(file="C:\Users\flavi\OneDrive\Desktop\Py\Aprendizado-python\Python\Modulos 21 - 25\Python .py e .pyw\imagens\arquivo-python.png")

# imagem = ttk.Button(root, image=botIcon)
# image.pack(ipadx= 5, ipady=5, expand=True)

def mostraInfo():
    # Quando o botão for clicado deve mostrar uma mensagem alertando que o botaõ foi acionado
    showinfo(title="Info", message="Click Click")
    pass

info = ttk.Button(root, text="Info", command=lambda: mostraInfo()).pack()

# # Criando botão com imagem e legenda
# imgBtn = tk.PhotoImage(file="Caminho do arquivo")

# imageBtn = ttk.Button(root,image=imgBtn,text="Nome da imagem",command=mostraInfo)
# imageBtn.pack(ipadx=5, ipady=5, expand=True)
# Entry - Text box
# Caixa de texto -
textBox = ttk.Entry(
    root
)
textBox.focus()
textBox.pack()
btnBox=ttk.Button(root,text="enviar", command=lambda: print(textBox.get())).pack()

# Textbox para senhas - 
# O método show oculta a senha para o usuario.
passWordBox = ttk.Entry(root, show="*").pack()

# Stringvar e text var -
'''
    String var é um tipo de variavel que serve para manipulação de texto.
'''
# Criando a string var que armazena o text box
texto1 = tk.StringVar()
# Define um valor padrão
texto1.set("Nome")

textBox2 = ttk.Entry(root, textvariable=texto1, font="Arial 12 italic")
# textBox2.focus()
textBox2.select_range(0,tk.END)
textBox2.pack()
botao2 = ttk.Button(root, text='Enviar...', command=lambda: print(texto1get())).pack()

# Se não for preenchido não envia nada
def textClick(event):
    if texto2.get() != "Nome" and texto2.get() != "":
        msg = f'Bem Vindo(a) {texto2.get()}!'
        showinfo(title="Informação", message=msg)
        texto2.set('Nome')
        textBox3.select_range(0, tk.END)
        textBox3.focus() 
    else:
        showinfo(title="Informação", message='Insira suas informações')

texto2 = tk.StringVar()
texto2.set('Nome')

# Manipulando eventos dentro da text box:
textBox3 = ttk.Entry(root, textvariable=texto2, font="Times 12 italic")
textBox3.select_range(0, tk.END)
textBox3.focus()
textBox3.bind("<Return>", textClick)
textBox3.pack()

botaoDeEnvio = ttk.Button(root, text='Confirma', command=textClick).pack()

root.mainloop()