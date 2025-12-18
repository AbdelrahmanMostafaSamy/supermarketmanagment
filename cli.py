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
        print(
            f"{key} --> {value['obj'].name} | "
            f"{value['obj'].price} | "
            f"{value['obj'].desc} | "
            f"{value['Quantity']}"
        )

# Function Add to Cart
def add_to_cart():
    print("\n__________A D D  T O  C A R T__________")
    user_input = input("Enter product id (or 0 to stop): ")
    if not user_input.isdigit():
        print("Invalid id")
        return False

    prod_id = int(user_input)

    if prod_id == 0:
        return False

    if prod_id not in stock.products:
        print("Product not found")
        return True

    qty_input = input("Enter quantity: ")
    if not qty_input.isdigit() or int(qty_input) <= 0:
        print("Invalid quantity")
        return True

    quantity = int(qty_input)

    product = stock.products[prod_id]["obj"]
    cart.addProduct(product, quantity)

    print(f"Added {quantity} of {product.name} to cart.")
    return True

# Function Delete From Cart
def delete_from_cart():
    print("\n__________DELETE FROM CART__________")    
    id = int(input("Enter product id to delete from cart: "))
    if id in cart.items:
        del cart.items[id]
        cart.update_total()
        print("Product removed from cart")
    else:
        print("Product not found in cart")



def prints():
    while True:
        print("\n__________M A I N   M E N U__________")
        print("1. Add product to store")
        print("2. Display products in store")
        print("3. Add product to cart")
        print("4. Delete product from cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_products()
        elif choice == "2":
            display_products()
        elif choice == "3":
            while True:
                if not add_to_cart():
                    break
        elif choice == "4":
            delete_from_cart()
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
    

# Main loop
prints()