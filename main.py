# Main.
import pyodbc
import os
import csv
import DerivedEntities.CalcPoint
from Helpers.Query import Query
from Repositories.ProductRepository import ProductRepository
from Repositories.CustomerRepository import CustomerRepository
from Repositories.TransactionRepository import TransactionRepository
from DerivedEntities.CalcPoint import CalcPoint

def main():

    productRepo = ProductRepository()
    products = productRepo.getData()

    print('There are {0} products.'.format(len(products)))

    customerRepo = CustomerRepository()
    customerCodes = customerRepo.getActiveCustomerCode()

    print('There are {0} active customers.'.format(len(customerCodes)))
    # for customer in customers:
    #     print(customer)

    # customerCode = customerCodes[0]

    # transactionRepo = TransactionRepository(customerCode)

    # transactions = transactionRepo.getTransactions()

    cwd = os.getcwd()

    if os.path.exists(cwd + '/points.csv'):
        os.remove(cwd + '/points.csv')

    fieldNames = ['OrderNo', 'CustomerCode', 'CustomerName', 'CustomerType', 'InvoiceDate', 'InvoiceNo', 'TransactionType', 'OrderStatus', 'ProductCode', 'ProductName', 'Uom', 'ItemPricePerUnit', 'ShippedQty', 'ShippedAmount', 'ConversionFactor', 'Point']
    y = 0

    with open(cwd + '/points.csv', 'a', newline = '', encoding = 'utf-8') as csvFile:
        writer = csv.writer(csvFile, 
                        delimiter = ',', 
                        quotechar = '|', 
                        quoting = csv.QUOTE_MINIMAL, 
                        dialect = 'excel')
        
        writer.writerow(fieldNames)

        # Iterate over customers.
        for code in customerCodes:
            transactionRepo = TransactionRepository(code)
            transactions = transactionRepo.getTransactions()
            i = 0
            # Test if list has value.
            if transactions:
                y = y + 1

                for t in transactions:
                    i = i + 1
                    print('No: {0}-{1}-{2} = Cust: {3}'.format(y, i, t.orderNo, t.customerCode))

                    exists = False
                    point = 0

                    for p in products:
                        if p.productCode == t.productCode:
                            exists = True
                            point = p.point

                    if exists == True:    
                        writer.writerow(
                            [t.orderNo,
                            t.customerCode,
                            t.customerName,
                            t.customerType,
                            t.invoiceDate,
                            t.invoiceNo,
                            t.transactionType,
                            t.orderStatus,
                            t.productCode,
                            t.productName,
                            t.uom,
                            t.itemPricePerUnit,
                            t.shippedQty,
                            t.shippedAmount,
                            t.conversion,
                            point]
                            )

    csvFile.close()

    #     for row in transactions:
            
    #         exists = False
    #         point = 0

    #         for p in products:
    #             if p.productCode == row.productCode:
    #                 exists = True
    #                 point = p.point
                    
    #         if exists == True:    
    #             writer.writerow(
    #                 [row.orderNo,
    #                 row.customerCode,
    #                 row.customerName,
    #                 row.customerType,
    #                 row.invoiceDate,
    #                 row.invoiceNo,
    #                 row.transactionType,
    #                 row.orderStatus,
    #                 row.productCode,
    #                 row.productName,
    #                 row.uom,
    #                 row.itemPricePerUnit,
    #                 row.shippedQty,
    #                 row.shippedAmount,
    #                 row.conversion,
    #                 point]
    #                 )

    # csvFile.close()
    # for row in transactions:
    #     print(row)
    #     print('CustName: {0}, ProdCode: {1}, Uom: {2}'.format(row.customerName, row.productCode, row.uom))
    

    print('Operation complete.')

if __name__ == '__main__':
    main()