

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
        print("{:<5}{:<8}{:<6}{:<10}{:<10}{:<20}".format("Id", "Name", "Price", "Quantity", "Total", "Desc"))
        self.checkout_receipt = {}

        for id in self.items:
            name = self.items[id]["obj"].prod_name
            price = self.items[id]["obj"].prod_price
            quantity = self.items[id]["quantity"]
            total_salary = self.items[id]["quantity"] * self.items[id]["obj"].prod_price
            desc = self.items[id]["obj"].prod_desc

            self.checkout_receipt[id] = {
                "name" : name,
                "price" : price,
                "Quantity": quantity,
                "Total" : total_salary,
                "desc": desc
            }

            msg = f"""{id:<5}{name:<8}{str(price)+"$":<6}{quantity:<10}{total_salary:<10}{desc:<20}"""
            print(msg)
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

my_cart = Cart()
my_cart.addProduct(LISTOFPRODUCTS[0], 50)
my_cart.addProduct(LISTOFPRODUCTS[1], 20)
my_cart.addProduct(LISTOFPRODUCTS[2], 30)
my_cart.checkout()



