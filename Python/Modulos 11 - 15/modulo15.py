# # MODULOS 15 - Escopo de Variáveis

# # Tipos de variaveis - Local e Global

# # A variavel so existe dentro do local onde ela é criada
# # Dentro de uma função  a variavel so ira existir dentro da função;

# def myFunc():
#     x = 300
#     print(x)

# # x  - quando referenciada dentro de uma função a variavel passa a não existir fora dela causando um erro sempre que for chamada fora da função.
    
# myFunc() # Vai printar o valor de x dentro da variavel.

# def myFunc1():
#     x = 300
#     def myInnerFunc():
#         print(x)
#     myInnerFunc()

# '''
#     Dentro da função as variaveis podem ser referenciadas dentro de qualquer função a baixo dela, mas fora dela não podem.
# '''
# myFunc1()

# # Variaveis de escopo global.
# x = 300
# # Dentro da função, posso refeciar qualquer variavel que exista a cima dela.
# def my300():
#     # print(x)

# # my300() # Ira imprimir 300
# # print(x) # Ira imprimir o valor de x.

# # Tornando a variavel global
# # def my200():
# #     x = 200
# #     print(x)

# # my200()

# Quando a variavel é definida como global, podemos chamr-la de qualque lugar.
def myFunc():
    global x
    x = 200
    print(x)


myFunc()
print(x)