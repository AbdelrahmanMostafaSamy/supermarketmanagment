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
            # increase by the requested quantity (not just 1)
            self.items[prod.id]['quantity'] += quantity

        else:
            self.items[prod.id] = {'obj': prod, "quantity": quantity, "itemtotal": 0}

        self.update_total()

    def removeProduct(self, prod: Product, quantity: int = 1):

        if prod.id in self.items.keys():
            # decrease by the requested quantity
            self.items[prod.id]['quantity'] -= quantity

            if self.items[prod.id]['quantity'] <= 0:
                self.items.pop(prod.id)

        self.update_total()

    def update_total(self):
        carttotal = 0

        for iid, idata in self.items.items():
            itemtotal = idata['obj'].price * idata['quantity']

            idata["itemtotal"] = itemtotal
            carttotal += itemtotal

        # store the computed total on the cart
        self.total = carttotal
        return self.total
    
    def __is_Serial_available(self) -> bool:
        
        """
        
            Search in the json file that have all serial numbers
            if the serial is --> found in json file return --> False
            if not found return --> True 

        """
        # self.serial_number

        return True
        ...


    def saveReceipt(self) -> None:
        """
            Docstring for saveReceipt.

            :param self: instance attribute
            :return: No return.

            This function is created to save the receipt.
        """
        # get the data from the checkout.
        data = self.checkout()

        # get date with another format
        date = datetime.now().strftime("%d %b %Y")
        
        # create a txt file that have a receipt.
        with open(f"receipts/receipt_{self.serial_number}_{date}_.txt", 'w') as receipt:
            
            # Put the data into the file.
            for line in data:
                receipt.write(line + "\n")

            # close the file.
            receipt.close()


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
        self.serial_number = randint(10000000, 99999999) 

        # still generate numbers until find a new serial number.
        while not self.__is_Serial_available():
            self.serial_number = randint(10000000, 99999999)

        # get the date.
        date = datetime.now().strftime("%A, %d-%B-%Y")
        
        # get the time.
        time = datetime.now().strftime("%I:%M:%S %p")

        # add separator. 
        msgs.append(f"-" * 60)

        # append the basic information about the receipt.
        msgs.append(f"Super Market Receipt\nSerial Number: {self.serial_number}\nDate: {date}\nTime: {time}")
        
        # add separator. 
        msgs.append(f"-" * 60)

        # Add the header of the table. 
        msgs.append("{:<8}{:<6}{:<10}{:<10}{:<20}".format("Name", "Price", "Quantity", "Total", "Desc"))


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
            msgs.append(f"{name:<8}{str(price)+"$":<6}{quantity:<10}{total_salary:<10}{desc:<20}")
        
        # add separator.
        msgs.append(f"-" * 60)
        
        # add the final total of receipt.
        msgs.append("{:<24}{}".format("Final Total", total_salary_of_receive))
        
        # return the data.
        return msgs 


LISTOFPRODUCTS = [
    Product(101, "Milk", 300, "1L of milk."),
    Product(102, "Bread", 250, "White bread loaf."),
    Product(103, "Eggs", 450, "12 eggs."),
    Product(104, "Butter", 500, "Butter stick."),
    Product(106, "Soap", 199, "Hand soap.")
]


# my_cart = Cart()
# my_cart.addProduct(LISTOFPRODUCTS[0], 100)
# my_cart.addProduct(LISTOFPRODUCTS[2], 150)
# my_cart.addProduct(LISTOFPRODUCTS[3], 300)
# my_cart.addProduct(LISTOFPRODUCTS[1], 200)

# my_cart.saveReceipt()

