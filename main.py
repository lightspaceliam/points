# Main.
import configparser
import pyodbc
import CalcPoint
from Query import Query
from ProductsData import ProductsData
from Repositories.CustomerRepository import CustomerRepository

def main():

    # config = configparser.ConfigParser()
    # config.read('config.ini')

    # print('DB: {0}'.format(config['ProntoCube']['server']))

    print('Name: {0}'.format(__name__))
    productsData = ProductsData()
    products = productsData.getData()

    print('There are {0} products.'.format(len(products)))

    repo = CustomerRepository()
    customerCodes = repo.getActiveCustomerCode()

    print('There are {0} active customers.'.format(len(customerCodes)))
    # for customer in customers:
    #     print(customer)

    # customerCodes = []



    query = Query('DIMA')

    # print(q.customerCode)
    # print(q.addCode())

    print('Yo Python Promotion Points Reader.')

if __name__ == '__main__':
    main()