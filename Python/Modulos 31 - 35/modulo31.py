# MODULO 31 - Programação Assíncrona Tkinter
#
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from threading import Thread
import requests as rq


class AsyncDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.html = None
        self.url = url

    def run(self):
        response = rq.get(self.url)
        self.html = response.text


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Webpage Download')
        self.geometry('680x430')
        self.resizable(0, 0)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()

    def create_header_frame(self):
        self.header = ttk.Frame(self)
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)

        # Label -
        self.label = ttk.Label(self.header, text='URL: ')
        self.label.grid(column=0, row=0, sticky=tk.W)

        # Entry -
        self.url_var = tk.StringVar()
        self.entry = tk.StringVar()
        self.url_entry = ttk.Entry(
            self.header,
            textvariable=self.url_var,
            width=80
        )
        self.url_entry.grid(column=1, row=0, sticky=tk.EW)

        # Button -
        self.download_button = ttk.Button(self.header, text='Download')
        self.download_button['command'] = self.handle_download
        self.download_button.grid(column=1, row=0, sticky=tk.E)

        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

    def create_body_frame(self):
        self.body = ttk.Frame(self)
        self.html = tk.Text(self.body, height=20)
        self.html.grid(column=0, row=1)
        
        scrollbar = ttk.Scrollbar(
            self.body,
            orient='vertical',
            command=self.html.yview
        )
        scrollbar.grid(column=1, row=1, sticky=tk.NS)
        self.html['yscrollcommand'] = scrollbar.set
        
        self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)
    
    def create_footer_frame(self):
        self.footer = ttk.Frame(self)
        self.footer.columnconfigure(0, weight=1)
        # Exit button -
        self.exit_button = ttk.Button(
            self.footer,
            text='Exit',
            command=self.destroy
        )
        self.exit_button.grid(column=0, row=0, sticky=tk.E)
        
        self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)
        
    def handle_download(self):
        url = self.url_var.get()
        
        if url:
            # Desativando o botão de download -
            self.download_button['state'] = tk.DISABLED
            self.html.delete(1.0, 'end')
            
            download_thread = AsyncDownload(url)
            download_thread.start()
            
            # Monitorando a thread criada -
            self.monitor(download_thread)
        
        else:
           showerror(title='Erro', message='Please, insert the webpage URL')
           
    def monitor(self, thread):
        if thread.is_alive():
            # Verificando a thread a cada 100 milessegundos -
            self.after(100, lambda: self.monitor(thread))
            
        else:
            # Reativando o botão de download -
            self.html.insert(1.0, thread.html)
            self.download_button['state'] = tk.NORMAL
            
    
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
