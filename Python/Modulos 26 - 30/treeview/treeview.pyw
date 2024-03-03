import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview')
root.resizable(0, 0)
root.geometry('650x300')

# Lista
contacts = []
for n in range(1, 100):
    contacts.append((f'nome {n}', f'sobrenome {n}', f'email{n}@gmail.com'))

columns = ('Nome', 'Sobrenome', 'Email')
tree = ttk.Treeview(root, columns=columns, show='headings')
# 'Tree', 'Tree headings' e 'headings', ''
tree.heading('Nome', text='Nome')
tree.heading('Sobrenome', text='Sobrenome')
tree.heading('Email', text='Email')

# tree.insert("", tk.END, values=('Natsuki', 'Subaru', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Vanastrea', 'Reinhard', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Tinsel', 'Garfield', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Vanastrea', 'Willhealm', 'xxxxxx@gmail.com'))
# tree.insert("", tk.END, values=('Batenkaitos', 'Lyee', 'xxxxxx@gmail.com'))
for contact in contacts:
    tree.insert('', tk.END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        tree.delete(selected_item)


tree.bind('<<TreeviewSelect>>', item_selected)
tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

root.mainloop()
