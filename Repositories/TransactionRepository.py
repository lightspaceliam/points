import pyodbc
from .RepositoryBase import RepositoryBase
from Helpers.Query import Query
from DerivedEntities.CalcPoint import CalcPoint

class TransactionRepository(RepositoryBase):

    code: str = ''

    def __init__(self, customerCode):
        self.code = customerCode
    
    
    def getTransactions(self):
        cursor = self.getCursor()
        print(self.code)
        query = Query(self.code)
        queryString = query.addCode()
        try:
            cursor.execute(queryString)

            transactions = []

            for row in cursor:
                
                calcPoint = CalcPoint(
                    row.OrderNo,
                    row.CustomerCode,
                    row.CustomerName,
                    row.CustomerType,
                    row.InvoiceDate,
                    row.InvoiceNo,
                    row.TransactionType,
                    row.OrderStatus,
                    row.ProductCode,
                    row.ProductName,
                    row.Uom,
                    row.ItemPricePerUnit,
                    row.ShippedQty,
                    row.ShippedAmount,
                    row.ConversionFactor,
                    0
                )
                transactions.append(calcPoint)
                
                return transactions

        except pyodbc.Error as ex:
            print(ex)
        finally:
            cursor.close()
            #self.connection.close()

