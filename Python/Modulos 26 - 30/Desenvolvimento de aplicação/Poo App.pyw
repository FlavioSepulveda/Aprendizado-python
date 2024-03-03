import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class Temperature_convert():
    @staticmethod
    def fahrenheit_to_celcius(f):
        return (f - 32) * 5 / 9


class ConvertFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        self.temp_label = ttk.Label(self, text='Fahrenheit')
        self.temp_label.grid(column=0, row=0, sticky='w', **options)

        self.stringVar = tk.StringVar()
        self.temp_entry = ttk.Entry(self, textvariable=self.stringVar)
        self.temp_entry.grid(column=1, row=0, **options)
        self.temp_entry.focus()

        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, column=1, **options)

        self.grid(padx=10, pady=10, sticky='NSEW')

    def convert(self):
        try:
            f = float(self.temp_entry.get())
            c = Temperature_convert.fahrenheit_to_celcius(f)
            result = f'{f} Farenheit = {c:.2f} Celsius.'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Erro encontrado', message=error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Conversor de temperaturas')
        self.geometry('400x100')
        self.resizable(0, 0)


if __name__ == '__main__':
    app = App()
    ConvertFrame(app)
    app.mainloop()
