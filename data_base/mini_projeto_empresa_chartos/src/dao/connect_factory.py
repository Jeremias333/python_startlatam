import mysql.connector

class ConnectFactory:
    def __init__(self):    
        self.connection = mysql.connector.connect(    
            host = "localhost",
            user = "root",
            password = "root",
            database = "empresa_chartos"
        )
        
    def get_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def get_connection(self):
        return self.connection 