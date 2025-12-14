class Product:
    def __init__(self, prod_id: int, prod_name: str, prod_price: int, prod_desc: str)-> None:
        self.id = prod_id
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.prod_desc = prod_desc

# """
#     id : {
#         obj : object,
#         Qu:
#     }

# """

class Cart:
    def __init__(self):
        self.items = {}

    def getCart(self):
        ...

    def addProduct(self, prod: Product, quantity: int = 1):
        ...

    def removeProduct(self, prod: Product, quantity: int = 1):
        ...

    def checkout(self):
        #return reciept info
        #create reciept
        ...

LISTOFPRODUCTS = [
    Product
]