import pyodbc
from .RepositoryBase import RepositoryBase

class CustomerRepository(RepositoryBase):

    activeCustomersQueryString: str = """
        SELECT	T.CustomerCode
        FROM	(
                SELECT	CONVERT(NVARCHAR(50), LTRIM(RTRIM(C.bi_dd_accountcode))) COLLATE SQL_Latin1_General_CP1_CI_AS AS 'CustomerCode'
                FROM	bi_deb_dim_v AS C
                WHERE	C.bi_dd_deb_status IS NOT NULL
                        AND LTRIM(RTRIM(C.bi_dd_deb_status)) = ''
                ) AS T
        ORDER BY T.CustomerCode ASC;
        """
    
    # returns a string list of customer codes.
    @classmethod
    def getActiveCustomerCode(self):
        cursor = self.getCursor(self)

        try:
            cursor.execute(self.activeCustomersQueryString)

            codes = []

            for row in cursor:
                codes.append(row.CustomerCode)

            return codes

        except pyodbc.Error as ex:
            print(ex)
        finally:
            cursor.close()
            #self.connection.close()
