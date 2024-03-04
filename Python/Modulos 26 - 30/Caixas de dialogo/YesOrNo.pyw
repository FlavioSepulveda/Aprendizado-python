import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sim ou Não')
        self.geometry('700x500')
        
        options = {'padx':5,'pady':5}
        
        ttk.Button(
            self,
            text='Sair',
            command=self.confirm
        ).pack(expand=True, **options)
        
    def confirm(self):
        result = askyesno(title='Confirme', message='Confirma a operação?')
        if result:
            self.destroy()
        
if __name__=='__main__':
    app = App()
    app.mainloop()