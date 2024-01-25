# MODULO 24 - Banco de dados MySQL

# Crie um servidor apache - XAMPP;
# Criando e manipulando bases de dados MySQL;

# MySQL não é uma base de dados é um servidor de bases de dados.
# Importando o mysql
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste123", 
    password="batata123",
    # Criando um parametro que referencia a data base
    database='my_database'
)

# print(mydb)
# Criando a base de dados em python.
# Precisamos criar um objeto cursor.
m_cursor = mydb.cursor()
# m_cursor.execute('CREATE DATABASE my_database') 
# m_cursor.execute("SHOW DATABASES")

# for x in m_cursor:
#     print(x)
    
# Criando tabelas:
# sql = """CREATE TABLE 
#             pessoas (nome VARCHAR(225), 
#             idade INT(2))"""

# m_cursor.execute(sql)
# Acessando as tabelas de dados:
# m_cursor.execute('SHOW TABLES')
# for x in m_cursor:
#     print(x)

# Alterando as estruturas das tabelas:


# sql = """
#     ALTER TABLE pessoas ADD
#     sobrenome VARCHAR(255)
# Removendo tabelas 
# sql = "ALTER TABLE pessoas DROP sobrenome"
# sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"

# Chave primaria - serve para termo registros de valor unico para cada campo
# sql = """
#     CREATE TABLE pessoas(
#         id INT AUTO_INCREMENT PRIMARY KEY
#         nome VARCHAR(255)
#         idade(2)
#     )
# """
# sql = """
#     ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST
# """

# Para inserir dados dentro da tabela;
# sql = """
#     INSERT INTO pessoas(
#         id, nome, sobrenome, idade
#     )
#     VALUES (
#         NULL, 'Gabriel', 'Araujo', '12'
#     )
# """
# sql = """
#     INSERT INTO pessoas(
#         id, nome, sobrenome, idade
#     )
#     VALUES (
#         NULL, %s, %s, %s
#     )
# """

# val = ("Danny", "Logan", "35")
# val1 = [
#     ("Flavio", "Sepulveda", "21"), 
#     ("Ricardo", "Flavio", "17"), 
#     ("João", "Paulo", "24")
#     ]

# m_cursor.execute(sql, val1)
# m_cursor.executemany(sql, val1)

# mydb.commit()

# print(m_cursor.rowcount, "Registros inseridos")
# #  Obtendo o ide do ultimo item inserido
# print(m_cursor.lastrowid)

# Acessando dados dentro de uma tabela.
# sql = "SELECT * FROM pessoas WHERE sobrenome = 'Logan'"
# sql = "SELECT * FROM pessoas WHERE id = '3'"
# sql = "SELECT * FROM pessoas WHERE idade = '30'"
# sql = "SELECT * FROM pessoas WHERE sobrenome LIKE '%ga%'" # Procura silabas
# Como evitar injeção de SQL
# sql = "SELECT * FROM pessoas WHERE sobrenome = %s"
# sobrenome = ('Logan',)
# m_cursor.execute(sql, sobrenome)
# myresult = m_cursor.fetchall() # Ele retorna todos
# # myresult = m_cursor.fetchone()
# # print(myresult)
# for x in myresult:
#     print(x)

# Ordenando por ordem crescente
# sql = "SELECT * FROM pessoas ORDER BY nome DESC"
# '''
#     Por padrão a ordem vem ASC (ascendente), mas podemos colocar DESC (descendente).
# '''
# m_cursor.execute(sql)
# myresult = m_cursor.fetchall()

# for x in myresult:
#     print(x)

# Apagando registros da tabela
# sql = "DELETE FROM pessoas WHERE idade = %s"
# sql = "DELETE FROM pessoas WHERE sobrenome = %s"
# sobrenome = ('Logan',)
'''
    Usamos o id para não apagar o arquivo errado.
'''

# m_cursor.execute(sql, sobrenome) 
# mydb.commit()
# print(m_cursor.rowcount)

# Excluindo tabela dentro do nosso data base.
# sql = "DROP TABLE pessoas"
# m_cursor.execute(sql)

# Se ele não encontrar tabela com esse nome ele retorna um erro.

# Atualizando registros de tabelas:

# Criando a tabela
# sql1 = """
#     CREATE TABLE pessoas(nome VARCHAR(225),sobrenome VARCHAR(225), idade INT(2))
# """

# m_cursor.execute(sql1)
# sql = """
#     ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST
# """
# m_cursor.execute(sql)

# sql2 = """
#     INSERT INTO pessoas(
#         id, nome, sobrenome, idade
#     )
#     VALUES (
#         NULL, %s, %s, %s
#     )
# """
# valores= [
#     ('Gabriel','Felipe', '12'),
#     ('Antonio', 'Flavio', '21'),
#     ('Ricardo', 'Flavio', '17'),
#     ('Pedro', 'Antonio', '21')
# ]
# m_cursor.executemany(sql2, valores)
# mydb.commit()

# sql = "UPDATE pessoas SET nome = %s WHERE id= %s"
# us = ('Luis', '1')
# m_cursor.execute(sql, us)
# mydb.commit()
# print(m_cursor.rowcount, "Registro(s) afetado(s)")

# Organização de registros:
# sql = "SELECT * FROM pessoas LIMIT 3"
# sql = "SELECT * FROM pessoas LIMIT 3 OFFSET 2"

# m_cursor.execute(sql)
# myResult = m_cursor.fetchall()

# for x in myResult:
#     print(x)

# Criando tabelas de usuarios e livros

# # Criando tabela de usuarios:
# sql_command_1 = """
#     CREATE TABLE User(Id INT AUTO_INCREMENT PRIMARY KEY, Apelido VARCHAR(225),Class VARCHAR(225), Idade INT(2))
# """
# # Criando tabela de livros
# sql_command_2 = """
#     CREATE TABLE Livros(Id INT AUTO_INCREMENT PRIMARY KEY, Titulo VARCHAR(255), Class VARCHAR(255))
# """

# # Dando comando para as duas tabelas serem geradas.
# m_cursor.execute(sql_command_1)

# m_cursor.execute(sql_command_2)

# Colocando usuarios na tabela de usuarios;
# sql_command_insert_1 = """
#     INSERT INTO User(
#         Id, Apelido, Class, Idade
#     )
#     VALUES(
#         NULL, %s, %s, %s
#     )
# """
# valUser = [
#     ('Usuario1', 'Livro1','20'),
#     ('Usuario2', 'Livro3','18'),
#     ('Usuario3', 'Livro2','19'),
#     ('Usuario4', 'Livro4','17'),
#     ('Usuario5', 'Livro5','21')
# ]
# # Adcionando na tabela:
# # colocando itens na tabela de livros:
# sql_command_insert_2 = """
#     INSERT INTO Livros(
#         Id, Titulo, Class
#     )
#     VALUES(
#         NULL, %s, %s
#     )
# """
# valLivros = [
#     ('Livro 1', 'Livre'),
#     ('Livro 2', 'Romance'),
#     ('Livro 3', 'Comedia romantica'),
#     ('Livro 4', 'Comedia'),
#     ('Livro 5', 'Terror')
# ]
# # Colocando na tabela os itens 
# m_cursor.executemany(sql_command_insert_1, valUser)
# m_cursor.executemany(sql_command_insert_2, valLivros)
# mydb.commit()



# Unindo as tabelas 
sql = """
    SELECT
        user.Apelido AS Apelido, livros.Class AS Class
        FROM User 
        INNER JOIN livros ON user.Class = livros.Titulo
"""
m_cursor.execute(sql)
myresult = m_cursor.fetchall()
for x in myresult:
    print(x)
    
print('Terminei.')