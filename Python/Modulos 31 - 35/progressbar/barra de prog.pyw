import tkinter as tk
from tkinter import ttk
from random import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('After metodo')
        self.geometry('300x160+450+300')
        self.resizable(0,0)
        
        self.tarefas = randint(1, 10)
        
    #    Progress bar --
        self.pb = ttk.Progressbar(
            self,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
    
    #    Label --
        self.value_label = ttk.Label(self, text='')
        self.value_label.grid(column=0, row=1, columnspan=2)
    
    #    Buttons --
        start_button = ttk.Button(
            self,
            text='Start',
        )
        start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
        
        stop_button = ttk.Button(
            self,
            text='Stop'
        )
        stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
if __name__=='__main__':
    app = App()
    app.mainloop()