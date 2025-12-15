from classes.main import LISTOFPRODUCTS
from classes.main import Cart

cart = Cart()

# for prod in LISTOFPRODUCTS:
#     print(prod.id)
#     print(prod.name)
#     print(prod.desc)
#     print(prod.price)
#     print()



products = {
    101: ["vcola", 15],
    102: ["pepsi", 18],
    103: ["milk", 50],
}
cart = []

while True:

    user_input = input("Enter product id (or 0 to stop): ")

    id = int(user_input)

    if id == 0:
        break

    count_input = input("Enter quantity: ")
    count = int(count_input)

    if id in products:
        total_price_product = 0
        total_price_product += products[id][1] * count

        cart.append({
            "name": products[id][0],
            "price": products[id][1],
            "quantity": count,
            "total": total_price_product
        })
        print("product added to cart")
    else :
        print("Product not foun")
    
    cheskout = input("Do you want to checkout? (y/n): ")
    if cheskout.lower() == "y":
        break

total = sum(itmem["price"] * itmem["quantity"] for itmem in cart)

print("__________C A R T__________")
for item in cart:
    print(f"{item['name']} x{item['quantity']} = LE {item['total']}")

print("Total amount: LE ", total)