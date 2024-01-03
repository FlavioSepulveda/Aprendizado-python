# FORMATOS DE STRINGS
# nÃO É POSSIVEL JUNTAR NUMEROS E STRINGS, A MENOS QUE SE USE O METODO FORMAT

'''
    O método format acessa a string e substitui o "{}" pelo valor a ser formatado.
'''
idade = 21
txt = 'Meu nome é Antonio e tenho {} anos de idade'

print(txt.format(idade))

# O método format insere valores na string de maneira ordenada desta forma:
quantidade = 3
comida = "Bolo"
preco = 14.50

txt2 = "Eu quero {} de {} por {} reais"
# A apresentação dos itens formatados pode ser configurada com a adição de indices a eles;
txt3 = "Quero pagar {2} por {0} pedaços de {1}."
print(txt2.format(quantidade, comida, preco))
print(txt3.format(quantidade, comida, preco))
