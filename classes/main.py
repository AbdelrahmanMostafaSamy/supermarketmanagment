from random import randint
from datetime import datetime
import json
import os

#os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Product:
    def __init__(self, prod_id: int, prod_name: str, prod_price: int, prod_desc: str)-> None:
        self.id     = prod_id
        self.name   = prod_name
        self.price  = prod_price
        self.desc   = prod_desc

    def getJson(self):
        return {'id': self.id, 'name': self.name, "price": self.price, "desc": self.desc}
    
    def loadJson(self, data):
        return Product(data.get('id'), data.get('name'), data.get('price'), data.get('desc'))
    

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
        # the products from the stock.
        self.products: dict = self.loadDataFromJSONFile()

        # # basic stock products .
        # self.products: dict = {
        #     101: {
        #         "obj" : Product(101, "Milk", 300, "1L of milk."),
        #         "Quantity" : 25
        #     },

        #     102: {
        #         "obj": Product(102, "Bread", 250, "White bread loaf."),
        #         "Quantity" : 25
        #     },

        #     103: {
        #         "obj": Product(103, "Eggs", 450, "12 eggs."),
        #         "Quantity" : 25
        #     },

        #     104: {
        #         "obj": Product(104, "Butter", 500, "Butter stick."),
        #         "Quantity" : 25
        #     },

        #     105: {
        #         "obj": Product(105, "Soap", 199, "Hand soap."),
        #         "Quantity" : 25
        #     }
        # }

    def addProductToStock(self, product: Product, quantity: int = 0):
        """
            Docstring for addProductToStock
            
            :param self: self instance attribute
            :param product: Object from the product class I need to add it into the stock
            :type product: Product
            :param quantity: Quantity I have it in the stock.
            :type quantity: int
        """

        # read the data.
        json_data = self.readJSONData()

        # Append new Item to the last data.
        json_data['stock'][str(product.id)] = {
                "obj": product.getJson(),
                "Quantity" : quantity
            }

        # write the data.
        self.writeJSONData(json_data)
    
    def loadDataFromJSONFile(self) -> dict:
        """
        Docstring for loadDataFromJSONFile
        
        :param self: Description
        :return: Dictionary with all data
        :rtype: dict
        """
        
        # A dict to add the products from the stock.
        products = {}

        # get the stock.
        products_in_json_data = self.readJSONData()['stock']

        # iterate on the stock dict to store it in the products dict.
        for key, value in products_in_json_data.items():
            products[int(key)] = {
                "obj" : Product(value.get('id'), value.get('name'), value.get('price'), value.get('desc')),
                "Quantity" : products_in_json_data[key]["Quantity"]
            }

        # return the products you have in the stock.
        return products



    def readJSONData(self) -> dict:
        """
        Docstring for readJSONData
        
        :param self: self instance attribute
        :return: Dictionary with all data in the json file.
        :rtype: dict
        """
        # Read the data from the json file.
        with open("classes/data.json", 'r') as json_file:
            json_data = json.load(json_file)

        # return the data.
        return json_data    

    def writeJSONData(self, json_data: dict) -> None:
        """
        Docstring for writeJSONData
        
        :param self: self instance attribute
        """

        # save the new item into the json file .
        with open("classes/data.json", "w") as json_file:
            json.dump(json_data, json_file, default=str)


    def getQuantity(self, id_of_product: int) -> int:
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
        
    def setQuantity(self, id_of_product: int, new_quantity: int) -> bool:
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
        self.stockobj = Stock()

    def getCart(self):
        return self.items, self.total

    def addProduct(self, prod: Product, quantity: int = 1):
        if prod.id in self.items.keys():
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

            self.items[iid]['item_total'] = item_total
            cart_total += item_total

        self.total = cart_total
        return self.total
    
    def __is_Serial_available(self, serial_number) -> bool:
        """
            Search in the json file that have all serial numbers
            if the serial is --> found in json file return --> False
            if not found return --> True 

        """
        # with open("classes/data.json", "r") as fp:
        #     jdata = json.load(fp)

        json_data = self.stockobj.readJSONData()

        return serial_number not in json_data["history"].keys()

    def saveReceipt(self, serial_number, msgs) -> None:
        """
            Docstring for saveReceipt.

            :param self: instance attribute
            :return: No return.

            This function is created to save the receipt.
        """

        print("I here")
        date = datetime.now().strftime("%d %b %Y")
        
        # create a txt file that have a receipt.
        with open(f"receipts/receipt_{serial_number}_{date}_.txt", 'w') as receipt:

            for line in msgs:
                receipt.write(line + "\n")

        # save history to json
        with open("classes/data.json", "r+") as fp:
            jdata = json.load(fp)

        historyitems = []
        for i in self.items.values():
            prod = i['obj'].getJson()
            prod.update({'quantity': i['quantity'], 'item_total': i['item_total']})

            historyitems.append(prod)

        jdata['history'][serial_number] = historyitems

        with open("classes/data.json", "w") as fp:
            json.dump(jdata, fp)

            

    def checkout(self) -> list:
        """
            Docstring for checkout
            
            :param self: instance attribute
            :return: True for success, False for quantity error 
            list of all statement in the receipt 
            :return type: bool, list
        """
        # list to strore all Statement.
        msgs = []

        # generate random number to serial.
        serial_number = randint(10000000, 99999999) 

        # still generate numbers until find a new serial number.
        while self.__is_Serial_available(serial_number) == False:
            serial_number = randint(10000000, 99999999)


        date = datetime.now().strftime("%A, %d-%B-%Y")
        time = datetime.now().strftime("%I:%M:%S %p")

        # add separator. 
        msgs.append(f"-" * 60)

        # append the basic information about the receipt.
        msgs.append(f"Super Market Receipt\nSerial Number: {serial_number}\nDate: {date}\nTime: {time}")
        
        # add separator. 
        msgs.append(f"-" * 60)

        # Add the header of the table. 
        msgs.append("{:<8}{:<6}{:<10}{:<10}{:<20}".format("Name", "Price", "Quantity", "Total", "Desc"))


        for id in self.items:
            # get the data from the list:
            name = self.items[id]["obj"].name
            price = self.items[id]["obj"].price
            quantity = self.items[id]["quantity"]
            itemtotal = self.items[id]['item_total']
            desc = self.items[id]["obj"].desc

            #check if quantity is in stock
            if quantity <= self.stockobj.getQuantity(id):
                #update stock
                newquantity = self.stockobj.getQuantity(id) - quantity
                self.stockobj.setQuantity(id, newquantity)
            else:
                return False, [f"Error: Not enough quantity for product ID {id} - {name} in stock."]
            
            # append every row in the receipt.
            msgs.append(f"{name:<8}{str(price)+"$":<6}{quantity:<10}{itemtotal:<10}{desc:<20}")
        
        msgs.append(f"-" * 60)
        msgs.append("{:<24}{}".format("Final Total", self.total))
        
        #save reciept and add to history
        self.saveReceipt(serial_number, msgs)

        #reset cart
        self.items = {}
        self.total = 0


        #Success
        return True, msgs 


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

# print(my_cart.checkout())

# my_cart.saveReceipt()

# my_stock = Stock()
# my_stock.addProductToStock(Product(107, "Butter", 199, "B."), 30)
# my_stock.loadDataFromJSONFile()

# my_stock.deleteFromStock(1000)
# my_stock.updateProduct(103, "Chipes", 350, "Lol")

# print(my_stock.set_quantity(106, 150))
# print(my_stock.get_quantity(106))


# for key, value in my_stock.products.items():
#     print(f"{key} : ==>", end="")
#     for key_, value_ in value.items():
#         print(f"{key_}: {value_.name} <--> {value_.price}  <--> {value_.desc}")
#         break

