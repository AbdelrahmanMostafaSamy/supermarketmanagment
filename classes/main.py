from random import randint
from datetime import datetime

class Product:
    def __init__(self, prod_id: int, prod_name: str, prod_price: int, prod_desc: str)-> None:
        self.id     = prod_id
        self.name   = prod_name
        self.price  = prod_price
        self.desc   = prod_desc



class Stock:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Self instance attribute
        """
        """
            self.products the products which you have in the store and their quantity 
            
            product: dict {
                id : {
                    "obj"       : Object of the product.
                    "quantity"  : Quantity you have it in th stock. 
                }
            }

        """
        
        # basic stock products .
        self.products: dict = {
            101: {
                "obj" : Product(101, "Milk", 300, "1L of milk."),
                "Quantity" : 25
            },

            102: {
                "obj": Product(102, "Bread", 250, "White bread loaf."),
                "Quantity" : 25
            },

            103: {
                "obj": Product(103, "Eggs", 450, "12 eggs."),
                "Quantity" : 25
            },

            104: {
                "obj": Product(104, "Butter", 500, "Butter stick."),
                "Quantity" : 25
            },

            105: {
                "obj": Product(105, "Soap", 199, "Hand soap."),
                "Quantity" : 25
            }
        }

    def addProductToStock(self, product: Product = None, quantity: int = 0) -> bool:
        """
            Docstring for addProductToStock
            
            :param self: self instance attribute
            :param product: Object from the product class I need to add it into the stock
            :type product: Product
            :param quantity: Quantity I have it in the stock.
            :type quantity: int
            :return: True if the process has finished successfully. 
            :rtype: bool
        """

        # If the object doesn't exists.
        if Product == None:
            return False

        # add the product.
        self.products[product.id] = {
            "obj": product,
            "Quantity" : quantity
        }

        return True

    def deleteFromStock(self, id_of_product : int) -> bool:
        """
        Docstring for deleteFromStock
        
        :param self: self instance attribute.
        :param id_of_product: Id that the product have.
        :type id_of_product: int
        :return: True if the process has finished successfully.
        :rtype: bool
        """

        if id_of_product in self.products.keys():
            self.products.pop(id_of_product)
            return True
        else:
            return False

    def updateProduct(self, id_of_product: int, name: str = "", price: int = 0, desc: str = "") -> bool:
        """
        Docstring for updateProduct
        
        :param self: self instance attribute
        :param name: name you want to update the product.
        :type name: str
        :param price: Price you want to update it.
        :type price: int
        :param desc: Description you want to update it.
        :type desc: str
        :return: True if the process has finished successfully.
        :rtype: bool
        """
        # Check if the id of product , already i have or not.
        if id_of_product in self.products.keys():
            if name != "":
                # update the name of product if the user entered value.
                self.products[id_of_product]["obj"].name = name
            
            if price != 0:
                # update the price of product if the user entered value.
                self.products[id_of_product]["obj"].price = price

            if desc != "":
                # update the desc of product if the user entered value.
                self.products[id_of_product]["obj"].desc = desc
            
            # True if the process has finished successfully.
            return True
        
        else:
            # False if the process has finished with failed.
            return False

    def get_quantity(self, id_of_product: int) -> int:
        """
        Docstring for get_quantity
        
        :param self: Self instance attribute
        :param id_of_product: id of the product which I need to get its quantity in the stock.
        :type id_of_product: int
        :return: the quantity we have it from this product in the stock.
        :rtype: int
        """
        # if I have the product in My stock.
        if id_of_product in self.products.keys():
            # return its quantity.
            return self.products[id_of_product]["Quantity"]
        else:
            # if I don't it return -1.
            return -1
        
    def set_quantity(self, id_of_product: int, new_quantity: int) -> bool:
        """
        Docstring for set_quantity
        
        :param self: Self instance attribute
        :param id_of_product: id of the product which I need to get its quantity in the stock.
        :type id_of_product: int
        :param new_quantity: The new quantity I need to set it.
        :type new_quantity: int
        :return: True if the process has finished successfully.
        :rtype: bool
        """
        # if I have the product in My stock.
        if id_of_product in self.products.keys():
            # set new quantity quantity.
            self.products[id_of_product]["Quantity"] = new_quantity
            return True
        else:
            # if I don't have it return false.
            return False
        
class Cart:
    def __init__(self):
    #     id : {
    #         obj        : object,
    #         quantity   : int
    #         item_total  : int
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
            self.items[prod.id] = {'obj': prod, "quantity": quantity, "item_total": 0}

        self.update_total()

    def removeProduct(self, prod: Product, quantity: int = 1):

        if prod.id in self.items.keys():
            # decrease by the requested quantity
            self.items[prod.id]['quantity'] -= quantity

            if self.items[prod.id]['quantity'] <= 0:
                self.items.pop(prod.id)

        self.update_total()

    def update_total(self):
        cart_total = 0

        for iid, idata in self.items.items():
            item_total = idata['obj'].price * idata['quantity']

<<<<<<< HEAD
            idata["itemtotal"] = itemtotal
            carttotal += itemtotal

        # store the computed total on the cart
        self.total = carttotal
        return self.total
=======
            idata["item_total"] = item_total
            cart_total += item_total
>>>>>>> 1513dea5a464dfa52c0a85647bb7a643f6235a74
    
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


# LISTOFPRODUCTS = [
#     Product(101, "Milk", 300, "1L of milk."),
#     Product(102, "Bread", 250, "White bread loaf."),
#     Product(103, "Eggs", 450, "12 eggs."),
#     Product(104, "Butter", 500, "Butter stick."),
#     Product(106, "Soap", 199, "Hand soap.")
# ]


# my_cart = Cart()
# my_cart.addProduct(LISTOFPRODUCTS[0], 100)
# my_cart.addProduct(LISTOFPRODUCTS[2], 150)
# my_cart.addProduct(LISTOFPRODUCTS[3], 300)
# my_cart.addProduct(LISTOFPRODUCTS[1], 200)

# my_cart.saveReceipt()

# my_stock = Stock()
# my_stock.addProductToStock(Product(106, "Soap", 199, "Hand soap."), 30)
# my_stock.deleteFromStock(1000)
# my_stock.updateProduct(103, "Chipes", 350, "Lol")

# print(my_stock.set_quantity(106, 150))
# print(my_stock.get_quantity(106))


# for key, value in my_stock.products.items():
#     print(f"{key} : ==>", end="")
#     for key_, value_ in value.items():
#         print(f"{key_}: {value_.name} <--> {value_.price}  <--> {value_.desc}")
#         break


