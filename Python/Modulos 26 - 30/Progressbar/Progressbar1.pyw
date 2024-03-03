# Exemplos do uso do widget barra de progresso - Indeterminado
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Barra do tipo indeterminado')
root.resizable(0, 0)
root.geometry('500x400')
root.grid()

progressbar = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
progressbar.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

btStart = ttk.Button(
    root,
    text='start',
    command=lambda: progressbar.start(10)
)
btStart.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

btStop = ttk.Button(
    root,
    text='stop',
    command=lambda: progressbar.stop()
)
btStop.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()
