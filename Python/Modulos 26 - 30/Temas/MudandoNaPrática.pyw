import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Modificando temas')
        self.geometry('300x115')
        self.resizable(0, 0)

        #  UI options -
        paddings = {'padx': 5, 'pady': 5}
        entry_fonts = {'font': ('Helvetica', 11)}

        # Configurar o grid -
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # User name -
        username_label = ttk.Label(self, text='Username: ')
        username_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_fonts)
        username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)

        #  User password -
        userp_label = ttk.Label(self, text='Password: ')
        userp_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        userp_entry = ttk.Entry(
            self, textvariable=password, show='*', **entry_fonts)
        userp_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # Login button -
        login_button = ttk.Button(self, text='Login')
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # Style configure -
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Arial', 14))
        self.style.configure('TButton', font=('Arial', 14))


if __name__ == '__main__':
    app = App()
    app.mainloop()
