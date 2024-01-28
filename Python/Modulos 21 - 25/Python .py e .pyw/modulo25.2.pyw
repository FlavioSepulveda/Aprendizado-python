# Arquivo Terminado em .pyw
'''
    Arquivos terminados em ".pyw" são arquivos cujo NÃO existe uma necessidade do uso do console para executar.
'''
import tkinter as tk

root = tk.Tk()
# Definindo o titulo da aplicação
root.title("App Test 01")
titulo = root.title()
# Dimensionando a janela
# root.geometry("600x400+500+500")
# Centalizando a janela

# Guardando a largura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

largura_janela = 700
altura_janela = 500

# Obtendo as dimensões da tela
# Encontrando o ponto central-
centro_x = int(largura_tela/2 - largura_janela/2)
centro_y = int(altura_tela/2 - altura_janela/2)

# Definindo a posição no centro

root.geometry(f"{largura_janela}x{altura_janela}+{centro_x}+{centro_y}")

# O método resizable() permite ao usuário redimensionar a janela da aplicação.
# Quando o parâmetro é 0 significa que a janela nao pode ser redimensionada.
# Quando o parâmetro é 1 significa que a janela pode ser redimensionada.
# root.resizable(0,0)
# root.resizable(1,1)
root.resizable(True, True)
# Dentro do parâmetro os dois valores booleanos, indicam altura e largura.
# root.resizable(True,True)
# O tamanho da janela por padrão ja vem como 1, com isso podemos por meio dos metodos
#minsize() e maxsize() delimitar um limite.
root.minsize(300,200)
root.maxsize(700,500)
# Assim posso redimensionar do tamanho que eu quiser, mas sem ultrapassar esses limites.

root.mainloop()