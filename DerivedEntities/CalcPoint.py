class CalcPoint:

    orderNo: int = 0
    customerCode: str = ''
    customerName: str = ''
    customerType: str = ''
    invoiceDate: str = ''
    invoiceNo: str = ''
    transactionType: str = ''
    orderStatus: str = ''
    productCode: str = ''
    productName: str = ''
    uom: str = ''
    itemPricePerUnit: float = 0.0
    shippedQty: float = 0.0
    shippedAmount: float = 0.0
    conversion: float = 0.0
    point: float = 0.0

    # Constructor.
    def __init__(self,orderNo,customerCode,customerName,customerType,invoiceDate,invoiceNo,transactionType,orderStatus,productCode,productName,uom,itemPricePerUnit,shippedQty,shippedAmount,conversion,point):
        self.orderNo = orderNo
        self.customerCode = customerCode
        self.customerName = customerName
        self.customerType = customerType
        self.invoiceDate = invoiceDate
        self.invoiceNo = invoiceNo
        self.transactionType = transactionType
        self.orderStatus = orderStatus
        self.productCode = productCode
        self.productName = productName
        self.uom = uom
        self.itemPricePerUnit = itemPricePerUnit
        self.shippedQty = shippedQty
        self.shippedAmount = shippedAmount
        self.conversion = conversion
        self.point = point