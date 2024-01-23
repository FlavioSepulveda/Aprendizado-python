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
sql = """
    ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST
"""

m_cursor.execute(sql)