# MODULO 16 - Modulos Python
'''
    Para criar um módulo, precisamos criar um arquivo com a terminação .py, pois ele sera nosso módulo a ser importado, por meio da palavra reservada import.
    OBS.: O módulo precisa estar dentro da mesma pasta que o main.py.
'''
# import meuModulo
import meuModulo as MM

# Para acessar uma função dentro de um módulo fazemos da seguinte forma
# NomeDoModulo.função()

# meuModulo.bemVindo('Flavio')

# a = meuModulo.pessoa['Idade']
# print(a)
# print(meuModulo.pessoa)
# podemos criar apelidos ao modulo para chamar-lo com o atributo as.
MM.bemVindo('Flavio')
# MM é o apelido do meu modulo

