# MODULO 27 - Widgets Tekinter e Ttk(GUI)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
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


root.mainloop()