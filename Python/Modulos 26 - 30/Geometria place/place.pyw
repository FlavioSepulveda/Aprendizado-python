import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Geometria place")
root.geometry('700x500+350+150')

# Definindo labels --------------------------------------------
label1 = ttk.Label(
    root,
    text='Exemplo',
    background= 'red',
    foreground='white',
    font='Arial 12'
)
label1.place(x=20, y=20)

# Place relativo ---------------------------------------------------
label2 = ttk.Label(
    root,
    text='Exemplo',
    background= 'blue',
    foreground='white',
    font='Arial 12'
)
# Aqui usamos pontos flutuantes
label2.place(relx=0.8, rely=0.2, anchor=tk.N)

root.mainloop()