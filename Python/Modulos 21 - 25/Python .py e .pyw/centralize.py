# Script para centralizar janelas no tkinter
import tkinter as tk

def centralize(janela, tam_1, tam_2):
    
    # Dando o tamanho maximo da aplicação
    jan = janela
    largura_janela = tam_1
    altura_janela = tam_2
    
    # Telas
    largura_tela = jan.winfo_screenwidth()
    altura_tela = jan.winfo_screenheight()
    
    # Calculando a metade da tela
    centro_x = int(largura_tela/2 - largura_janela/2)
    centro_y = int(altura_tela/2 - altura_janela/2)
    
    # Centralizando:
    jan.geometry(f'{largura_janela}x{altura_janela}+{centro_x}+{centro_y}')
    
