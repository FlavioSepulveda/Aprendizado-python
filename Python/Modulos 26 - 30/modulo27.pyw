# MODULO 27 - Widgets Tekinter e Ttk(GUI)
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title('Modulo 27 - TTK(GUI)')
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
# # root.resizable(0, 0)
# Introdução ao FRAME
'''
	Serve pra organizar um widget a nivel de codificação.
	*Comparavel a um container
'''
st = ScrolledText(root, width=50, height=10, font='Arial 24')
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# frame1 = ttk.Frame(
# 	root,
# 	width=400,
# 	height=300,
# 	borderwidth=25,
# 	relief='solid',
# 	padding=(10, 50, 10, 50) # -> (Left, top, right, bottom)
# 	)
# frame1.pack()
# # # Ele tem suas caracteristicas mas não é visivel por ser um container.
# # Posso colocar widgets dentro do frame
# label1 = ttk.Label(
# 	frame1,	
#  	text='Primeiro label pro frame',
# 	background='yellow'
# ).pack()

# label2 = ttk.Label(
# 	frame1,
# 	text='O Segundo label do frame',
# 	background='green'
# ).pack()
# # Widget text - exibe e permite a alteração de textos
# # Criando caixa de texto com fonte arial tamanho 12, fundo amarelo e cor vermelha
# text = Text(root,height=8,font='Arial 12',background='yellow',foreground='red')
# text.pack()
# text.insert('1.0','Insira seu texto')
# txt = text.get('1.0', '1.4')

# Ativando e desativando o  widget text -
# # Alterando a propriedade state do widget.
# text['state'] = 'disabled'
# # Para reabilitar mudamos para 'Normal'
# text['state'] = 'normal'

# criando botão que desablita 
# ttk.Button(root, text="desabilita", command=lambda: text.config(state='disabled')).pack()
# # Botão que reativa
# ttk.Button(root, text="reabilita", command=lambda: text.config(state='normal')).pack()

# Widget de barra de rolagem - ela é um item independente
# text = tk.Text(root, height=8, font='Arial, 12').pack()
# text.grid(row=0, column=0, sticky="ew")
# # Barra de rolagem
# roll = ttk.Scrollbar(root, orient='vertical', command=text.yview)
# roll.grid(row=0, column=1, sticky='ns')
# # O text faz isso com o intermedio da 'yscrollcommand'
# text['yscrollcommand'] = roll.set
# # Ele ativa ela apenas quando a barra de rolagem esta ativa
# Scroll de teste


root.mainloop()