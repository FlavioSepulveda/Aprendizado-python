# MODULO 26 - Gerenciadores de Geometria Tkinter (GUI)
# Importando as bibliotecas/frameworks -
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Iniciando o modulo Tkinter
root = tk.Tk()
root.title("Gerenciadores de Geometria")

# root.columnconfigure(index=0, weight=2)
# root.rowconfigure(index=0, weight=1)

root.geometry('250x150+350+150')

# Configurando a grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# Criando os assuntos do módulo -
# Criando o box 1 -
box1 = tk.Label(root, text="Box1", bg='green', fg='white')
box1.pack(ipadx=10, ipady=10)
# # Criando o box 2 -
box2 = tk.Label(root, text="Box2", bg='red', fg='white')
box2.pack(ipadx=10, ipady=10)
# '''
#     As funções ipadx e ipady servem para criar um espaçamento entre o conteudo e a borda do objeto.
# '''
# # Alterando a ordem dos packs ela vai mudar a ordem que os objetos são colocados na pagina da aplicação.

# # Preenchimento de geometria pack.
# # Criando o box 3 -
box3 = tk.Label(root, text="Box3", bg='blue', fg='white')
box3.pack(ipadx=10, ipady=10, fill='x')
# # Criando o box 4 -
box4 = tk.Label(root, text="Box4", bg='black', fg='white')
box4.pack(ipadx=10, ipady=10, fill="x")
# # O metodo fill preenche o espaço com base no eixo x ou y.
# #  As opções desse método são: 'x', 'y' e 'both'

# # Usando a opção de expansão

# # Criando o box 6 -
box6 = tk.Label(root, text="Box6", bg='pink', fg='white')
box6.pack(ipadx=10, ipady=10, expand=True, fill='both',side='left')
# # O expand expande uma area para preenchimento quando os widgets possuem a mesma ancora.

# # A opção side - muda a criação dos widgets 
# # Criando o box 5 -
box5 = tk.Label(root, text="Box5", bg='yellow', fg='white')
box5.pack(ipadx=10, ipady=10, expand=True,fill="both", side='left')

# Quando o usar o gerenciador de geometria pack:
'''
    É adequado para colocar widgets de cima para baixo e lado a lado.
'''

#  Gerenciador Grid -
# As colunas e linhas dependem do tamnho e largura das linhas.

# Pra configurar usamos o seguinte comando
root.columnconfigure(index=0, weight=2)
root.rowconfigure(index=0, weight=1)

# Posicionando widgets na grade
# nomeDoWidget.grid(**Opções)

'''
    O método grid() possui os seguintes parametros:
    *column      : O column Indica a coluna que voce quer colocar o widget.
    *row         : O row indica a linha que ele ira se encontrar.
    *rowspan     : O rowspan indica o numero de linhas adjacentes que ira ocupar.
    *columnspan  : O columnspan indica o numero de colunas adjacentes.
    *sticky      : O sticky se a célula for maior doque o widget ele define o preenchimento.
    *padx        : Adciona o preenchimento a cima e abaixo.
    *pady        : Adciona o preenchimento na esquerda e direita.
    *ipadx        : Adciona o preenchimento interno a cima e abaixo.
    *ipady        : Adciona o preenchimento interno na esquerda e direita.
'''

'''
    *O sticky possui os seguintes valores -
    * NW - Nort West
    * N - North
    * NE - Nort East
    * E - East
    * SE - South East
    * S - South
    * SW - South West
    * W - West
    
'''

# Uso do gerenciamento de grid
# Pra esse exemplo vamos usar 2 colunas e 3 linhas

# Criando os widgets
# Username -------------------------------------------------------
username_label = ttk.Label(root, text='Username: ', font="Arial 12")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# Senha ----------------------------------------------------------
user_password = ttk.Label(root, text="Password: ", font="Arial 12")
user_password.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

userPass_entry = ttk.Entry(root, show='*')
userPass_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Botão de login ------------------------------------------------
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

# O place voce usa as funç x e y
# Voce chama ele com: nome.place(**Opções)
# So é util quando voce quer que o usuario decida onde vão ficar os itens.



root.mainloop()