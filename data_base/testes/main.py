import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "empresa_chartos"
)

name = "Jeremias"
function = "Segurança"
salary = 1999.00

sql = "insert into funcionarios (nome, funcao, salario) values (%s, %s, %s)"

cursor = connection.cursor()
val = (name, function, salary)
cursor.execute(sql, val)

connection.commit()

print(cursor.rowcount)


