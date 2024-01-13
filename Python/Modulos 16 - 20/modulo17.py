# MODULO 17 - Datas em Python
import datetime 
# Criação de objeto de data
x = datetime.datetime(2020, 5, 17, 12, 30, 10)
y = datetime.datetime.now()
# Descobrindo a diferença entre datas:
z = y - x
v = x - y 

print(x)
print(z)
print(v)

# Esse modulo não aceita adição de tempo mas podemos fazer com datas negativas.
# O resultado é negativo mas podemos colocar com .now()

# Metododo strdatetime()
# ele tem um formato pra receber o retorno.

x1 = datetime.datetime(2001, 10, 17)

# Formatando a data:
y1=x1.strftime('%A %d %B %Y')

print(y1)