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
        self.geometry('525x65')
        self.resizable(0, 0)
        
        self.create_header_frame()
        
    def create_header_frame(self):
        self.header = ttk.Frame(self)
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=10)
        self.header.columnconfigure(2, weight=1)
        
        # Label -
        self.label = ttk.Label(self.header, text='URL')
        self.label.grid(column=0, row=0, sticky=tk.W)
        
        # Entry -
        self.entry = tk.StringVar()
        self.url_entry = ttk.Entry(
            self.header,
            textvariable=self.entry,
            width=80
        )
        self.url_entry.grid(column=1, row=0, sticky=tk.EW)
        
        # Button -
        self.download_button = ttk.Button(self.header, text='Download')
        self.download_button.grid(column=1, row=0, sticky=tk.E)
        
        self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        
        
if __name__=='__main__':
    app = App()

    app.mainloop()