import pyodbc
import configparser

class RepositoryBase:

    # read must be configured with utf-8 encoding.
    _config = configparser.ConfigParser()
    _config.read('config.ini', encoding='utf-8')
    
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+_config.get('ProntoCube','server') +
        ';DATABASE='+_config.get('ProntoCube','database')+';UID='+_config.get('ProntoCube','username')+';PWD=' + _config.get('ProntoCube','password')
    )

    def getCursor(self):
     
        return self.connection.cursor()