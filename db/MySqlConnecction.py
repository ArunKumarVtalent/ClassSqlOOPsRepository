import mysql.connector as mysqlConn

class MySqlConnection:
    def __init__(self):
        self.get_connection = mysqlConn.connect(
            host='localhost',
            user='root',
            password='password',
            database='companydb'
        )

    def get_connection(self):
        return self.get_connection