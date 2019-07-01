import pyodbc
import configparser

class RepositoryBase:

    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # print('Base Repo: ' + config['ProntoCube']['server'])
    
    server: str = ''
    database: str = ''
    username: str = ''
    password: str = ''

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server +
        ';DATABASE='+database+';UID='+username+';PWD=' + password
    )
    connection.setencoding(encoding='utf-8')

    def getCursor(self):

        return self.connection.cursor()