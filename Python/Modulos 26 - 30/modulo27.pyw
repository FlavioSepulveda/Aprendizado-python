# MODULO 27 - Widgets Tekinter e Ttk(GUI)
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Modulo 27 - TTK(GUI)')
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
root.resizable(0, 0) # Garantindo que seja redimencionavel
root.geometry('700x500')
# Introdução ao FRAME
'''
	Serve pra organizar um widget a nivel de codificação.
	*Comparavel a um container
'''
# st = ScrolledText(root, width=50, height=10, font='Arial 24')
# st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
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
# widget separador
# usamos o método separator
# ttk.Label(root, text='primeiro label', font='Arial 24').pack(side='left')

# separador = ttk.Separator(root, orient='vertical')
# separador.pack(fill='y', side='left')

# ttk.Label(root, text='segundo label', font='Arial 24').pack(side='left')
# Check box
# concordar = tk.StringVar()

# def resultadoCheck():
#     showinfo('Resulado', f'O usuario: {concordar.get()}')

# ttk.Checkbutton(root,
#                 text='Clica ai man',
#                 variable=concordar,
#                 # command=lambda: print(concordar.get()),
#                 command=resultadoCheck,
#                 onvalue='concorda',
#                 offvalue='não concorda').pack()

# Criando radio buttons
'''
	cada radio buttom possui um balor diverente.
'''
# selected_size = tk.StringVar()


# ttk.Label(root, text='Qual o tamanho da sua camiseta?')

# ttk.Radiobutton(root,
#                 text='pequena',
#                 value='p',
# 				variable=selected_size
# ).pack(fill='x', padx=5, pady=5)
# ttk.Radiobutton(root,
#                 text='media',
#                 value='m',
# 				variable=selected_size
# ).pack(fill='x', padx=5, pady=5)
# ttk.Radiobutton(root,
#                 text='grande',
#                 value='g',
# 				variable=selected_size
# ).pack(fill='x', padx=5, pady=5)

# ttk.Button(root, text='Seleção', command=lambda: showinfo('Confirme sua escolha.', f'Tamanho escolhido: {selected_size.get()}')).pack(fill='x', padx=5, pady=5)
# Combo box-
# selected_day = tk.StringVar()
# def cb_result(event):
#     showinfo(title='Resultado', message=f'voce selecionou: {day_cb.get()}')
# # Permite selecionar um valor em um grupo de valores.
# day_cb = ttk.Combobox(root,
#                     state='readonly',
#                     textvariable=selected_day
# )
# day_cb['values'] = ['Domingo','Segunda','Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
# # day_cb.set('Domingo')
# selected_day.set('Segunda')
# day_cb.bind('<<ComboboxSelected>>', cb_result)
# day_cb.pack(fill='x', padx=5, pady=5)
# Listbox -
# langs = ('Java', 'c', 'c++', 'python', 'go', 'javascript', 'swift')
# langs_var = tk.StringVar(value=langs)

# listbox = tk.Listbox(
#     root,
#     listvariable=langs_var,
#     height=6,
#     font='Arial 12',
#     # O outro modo é o extend permite a seleção de mais de um com o botão ctrl do teclado.
#     selectmode='browse'
# )
# listbox.grid(column=0, row=0, sticky='nwes')


# scrollbar = ttk.Scrollbar(
#     root,
#     orient='vertical',
#     command=listbox.yview
# )
# listbox['yscrollcommand'] = scrollbar.set
# scrollbar.grid(
# 	column=1,
# 	row=0,
# 	sticky='ns'
# )

# def item_selecionado(event):
#     selected_indices = listbox.curselection()
#     for i in selected_indices:
#         print(listbox.get(i))


# listbox.bind('<<ListboxSelect>>', item_selecionado)

# tkinter slider
# currentValue = tk.DoubleVar()


# def slider_change(event):
#     # print(currentValue.get())
#     val = slider.get()
#     print("{: .2f}".format(val))


# '''
# 	O slider precisa ter o event para evitar um erro em sua sintaxe.
# '''

# slider = ttk.Scale(
#     root,
#     from_=0,
#     to=100,
#     variable=currentValue,
#     command=slider_change
# )
# slider.pack()
# # Para desativar ou ativar precisamos mudar o estado do slider:
# slider['state']

# ttk.Button(
#     root,
#     text='Desligar',
#     command=lambda: slider.configure(state='disabled')
# ).pack()
# ttk.Button(
#     root,
#     text='Ligar',
#     command=lambda: slider.configure(state='normal')
# ).pack()
#

# current_value = tk.StringVar(value=0)


# def value_changed():
#     print(current_value.get())


# valores = (0, 2, 4, 6, 8, 10)

# spinbox = ttk.Spinbox(root,
# 					# from_=0,
# 					# to=100,
# 					textvariable=current_value,
# 					font='Arial 12',
# 					command=value_changed,
# 					wrap=True,
# 					values=valores
# 					)
# spinbox.pack()
# sg = ttk.Sizegrip(root)
# sg.grid(row=1, sticky='SE')
# lf = ttk.Labelframe(root, text='Alinhamento',labelanchor='n')
# lf.grid(column=0, row=0, padx=20, pady=20)

# stringvar = tk.StringVar()

# rb1 = ttk.Radiobutton(lf, text='Esquerda',value='E',textvariable=stringvar)
# rb1.grid(column=0, row=0, ipadx=10, ipady=10)
# rb2 = ttk.Radiobutton(lf, text='meio',value='C',textvariable=stringvar)
# rb2.grid(column=1, row=0, ipadx=10, ipady=10)
# rb2 = ttk.Radiobutton(lf, text='direita',value='D',textvariable=stringvar)
# rb2.grid(column=2, row=0, ipadx=10, ipady=10)

# Barra de progresso:
# pb=ttk.Progressbar(
# 	root,
# 	orient='horizontal', # Vertical
# 	length=300,
# 	mode='determinate' # indeterminate
# )
# pb.pack()
# pb.start()



root.mainloop()
