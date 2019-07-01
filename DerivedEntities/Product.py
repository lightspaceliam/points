class Product:
    
    productCode: str = ''
    point: float = 0.0

    def __init__(self, code, point):
        self.productCode = code
        self.point = point