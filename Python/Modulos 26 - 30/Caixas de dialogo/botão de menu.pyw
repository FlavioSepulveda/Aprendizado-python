import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry('700x500')
        
        # Variaveis do menu
        self.selected_color = tk.StringVar()
        self.selected_color.trace_add('write', self.menu_item_selected)
        
        colors = ('Red', 'Green', 'Blue', 'White')
        menu_button = ttk.Menubutton(self, text='Select the color')
        menu = tk.Menu(menu_button, tearoff=False)
        for cor in colors:
            menu.add_radiobutton(
                label=cor, 
                value=cor, 
                variable=self.selected_color)
        
        menu_button['menu'] = menu
        menu_button.pack(expand=True)
        
    def menu_item_selected(self, *args):
        self.configure(bg=self.selected_color.get())

if __name__ == '__main__':
    app = App()
    app.mainloop()
