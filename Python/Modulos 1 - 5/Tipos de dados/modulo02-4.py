# OS CARACTERES DE ESCAPE

# Os caracteres de escape sevem para representar caracteres que normalmente não podem ser inseridos numa string de maneira convencional.

txt = "Somos chamados \"Vikings\" do norte."
# A barra invertida insere no codigo os caracteres de escape, no exemplo a cima ela inseriu na string as aspas duplas.
print(txt)

txt = "Ola\nmundo" # Quebra de linha
print(txt)
txt = "Ola\rmundo" # Retorno
print(txt)
txt = "Ola\tmundo" # Representa uma tabulação a tecla 'Tab'
print(txt)

txt = "Isso irá inserir um \\ (Uma barra invertida)"
print(txt)
txt = "It\'s alright." # Adciona aspas simples
print(txt)
txt = "Ola \bmundo!"   # Apaga o caractere anterior (Backspace)
print(txt)
txt = "\x48\x65\x6c\x6c\x6f" # Quando seguida por um x a barra invertida representa um numero hexadecimal
print(txt)
txt = "\110\145\154\154\157" # Quando seguida por 3 inteiros representa um valor em octal
print(txt)