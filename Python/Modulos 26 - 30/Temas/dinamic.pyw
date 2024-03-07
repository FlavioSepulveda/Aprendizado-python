import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alteração dinamica')
        self.geometry('300x115')
        self.resizable(0, 0)

        button = ttk.Button(
            self,
            text='Executar'
        )
        button.pack(expand=True)

        style = ttk.Style(self)
        style.configure('TButton', font=('Arial', 12))
        style.map('TButton',foreground=[('pressed', 'blue'),('active', 'white')])

if __name__ == '__main__':
    app = App()
    app.mainloop()
