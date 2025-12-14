from random import randint
from datetime import datetime
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
            
    def saveReceipt(self):
        ...

    def checkout(self) -> list:
        """
        Docstring for checkout
        
        :param self: instance attribute
        :return: list of all statement in the receipt 
        :return type: list
        """
        # list to strore all Statement.
        msgs = []
        
        # total salary .
        total_salary_of_receive = 0

        # generate random number to serial.
        random_number = randint(0, 100000000)

        # get the date.
        date = datetime.now().strftime("%A, %d-%B-%Y")
        
        # get the time.
        time = datetime.now().strftime("%I:%M:%S %p")

        # add separator. 
        msgs.append(f"-" * 60)

        # append the basic information about the receipt.
        msgs.append(f"Super Market Receipt\nSerial Number: {random_number}\nDate: {date}\nTime: {time}")
        
        # add separator. 
        msgs.append(f"-" * 60)

        # Add the header of the table. 
        msgs.append("{:<5}{:<8}{:<6}{:<10}{:<10}{:<20}".format("Id", "Name", "Price", "Quantity", "Total", "Desc"))


        for id in self.items:
            # get the data from the list:
            name = self.items[id]["obj"].name
            price = self.items[id]["obj"].price
            quantity = self.items[id]["quantity"]
            total_salary = (self.items[id]["quantity"]) * (self.items[id]["obj"].price)
            desc = self.items[id]["obj"].desc

            # sum the total of every item.
            total_salary_of_receive += total_salary
            
            # append every row in the receipt.
            msgs.append(f"{id:<5}{name:<8}{str(price)+"$":<6}{quantity:<10}{total_salary:<10}{desc:<20}")
        
        # add separator.
        msgs.append(f"-" * 60)
        
        # add the final total of receipt.
        msgs.append("{:<29}{}".format("Final Total", total_salary_of_receive))
        
        # return the data.
        return msgs 


LISTOFPRODUCTS = [
    Product(101, "Milk", 300, "1L of milk."),
    Product(102, "Bread", 250, "White bread loaf."),
    Product(103, "Eggs", 450, "12 eggs."),
    Product(104, "Butter", 500, "Butter stick."),
    Product(106, "Soap", 199, "Hand soap.")
]

