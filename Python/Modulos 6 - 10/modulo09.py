# MODULO 09 - Estrutura de repetição (loops)
# Loop While: o loop while é um loop que roda infinitamente enquanto a condicional para sua execução for verdadeira;

# Prieiro para montar este tipo de loop precisamos de uma variavel de controle que neste caso é 'i'.
i = 0

# A estrutura do loop while se baseaia na palavra reservada 'while';
while i < 8:
    print(i) #  Imprime todos os numeros de 0 a 7, (8 numeros no total).
    i += 1
# Podemos utilizar instruçõies else dentro desses loops.
else:
    print('O valor de i não é mais menor que 8. ')

print('Fim da execução do loop.')

# Criando um loop for:
# O loop for serve para interar nnuma sequencia;

nome = ['Gabriel', 'Danny', 'Arthur']

# Criando o loop for para printar os itens da sequencia for:
for x in nome:
    print(x)

print('Fim da execução.')

# Ele tambem inteira numa cadeia de caracteres:
# Por exemplo -

for x in 'Ola mundo':
    print(x)

# Podemos  usar um else neste estilo de loop taambem:
else:
    print('Fim da execução.')