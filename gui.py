import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import main as m
import winsound

class SuperMarketGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Super Market")
        self.geometry("1200x750")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")

        self.cart_logic = m.Cart()
        self.cart_rows = {}

        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0) 
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT SIDE ---
        self.main_container = ctk.CTkFrame(self, fg_color="#D9D9D9", corner_radius=16)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        
        #Left Side Text
        self.title_label = ctk.CTkLabel(self.main_container, text="سوبرماركت", font=("Arial Bold", 60), text_color="#1a1a1a")
        self.title_label.pack(pady=(30, 10), padx=50, anchor="nw")
        
        #Left Side Scroll
        self.scroll_frame = ctk.CTkScrollableFrame(self.main_container, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=40, pady=10)

        # --- RIGHT SIDE (CART) ---
        self.cart_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", width=350, corner_radius=30)
        self.cart_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.cart_frame.grid_propagate(False)
        
        #Right Side Text
        self.cart_label = ctk.CTkLabel(self.cart_frame, text="السلة", font=("Arial Bold", 28))
        self.cart_label.pack(pady=(40, 20))
        
        #Right Side Scroll
        self.cart_items_container = ctk.CTkScrollableFrame(self.cart_frame, fg_color="transparent")
        self.cart_items_container.pack(fill="both", expand=True, padx=10)
        
        #Total Label
        self.total_price_label = ctk.CTkLabel(self.cart_frame, text="Total: 0 EGP", font=("Arial Bold", 22), text_color="#7EE37E")
        self.total_price_label.pack(side="bottom", pady=(10, 5))

        self.checkout_btn = ctk.CTkButton(self.cart_frame, text="شراء", 
                                          fg_color="#7EE37E", text_color="black",
                                          hover_color="#6BC96B", height=45, corner_radius=12,
                                          font=("Arial Bold", 15), command=self.process_checkout)
        self.checkout_btn.pack(side="bottom", fill="x", padx=25, pady=20)

        self.draw_product_grid()

    def update_total_display(self):
        current_total = self.cart_logic.update_total()
        self.total_price_label.configure(text=f"Total: {current_total} EGP")


    def draw_product_grid(self):
        num_columns = 4
        stock = m.Stock()
        for i,v in enumerate(stock.products.values()): 
            product = v["obj"]
            r, c = i // num_columns, i % num_columns
            card = ctk.CTkFrame(self.scroll_frame, fg_color="#242424", width=180, height=280, corner_radius=15)
            card.grid(row=r, column=c, padx=12, pady=12)
            card.grid_propagate(False) 
            ctk.CTkLabel(card, text=product.name, font=("Arial Bold", 25)).pack(pady=(20, 5))
            ctk.CTkLabel(card, text=product.desc, font=("Arial", 17), text_color="#888888", wraplength=140).pack()
            ctk.CTkLabel(card, text=f"{product.price} EGP", font=("Arial Bold", 20), text_color="#7EE37E").pack(pady=5)
            ctk.CTkFrame(card,width=170,height=20, fg_color="transparent").pack()
            ctk.CTkButton(card, text="اضافة", fg_color="#D9D9D9", text_color="#1a1a1a", 
                          hover_color="#6BC96B", width=120, height=35, corner_radius=8,font=("Arial Bold", 15),
                          command=lambda prod=product: self.add_to_cart_ui(prod)).pack(side="bottom", pady=15)

    def add_to_cart_ui(self, product):
        if product.id in self.cart_rows:
            self.cart_rows[product.id](1)
        else:
            self.cart_logic.addProduct(product, 1)
            self.create_cart_item_row(product)
        self.update_total_display()

    def create_cart_item_row(self, product):
        item_row = ctk.CTkFrame(self.cart_items_container, fg_color="#D9D9D9", height=45, corner_radius=10)
        item_row.pack(fill="x", padx=5, pady=6)
        item_row.pack_propagate(False)

        count_label = ctk.CTkLabel(item_row, text="1", text_color="black", font=("Arial Bold", 12))

        def update_qty(amount):
            curr = int(count_label.cget("text"))
            if amount > 0:
                self.cart_logic.addProduct(product, 1)
                count_label.configure(text=str(curr + 1))
            elif curr > 1:
                self.cart_logic.removeProduct(product, 1)
                count_label.configure(text=str(curr - 1))
            else:
                self.cart_logic.removeProduct(product, 1)
                if product.id in self.cart_rows:
                    del self.cart_rows[product.id]
                item_row.destroy()
            self.update_total_display() 

        self.cart_rows[product.id] = update_qty

        ctk.CTkLabel(item_row, text=product.name, text_color="black", font=("Arial Bold", 13)).pack(side="left", padx=10)
        
        ctk.CTkButton(item_row, text="🗑", width=25, fg_color="transparent", text_color="black", 
                      hover_color="#AF3030", 
                      command=lambda: [self.cart_logic.removeProduct(product, int(count_label.cget("text"))), 
                                       self.cart_rows.pop(product.id, None), 
                                       item_row.destroy(),
                                       self.update_total_display()]).pack(side="right", padx=5)
        
        ctk.CTkButton(item_row, text="+", width=25, height=25, fg_color="#1e1e1e", command=lambda: update_qty(1)).pack(side="right", padx=2)
        count_label.pack(side="right", padx=5)
        ctk.CTkButton(item_row, text="-", width=25, height=25, fg_color="#1e1e1e", command=lambda: update_qty(-1)).pack(side="right", padx=2)

    def process_checkout(self):
        success, msg = self.cart_logic.checkout()
        print("\n".join(msg))
        if success:
            for child in self.cart_items_container.winfo_children():
                child.destroy()
            self.cart_rows = {}
            self.update_total_display()
            CTkMessagebox(title="تحقق", message= "تم اصدار الفاتورة بنجاح", icon="check" , font=("Arial",22,"bold"))
            winsound.MessageBeep(winsound.MB_OK)
        else:
            CTkMessagebox(title="خطأ", message=msg , icon="cancel",font=("Arial",22,"bold"))
            winsound.MessageBeep(winsound.MB_ICONHAND)

if __name__ == "__main__":
    app = SuperMarketGUI()
    app.mainloop()
