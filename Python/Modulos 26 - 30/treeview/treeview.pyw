import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview')
root.resizable(0, 0)
root.geometry('650x300')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Lista
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'nome {n}', f'sobrenome {n}', f'email{n}@gmail.com'))

# columns = ('Nome', 'Sobrenome', 'Email')
# tree = ttk.Treeview(root, columns=columns, show='headings')
# # 'Tree', 'Tree headings' e 'headings', ''
# tree.heading('Nome', text='Nome', anchor=tk.W)
# tree.heading('Sobrenome', text='Sobrenome', anchor=tk.W)
# tree.heading('Email', text='Email', anchor=tk.CENTER)

# tree.column('Nome', width=100, anchor=tk.W)
# tree.column('Sobrenome', width=100, anchor=tk.W)
# tree.column('Email', width=300,anchor=tk.CENTER)

# tree.insert("", tk.END, values=('Natsuki', 'Subaru', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Vanastrea', 'Reinhard', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Tinsel', 'Garfield', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Vanastrea', 'Willhealm', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Batenkaitos', 'Lyee', 'xxxxxx@gmail.com'))
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)

# def item_selected(event):
#     for selected_item in tree.selection():
#         tree.delete(selected_item)


# tree.bind('<<TreeviewSelect>>', item_selected)
# tree.grid(row=0, column=0, sticky='nsew')

# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')

tree = ttk.Treeview(root, columns=('text'), show='tree headings')
tree.heading('text', text='Departamentos', anchor='w')

tree.insert('', tk.END, values=('Administração'), iid=0, open=False)
tree.insert('', tk.END, values=('Logistica'), iid=1, open=False)
tree.insert('', tk.END, values=('Vendas'), iid=2, open=False)
tree.insert('', tk.END, values=('Financeiro'), iid=3, open=False)
tree.insert('', tk.END, values=('TI'), iid=4, open=False)

# Dados filhos -
tree.insert('0', tk.END, values=('Gabriel'), iid=5, open=False)
tree.insert('3', tk.END, values=('Dani'), iid=6, open=False)
tree.insert('2', tk.END, values=('Arthur'), iid=7, open=False)

tree.move(3, 2, tk.END)

tree.grid(row=0, column=0, sticky='nsew')


root.mainloop()
