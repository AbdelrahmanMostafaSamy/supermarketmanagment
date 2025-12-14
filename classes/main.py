class Product:
    def __init__(self, prod_id: int, prod_name: str, prod_price: int, prod_desc: str)-> None:
        self.id = prod_id
        self.name = prod_name
        self.price = prod_price
        self.desc = prod_desc


class Cart:
    def __init__(self):
    #     id : {
    #         obj        : object,
    #         quantity   : int
    #         itemtotal  : int
    #     }
        self.items = {}
        self.total = 0

    def getCart(self):
        return self.items, self.total

    def addProduct(self, prod: Product, quantity: int = 1):
        if prod.id in self.items.keys():
            self.items[prod.id]['quantity'] += 1

        else:
            self.items[prod.id] = {'obj': prod, "quantity": quantity, "itemtotal": 0}

        self.update_total()

    def removeProduct(self, prod: Product, quantity: int = 1):

        if prod.id in self.items.keys():
            self.items[prod.id]['quantity'] -= 1

            if self.items[prod.id]['quantity'] <= 0:
                self.items.pop(prod.id)

        self.update_total()

    def update_total(self):
        carttotal = 0

        for iid, idata in self.items.items():
            itemtotal = idata['obj'].price * idata['quantity']

            idata["itemtotal"] = itemtotal
            carttotal += itemtotal
            

    def checkout(self):
        #return reciept info
        #create reciept
        ...

LISTOFPRODUCTS = [
    Product(101, "Milk", 300, "1L of milk."),
    Product(102, "Bread", 250, "White bread loaf."),
    Product(103, "Eggs", 450, "12 eggs."),
    Product(104, "Butter", 500, "Butter stick."),
    Product(106, "Soap", 199, "Hand soap.")
]