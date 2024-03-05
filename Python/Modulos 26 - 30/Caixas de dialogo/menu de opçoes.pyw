import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry('700x500')
        
        self.languages = ('python', 'JavaScript', 'Java', 'Swift', 'Golang', 'C#', 'C++', 'Scala')
        self.option_var = tk.StringVar(self)
        
        paddings = {'padx':5, 'pady':5}
        
        label = ttk.Label(self, text='Select your favorite language')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_change
        )
        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)
        
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        
    def option_change(self, *args):
        self.output_label['text'] = f'Voce selecionou: {self.option_var.get()}'
        
        
    

if __name__ == '__main__':
    app = App()
    app.mainloop()
