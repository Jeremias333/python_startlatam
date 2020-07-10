import mysql.connector

class ConnectFactory:
    def __init__(self):    
        self.connection = mysql.connector.connect(    
            host = "sql10.freemysqlhosting.net",
            user = "sql10353994",
            password = "vkKAleExQA",
            database = "sql10353994"
        )
        
    def get_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def get_connection(self):
        return self.connection 