import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview')
root.resizable(0, 0)
root.geometry('600x300')

columns = ('Nome', 'Sobrenome', 'Email')
tree = ttk.Treeview(root, columns=columns, show='headings')
# 'Tree', 'Tree headings' e 'headings', ''
tree.heading('Nome', text='Nome')
tree.heading('Sobrenome', text='Sobrenome')
tree.heading('Email', text='Email')

tree.insert("", tk.END, values=('Natsuki', 'Subaru', 'xxxxxx@gmail.com'))
tree.insert("", tk.END, values=('Vanastrea', 'Reinhard', 'xxxxxx@gmail.com'))
tree.insert("", tk.END, values=('Tinsel', 'Garfield', 'xxxxxx@gmail.com'))
tree.insert("", tk.END, values=('Vanastrea', 'Willhealm', 'xxxxxx@gmail.com'))
tree.insert("", tk.END, values=('Batenkaitos', 'Lyee', 'xxxxxx@gmail.com'))

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)

tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')


root.mainloop()
