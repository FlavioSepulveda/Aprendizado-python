# MODULO 21 - Instalador de Pacotes (PIP)
'''
    O pip é um gerenciador de pacotes do python.
    Ele ja vem instalado no python.
    Apertando windows + r digite cmd na barra de pesquisa e no cmd digite pip e de enter.
    Fazendo isso ao estar instalado o cmd retorna a versão do pip.
'''

# pip install [nome do pacote] - No terminal para instalar uma biblioteca.
# pip install pygame - por exemplo instala a a biblioteca pygame.
# python -m pip --upgrade pip (Atualiza o pip do seu computador).
# Exemplo na prática.
import pygame as pg

pygame = dir(pg)
for x in pygame:
    print(x)
    
# Para remover um pacote:
# pip unistall [Nome do pacote a ser desinstalado]
# Confirme com Y e pronto.

# pip list - para mostrar todos os pacotes instalados.