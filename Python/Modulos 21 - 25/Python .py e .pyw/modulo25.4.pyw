import tkinter as tk
from tkinter import ttk

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

root.mainloop()