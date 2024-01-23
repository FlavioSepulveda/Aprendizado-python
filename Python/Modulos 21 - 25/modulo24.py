# MODULO 24 - Banco de dados MySQL

# Crie um servidor apache - XAMPP;
# Criando e manipulando bases de dados MySQL;

# MySQL não é uma base de dados é um servidor de bases de dados.
# Importando o mysql
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="teste123", 
    password="batata123"
)

# print(mydb)
# Criando a base de dados em python.
# Precisamos criar um objeto cursor.
m_cursor = mydb.cursor()
# m_cursor.execute('CREATE DATABASE my_database') 
m_cursor.execute("SHOW DATABASES")

for x in m_cursor:
    print(x)