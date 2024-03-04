import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.messagebox import WARNING      

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Ask Ok/Cancel')
        self.geometry('700x500')
        
        ttk.Button(
            self,
            text='Sair',
            command=self.confirm
        ).pack(expand=True)
        
    def confirm(self):
        result = askokcancel(title='Confirme', message='Confirma a operação?')
        if result:
            # Codigo de exclusão dos dados
            # Exibir mensagem sobre status da operação.
            showinfo(title="Status da operação", message='Operação completa', icon=WARNING)
        
    
if __name__=='__main__':
    app = App()
    app.mainloop()
        