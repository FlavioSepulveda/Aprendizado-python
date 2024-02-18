# MODULO 27 - Widgets Tekinter e Ttk(GUI)
from tkinter import Tk, Text, ttk


root = Tk()
root.title('Modulo 27 - TTK(GUI)')
# root.resizable(0, 0)
# Introdução ao FRAME
'''
	Serve pra organizar um widget a nivel de codificação.
	*Comparavel a um container
'''
frame1 = ttk.Frame(
	root,
	width=400,
	height=300,
	borderwidth=25,
	relief='solid',
	padding=(10, 50, 10, 50) # -> (Left, top, right, bottom)
	)
frame1.pack()
# Ele tem suas caracteristicas mas não é visivel por ser um container.
# Posso colocar widgets dentro do frame
label1 = ttk.Label(
	frame1,	
 	text='Primeiro label pro frame',
	background='yellow'
).pack()

label2 = ttk.Label(
	frame1,
	text='O Segundo label do frame',
	background='green'
).pack()
# Widget text - exibe e permite a alteração de textos
# Criando caixa de texto com fonte arial tamanho 12, fundo amarelo e cor vermelha
text = Text(root,height=8,font='Arial 12',background='yellow',foreground='red')
text.pack()
text.insert('1.0','Insira seu texto')
txt = text.get('1.0', '1.4')

# Ativando e desativando o  widget text -
# # Alterando a propriedade state do widget.
# text['state'] = 'disabled'
# # Para reabilitar mudamos para 'Normal'
# text['state'] = 'normal'

# criando botão que desablita 
ttk.Button(root, text="desabilita", command=lambda: text.config(state='disabled')).pack()
# Botão que reativa
ttk.Button(root, text="reabilita", command=lambda: text.config(state='normal')).pack()

root.mainloop()