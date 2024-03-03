# widget notebook
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Python Notebook')
root.geometry('600x400')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

label1 = ttk.Label(frame1, text='Ola')
label2 = ttk.Label(frame2, text='eae')
label1.pack()
label2.pack()

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Informação geral')
notebook.add(frame2, text='Menu inicial')

ttk.Button(
    root,
    text='Mostrar',
    command=lambda: notebook.add(frame1, text='Informação geral')
).pack()
ttk.Button(
    root,
    text='Menu',
    command=lambda: notebook.add(frame2, text='Menu inicial')
).pack()
ttk.Button(
    root,
    text='Esconder 1',
    command=lambda: notebook.hide(0)
).pack()
ttk.Button(
    root,
    text='Esconder 2',
    command=lambda: notebook.hide(1)
).pack()
ttk.Button(
    root,
    text='Apagar 1',
    command=lambda: notebook.forget(0)
).pack()
ttk.Button(
    root,
    text='Apagar 2',
    command=lambda: notebook.forget(1)
).pack()

root.mainloop()
