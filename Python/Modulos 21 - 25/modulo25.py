# MODULO 25 - Aplicações de Ambiente grafico(GUI) Tkinter Fundamentos
# Importando o Tkinter
import tkinter as tk

# tk._test()
# Criando uma instancia da classe que representa a janela principal
# Root - representa o principio a rais
root = tk.Tk() # Inicia a tela

# Classe label
lbl = tk.Label(root, text="Ola mundo!") 
# Métodos de posicionamento
lbl.pack()

# Chamando o main loop
root.mainloop() # Mantem a tela do aplicativo aberta
# Pequena mudança: 
# Apartir daqui todos os arquivos python serãoo feitos em terminação .pyw, criando o habito de criar aplicações.