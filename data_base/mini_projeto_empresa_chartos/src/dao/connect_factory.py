import pymysql

class ConnectFactory:
    def __init__(self):    
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "root"
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("use empresa_chartos")
        
    def get_connection(self):
        self.cursor = self.connection.cursor()
        return self.cursor