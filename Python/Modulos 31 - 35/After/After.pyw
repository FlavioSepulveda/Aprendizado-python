import tkinter as tk
from tkinter import ttk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('After metodo')
        self.geometry('300x85')
        self.resizable(0,0)
        '''
            Utilizando o metodo after para checagem de processos.
            *after() -
                Ele chama um método callback que roda apos uma quantidade x de milesegundos;
                Ele se comporta como o metodo sleep() da biblioteca time
        '''
        
        self.style = ttk.Style(self)
        self.style.configure('TButton', font='Arial 12')

        self.button = ttk.Button(self, text='3 Seconds...')
        self.button['command'] = self.start
        self.button.pack(expand=True, padx=10, pady=10)

    def start(self):
        self.change_button_color('Red')
        # time.sleep(3)
        # self.change_button_color('Black')
        self.after(3000, self.change_button_color, 'Black')
        
        
    def change_button_color(self, color):
        self.style.configure('TButton', foreground=color)
        
    
        
if __name__=='__main__':
    app = App()
    app.mainloop()