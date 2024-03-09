import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('After metodo')
        self.geometry('300x160+450+300')
        self.resizable(0,0)
        
        self.tarefas = randint(1, 10)
        
    #    Progress bar --
        self.pb = ttk.Progressbar(self,orient='horizontal',mode='determinate',length=280)
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
    
    #    Label --
        self.value_label = ttk.Label(self, text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)
    
    #    Buttons --
        start_button = ttk.Button(self,text='Start', command=self.progress)
        start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
        stop_button = ttk.Button(self,text='Stop', command=self.stop)
        stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
       
    def update_progress_label(self):
        return f'Progresso: {round(self.pb["value"], None)}%...'
    
    def progress(self):
        if self.pb['value'] < 100:
            self.pb['value'] += (100/self.tarefas)
            self.value_label['text'] = self.update_progress_label()
            
            # Tarefa a ser executada vem aqui -
            self.after(randint(100, 3000)) # Quando for usar troque isso pelo codigo que será utilizado.
            
            self.id = self.after_idle(self.progress)
            print(self.id)
        else:
            self.pb['value'] = 100
            self.value_label['text'] = self.update_progress_label()
            showinfo(message="Processo concluido!")
    
    def stop(self):
        self.pb.stop()
        self.value_label['text'] = self.update_progress_label()
        self.after_cancel(self.id)
        
        
if __name__=='__main__':
    app = App()
    app.mainloop()