import tkinter as tk
from tkinter import ttk
import time as tm


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Relogio Digital')
        self.resizable(0, 0)
        self.geometry('500x160+450+300')
        self['bg'] = 'black'

        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='Black', foreground='Red')

        # label -
        self.label = ttk.Label(
            self,
            text=self.time_string(),
            font=('Digital-7', 60)
        )
        self.label.pack(expand=True)
        self.label.after(990, self.update)

    def time_string(self):
        # Retrorna uma string formatada com as horas
        return tm.strftime('%H:%M:%S')

    def update(self):
        self.label.configure(text=self.time_string())
        self.label.after(1000, self.update)

if __name__ == '__main__':
    clock = DigitalClock()
    clock.mainloop()
