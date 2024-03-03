# Exemplos do uso do widget progressbar - Determinada
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Barra do tipo Determinada')
root.resizable(0, 0)
root.geometry('500x400')
root.grid()
# Criando progresso visivel da barra.


def update_progress_label():
    return f"Progresso atual: {pb['value']}%"


def progress():
    # Verificando se o valor do progresso é menor que 100...
    if pb['value'] < 100:
        # Se for menor que 100, aumento em 20...
        pb['value'] += 20
        # Sempre que eu aumentar em 20, irei atualizar a barra de progresso...
        value_label['text'] = update_progress_label()
    else:
        # Caso o contrario, exibo uma mensagem indicando a conclusão do processo.
        showinfo(message='Processo concluido!')


def stop():
    # Ao apertar o botão ele para a barra de progresso.
    pb.stop()
    # Ela ira zerar o valor da barra de progresso.
    value_label['text'] = update_progress_label()

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
pb.grid(column=0, row=1, columnspan=2, padx=10, pady=20)

value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=0, columnspan=2)

start_button = ttk.Button(
    root,
    text='Start',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

root.mainloop()
