# MODULO 32 - Tkinter_MVC
import tkinter as tk
from tkinter import ttk
import Model, View, Controller


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC')
        # Definindo o model
        model = Model.Model('teste@email.com')
        # defininfo a view
        view = View.View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        # definindo o controller
        controller = Controller.Controller(model, view)
        # definindo o controller
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
