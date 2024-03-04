import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class TemperatureConverter:
    @staticmethod
    def fareheint_to_celsius(f, format=True):
        result = (f - 32) * 5 / 9
        if format:
            return f'{f} Farenheit = {result:.2f} Celsius.'

    @staticmethod
    def celsius_to_farenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Farenheit.'
        return result


class ConverterFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        options = {'padx': 5, 'pady': 5}

        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w', **options)

        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
        self.temperature_entry.focus()

        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button.grid(column=2, row=2, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        self.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')

    def convert(self, event=None):
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, 'end')
        self.result_label.text = ''


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # Radio Buttons -
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='F to C',
            value=0,
            variable=self.selected_value,
            command=self.change_frame
        ).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='C to F',
            value=1,
            variable=self.selected_value,
            command=self.change_frame
        ).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')
        
        # Iniciando frames -
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            'Farenheit',
            TemperatureConverter.fareheint_to_celsius
        )
        self.frames[1] = ConverterFrame(
            container,
            'Celsius',
            TemperatureConverter.celsius_to_farenheit
        )

        self.change_frame()
    
    def change_frame(self):
        # Ele acessa o 'Selected value' que tem o valor de 1 ou 0, que esta armazenado nela pelo metodo get.
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        # Aqui ele determina qual o proximo frame.
        frame.tkraise()
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Conversor de temperaturas')
        self.geometry('300x200')
        self.resizable(0, 0)


if __name__ == '__main__':
    app = App()
    ControlFrame(app)
    app.mainloop()
