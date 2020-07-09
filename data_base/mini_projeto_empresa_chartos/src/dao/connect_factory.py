import pymysql

class ConnectFactory:
    def __init__(self):    
        self.connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "root",
            db = "empresa_chartos"
        )
        self.cursor = self.connection.cursor()
        
    def get_connection(self):
        self.cursor = self.connection.cursor()
        return self.cursor