# MODULO 33 - Validação Tkinter
import tkinter as tk
from tkinter import ttk
import re
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Validação tkinter')
         
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=2)
        
        ttk.Label(self, text='email: ').grid(row=0, column=0, padx=5, pady=5)
        
        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid))
        
        self.email_entry = ttk.Entry(self, width=50)
        self.email_entry.configure(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)
        self.email_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        
        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        self.send_button = ttk.Button(text='Enviar')
        self.send_button.grid(row=0, column=4, padx=5)
    
    def show_message(self, error="", color='black'):
        self.label_error['text'] = error
        self.email_entry['foreground'] = color
        
    def validate(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value) is None:
            return False
        
        self.show_message()
        return True
    
    def on_invalid(self):
        self.show_message('Por favor insira um email válido')
            
if __name__ == '__main__':
    app = App()
    app.mainloop()