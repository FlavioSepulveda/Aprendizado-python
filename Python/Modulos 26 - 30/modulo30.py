# MODULO 30 - Temas e Estilos do Tkinter
#
# Importando bibliotecas
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter temas')
        self.geometry('700x500')

        self.style = ttk.Style(self)

        config = {'padx': 10, 'pady': 10, 'sticky': 'w'}

        # label -
        label = ttk.Label(self, text='Nome: ')
        label.grid(column=0, row=0, **config)

        # entry -
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, **config)

        # button -
        btn = ttk.Button(self, text='executar')
        btn.grid(column=2, row=0, **config)

        # Radio button -
        self.selected_theme = tk.StringVar()
        them_frame = ttk.LabelFrame(self, text='Temas')
        them_frame.grid(padx=10, pady=10, ipadx=30, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                them_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.theme_change
            )
            rb.pack(expand=True, fill='both')
            
    def theme_change(self):
        self.style.theme_use(self.selected_theme.get())

if __name__ == '__main__':
    app = App()
    app.mainloop()
