import platform
# Esse comando retorna o sistema operacional 
x = platform.system()

print(x)

# Função que chama todos os comandos;
x = dir(platform)
for i in x:
    print(i)