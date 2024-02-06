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


root.mainloop()