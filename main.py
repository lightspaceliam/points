# Main.
import pyodbc
import DerivedEntities.CalcPoint
from Helpers.Query import Query
from Repositories.ProductRepository import ProductRepository
from Repositories.CustomerRepository import CustomerRepository
from Repositories.TransactionRepository import TransactionRepository

def main():

    productRepo = ProductRepository()
    products = productRepo.getData()

    print('There are {0} products.'.format(len(products)))

    customerRepo = CustomerRepository()
    customerCodes = customerRepo.getActiveCustomerCode()

    print('There are {0} active customers.'.format(len(customerCodes)))
    # for customer in customers:
    #     print(customer)

    customerCode = customerCodes[0]

    transactionRepo = TransactionRepository(customerCode)

    transactions = transactionRepo.getTransactions()

    for row in transactions:
        print('CustName: {0}, ProdCode: {1}'.format(row.customerName,row.productCode))
    

    print('Yo Python Promotion Points Reader.')

if __name__ == '__main__':
    main()