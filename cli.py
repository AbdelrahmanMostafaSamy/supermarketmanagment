# from classes.main import LISTOFPRODUCTS
from classes.main import Cart
from classes.main import Stock
from classes.main import Product

cart = Cart()
stock = Stock()

# for prod in LISTOFPRODUCTS:
#     print(prod.id)
#     print(prod.name)
#     print(prod.desc)
#     print(prod.price)
#     print()


products = {}
cart = []


# Functions Add product in Store
def add_products():
    print("__________A D D  IN  S T O R E__________")    
    id = int(input("Enter product id: "))
    if id in stock.products.keys():
        print("product id already exists")
        return

    name = input("Enter product name: ")

    price = int(input("Enter product price: "))

    desc = input("Enter product description:")

    quantity = int(input("Enter product quantity:"))

    newProduct = Product(id, name, price, desc)

    stock.addProductToStock(newProduct, quantity)
    print("Product added successfully")


# Function Display Products
def display_products():
    print("__________PRODUCTS__________")

    for key, value in stock.products.items():
        print(f"{key} -->  {value["obj"].name} <-> {value["obj"].price} <-> {value["obj"].desc} <-> {value["Quantity"]}")
        
# Function Add To Cart
# def add_to_cart():
#     user_input = input("Enter product id (or 0 to stop): ")
#     if not user_input.isdigit():
#         print("Invalid id")
#         return
#     id = int(user_input)

#     if id == 0:
#         return

#     count_input = input("Enter quantity: ")
#     if not count_input.isdigit():
#         print("Invalid quantity")
#         return
#     count = int(count_input)

#     if id in products:
#         total_price_product = products[id][1] * count
#         cart.append({
#             "name": products[id][0],
#             "price": products[id][1],
#             "quantity": count,
#             "total": total_price_product
#         })
#         print("Product added to cart")
#     else:
#         print("Product not found")


def add_to_cart():
    while True:
        user_input = input("Enter product id (or 0 to stop): ")
        if not user_input.isdigit():
            print("Invalid id")
            continue

        prod_id = int(user_input)

        if prod_id == 0:
            print("Stopping add to cart")
            break
        if prod_id not in stock.products:
            print("Product not found")
            continue
        
        qty_input = input("Enter quantity: ")
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Invalid quantity")
            continue
        qty_input = int(qty_input)

        product = stock.products[prod_id]["obj"]
        cart.addProduct(product, qty_input)

        print(f"Added {qty_input} of {product.name} to cart.")

# Function Delete From Store
def delete_from_store():
    id = int(input("Enter product id to delete:"))
    if id in products:
        del products[id]
        print("Product deleted successfully")
    else:
        print("Product not found")


# Function Delete From Cart



# Main loop
while True:
    display_products()
    add_to_cart()
    

    checkout = input("Do you want to checkout? (y/n): ")
    if checkout.lower() == "y":
        break

print("__________C A R T__________")
