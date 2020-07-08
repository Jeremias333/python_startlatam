import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

cursor = connection.cursor()
cursor.execute("show databases")

for x in cursor:
    print(x)
