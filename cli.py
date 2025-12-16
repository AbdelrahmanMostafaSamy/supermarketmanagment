from classes.main import LISTOFPRODUCTS
from classes.main import Cart

cart = Cart()

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

    name = input("Enter product name: ")

    price = int(input("Enter product price: "))

    products[id] = [name, price]
    print("Product added successfully")


# Function Display Products
def display_products():
    print("__________PRODUCTS__________")
    for id, info in products.items():
        print(f"ID: {id}, Name: {info[0]}, Price: LE {info[1]}")


# Function Add To Cart
def add_to_cart():
    user_input = input("Enter product id (or 0 to stop): ")
    if not user_input.isdigit():
        print("Invalid id")
        return
    id = int(user_input)

    if id == 0:
        return

    count_input = input("Enter quantity: ")
    if not count_input.isdigit():
        print("Invalid quantity")
        return
    count = int(count_input)

    if id in products:
        total_price_product = products[id][1] * count
        cart.append({
            "name": products[id][0],
            "price": products[id][1],
            "quantity": count,
            "total": total_price_product
        })
        print("Product added to cart")
    else:
        print("Product not found")


# Main loop
while True:
    add_products()
    display_products()
    add_to_cart()

    checkout = input("Do you want to checkout? (y/n): ")
    if checkout.lower() == "y":
        break


total = sum(item["total"] for item in cart)

print("__________C A R T__________")
for item in cart:
    print(f"{item['name']} x{item['quantity']} = LE {item['total']}")

print("Total amount: LE", total)
