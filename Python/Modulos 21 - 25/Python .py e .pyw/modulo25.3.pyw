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
root.bind_class("Button", "<Any-KeyPress>", log)
# Tres botões teste:
btn1 = tk.Button(root, text="First Button!")
btn1.focus()
btn1.pack()

btn2 = tk.Button(root, text="Second Button!")
btn2.focus()
btn2.pack()

btn3 = tk.Button(root, text="Third Button!")
btn3.focus()
btn3.pack()

root.mainloop()