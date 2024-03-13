# MODULO 34 - Python Matplotlib
import matplotlib.pyplot as plt

# print(mp.__version__)

# Plotagem de grafico
# Passmaos cordenadas iniciais no zero e apos ele os pontos onde o grafico sofre deformidades -

# Plot  1 -
xpoints = [0, 6, 8, 10, 13]
ypoints = [0, 15, 10, 12, 13]
plt.subplot(2, 3, 1)  # Linhas, Colunas, Indices
plt.title('Vendas')
plt.plot(xpoints, ypoints, ls='dashed', color='r')
# Montando um segundo plot
# Plot 2 -
xpoints = [0, 6, 8, 10, 13]
ypoints = [3, 14, 0, 8, 13]
plt.subplot(2, 3, 2)
plt.title('Lucro')
plt.plot(xpoints, ypoints, ls='dashed', color='r')
# Plot 3 -
xpoints = [0, 6, 8, 10, 13]
ypoints = [3, 14, 0, 8, 13]
plt.subplot(2, 3, 3)
plt.title('Prejuizos')
plt.plot(xpoints, ypoints, ls='dashed', color='r')
# # Plot 4 -
# xpoints = [0, 6, 8, 10, 13]
# ypoints = [3, 14, 0, 8, 13]
# plt.subplot(2,3,4)
# plt.plot(xpoints, ypoints, ls='dashed', color='r')
# # Plot 5 -
# xpoints = [0, 6, 8, 10, 13]
# ypoints = [3, 14, 0, 8, 13]
# plt.subplot(2,3,5)
# plt.plot(xpoints, ypoints, ls='dashed', color='r')
# # Plot 5 -
# xpoints = [0, 6, 8, 10, 13]
# ypoints = [3, 14, 0, 8, 13]
# plt.subplot(2,3,6)
# plt.plot(xpoints, ypoints, ls='dashed', color='r')

# # Colocamos as listas nas variaveis de pontos no eixo x e y para encontrar um resultado de forma dinamica -
# # plt.plot(xpoints)
# # plt.plot(xpoints, ypoints)
# # plt.plot(xpoints, ypoints, 'o')
# # plt.plot(xpoints, ypoints, marker='|')

# # Parametros
# # marker | line | color
# # plt.plot(xpoints, ypoints,'*:r')
# plt.plot(xpoints, ypoints, marker='*', ms=10, mec='b', mfc='w') # Configurando os graficos


'''
    *Os marcadores podem ser apresentados da sequinte maneira-
    "o" - Circulo
    "*" - Estrela
    "." - Ponto
    "," - Pixel
    "x" - X
    "X" - X (Preenchido)
    "+" - Mais
    "P" - Mais (Preenchido)
    "S" - Quadrado
    "D" - Diamante
    "d" - Diamante (Fino)
    "p" - Pentagono
    "H" - Hexagono
    "h" - Hexagono
    "V" - Triangulo (Para baixo)
    "^" - Triangulo (Para cima)
    "<" - Triangulo (Esquerdo)
    ">" - Triangulo (Direito)
    "1" - Tri Down
    "2" - Tri-Up
    "3" - Tri esquerda
    "4" - Tri Direita
    "|" - Linha vertical
    "_" - Linha horizontal
    
'''
# Plotagem no grafico -

# Estilos de linha -

'''
    * Podemos mudar o estilo das linhas dos nossos graficos utilizando o argumento "Linestyle".
    nome   | Abreviação
    dotted > ':'
    dashed > '--'
    solid > '-'
    dashdot >  '-.'
    none > '' ou ' '
'''
plt.plot(xpoints, ypoints, ls='dashed', color='r')
# Color ou c - Para definir a cor
# linewidth ou lw - Para definir expessura
# linestyle ou ls - Para definir o estilo de linha

font1 = {'family': 'serif', 'color': 'blue',
         'size': 15}  # Configurando a fonte
font2 = {'family': 'serif', 'color': 'blue', 'size': 10}

# Rotulos e titulos do Matplotlib
# plt.title('Modulo pyplot', fontdict=font1, loc='left') # Define o titulo que Identifica o grafico, ele possue 3 valores
plt.suptitle('Minha Loja', fontdict=font1)
# Left, Right e Center
# Define a etiqueta que identifica o eixo x
plt.xlabel('Valor x (Exemplo 1)', fontdict=font2)
# Define a etiqueta que identifica o eixo y
plt.ylabel('Valor y (Exemplo 2)', fontdict=font2)

# Adcionando linhas de grade -

# plt.grid()
# plt.grid(axis='x')
# plt.grid(axis='y', color='r')  # Definindo a linha de destaque 'Axis'

plt.show()
