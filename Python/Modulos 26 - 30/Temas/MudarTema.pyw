import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Minha aplicação em POO')
        self.geometry('400x200')
        self.resizable(0, 0)
        
        '''
            Cada widget tem uma variavel de tema diferente.
        '''
        tButton = ttk.Button(
            self,
            text='Click me!',
            command=lambda: print(tButton.winfo_class())
        )
        tButton.pack(expand=True)


if __name__ == '__main__':
    app = App()
    app.mainloop()
