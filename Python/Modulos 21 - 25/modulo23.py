# MODULO 23 - Manipular arquivo (Criação, Leitura e Escrita)
# 
# open("Nome do Arquivo", "Modo")

# MODOS -
'''
    "r" - Ler - é o valor padrao;
    "a" - Anexar - abre um arquivo para anexar o conteudo, ou o cria se ele não existir;
    "w" - Gravar - abre um arquivo para gravação, cria o arquivo se ele não existir;
    "x" - Cirar - Cria o arquivo especificado, retorna um erro se o arquivo não existir;
'''

# TIPOS -
'''
    Podemos especificar o modo que o arquivo sera tratado da seguinte forma.
    "t" - Texto - valor padrão modo texto;
    "b" - Binário - Modo binario (por exemplo, imagens);
'''

# 
f = open('C:\\Users\\flavi\\OneDrive\\Desktop\\Py\\Aprendizado-python\\Python\\Modulos 21 - 25\\teste.txt', 'r', encoding="UTF-8")
# Para ver o conteudo do arquivo funciona assim
# print(f.read())

# Métodos de leitura

# print(f.readline(2))
for x in f:
    print(x)
    # fechando o arquivo (boas praticas)
f.close()   