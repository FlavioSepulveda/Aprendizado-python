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

# Função range -ela delimita o inicio e o fim ded uma execução em um determinado raio.
    
for x in range(1, 6, 2): # Definindo o primeiro parametro de inicio fornecendo um numero e uma virgula.
    # Impllemaentar um 3°  valo ele determina ded quanto em qquantoe ele ira iniciar.
    print(x)  # A função range não precisaa de uma coleção para funcionar


print('Fim da excução')
# Func  range(Numero do inicio, Numero do fim, Numero do incremento).

# Instrução break - serve pra interromper um fluxo ainda que a condição de um loop seja verdadeira.

i = 1
while 1 < 6:
    print(i)
    if (i == 3):
        print('Fim da execução com o comando "break".')
        break
    i += 1

#  O break tambem pode ser utilizado dentro da função for tambem;
for x in nome:
    #print(x)
    if x == 'Danny':
        break # Parando a execução no "Danny".
    print(x)  # Com o print aqui, ele vai pegar apenas o primeiro nome pois o segundo ja quebra a execução.

    

