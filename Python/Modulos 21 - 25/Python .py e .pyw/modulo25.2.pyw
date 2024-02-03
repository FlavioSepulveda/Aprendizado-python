# Arquivo Terminado em .pyw
'''
    Arquivos terminados em ".pyw" são arquivos cujo NÃO existe uma necessidade do uso do console para executar.
'''
import tkinter as tk
from tkinter import ttk

# Adcionando retorno ao botão
def OlaMundo():
    # Alem do nome da cor podemos colocar no formato hexadecimal
    root.config(background='Pink')
    print('Mudei a cor')
    
root = tk.Tk()
# Definindo o titulo da aplicação
root.title("App Test 01")
titulo = root.title()
# Dimensionando a janela
# root.geometry("600x400+500+500")
# Centalizando a janela

# Guardando a largura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

largura_janela = 700
altura_janela = 500

# Obtendo as dimensões da tela
# Encontrando o ponto central-
centro_x = int(largura_tela/2 - largura_janela/2)
centro_y = int(altura_tela/2 - altura_janela/2)

# Definindo a posição no centro

root.geometry(f"{largura_janela}x{altura_janela}+{centro_x}+{centro_y}")

# O método resizable() permite ao usuário redimensionar a janela da aplicação.
# Quando o parâmetro é 0 significa que a janela nao pode ser redimensionada.
# Quando o parâmetro é 1 significa que a janela pode ser redimensionada.
# root.resizable(0,0)
# root.resizable(1,1)
root.resizable(True, True)
# Dentro do parâmetro os dois valores booleanos, indicam altura e largura.
# root.resizable(True,True)
# O tamanho da janela por padrão ja vem como 1, com isso podemos por meio dos metodos
#minsize() e maxsize() delimitar um limite.
root.minsize(300,200)
root.maxsize(700,500) 
# Assim posso redimensionar do tamanho que eu quiser, mas sem ultrapassar esses limites.

# Tipos de apresentação da aplicação - 
# Apresentação maximizada 
#root.state('zoomed')
# Apresentação normal
root.state('normal')
# Apresentação minimizada 
#root.state('iconic')

# Para ver o codigo de resultado 
print(root.state())
root.title(root.state())
# Mudando a transparencia da aplicação
# Os valores vão de 0.0 ate 1.0 sendo 00 totalmente transparente e 1.0 totalmente visivel.
root.attributes("-alpha", 1)
# Ordem de empilhamento da janela.
# Garante que a minha aplicação sempre esteja no topo ao se manusear outros aplicativos.
root.attributes("-topmost", 1)

# Para mover uma janela para cima - Tras pro inicio da fila
# root.lift()

# Para mover a janela para baixo - Leva pro final da fila
# root.lower()

# O topmost garante que ela sempre fique no topo.
# Alterando o icone do arquivo
# Deve ser no formato .ico
root.iconbitmap("arquivo-python.png")
# Widgets tematicos no tkinter

# A biblioteca ttk é responsavel pela criação de widgets tematicos sempre que disponiveis. 

# Criando uma label do jeito classico
# lbl = tk.Label(root, text='Exemplo 1')
# lbl.pack()

# Criando de uma maneira um pouco mais elaborada
# tk.Label(root, text='Exemplo 2').pack()

# # Usando o ttk
# ttk.Label(root, text='Exemplo 3').pack()

# # Widget de botão
# # Com o tkinter apenas
# tk.Button(root, text='Botão 1').pack()
# ttk.Button(root, text='Botão 2').pack()

# Definindo atributos
ttk.Label(root, text='Ola mundo').pack()

# Podemos fazer a atribuição por meio de indice com palavras chave
lbl1 = ttk.Label(root)
lbl1["text"] = "Outro ola mundo"
lbl1.pack()

# Mas tambem adcionar o atributo config
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um ola mundo.")
lbl2.pack()

# Criando o botão

btn = ttk.Button(root, text='Ola', command=OlaMundo).pack()

# Argumentos de comando
# Primeiramente definimos uma função
# Dentro dos parametros determinamos o argumento que a função ira receber
def select(argumento):
    root.config(background= argumento)

# Usaremos uma função lambda pra chamar o evento
# criando o botão;
ttk.Button(
    root,
    text = "Mude a cor.",
    command= lambda: select("red")
).pack()
# Agora o a função ira realizar o evento conforme a cor repassada pela sua variavel.

# Limitação de comandos
'''
    Os comandos respondem a alguns botões e se limitam a alguns widgets como o de botão por exemplo, sendo acionado pelo botão esquerdo do mouse e não pelo direito, e pelo botão de espaço mas não pelo enter.
'''

# Associação de eventos Tkinter
# Função do notão enter
def button_pressed(event):
    print('Botão pressionado')
    
ente = ttk.Button(root, text='enter')
ente.bind("<Return>", button_pressed)
ente.focus()
ente.pack(expand=True)

root.mainloop()