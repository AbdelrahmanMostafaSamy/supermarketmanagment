import customtkinter as ctk
from classes.main import LISTOFPRODUCTS
class SuperMarketGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Super Market")
        self.geometry("1200x750")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")

        # Configure layout weights
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=0) 
        self.grid_rowconfigure(0, weight=1)

        self.main_container = ctk.CTkFrame(self, fg_color="#D9D9D9", corner_radius=0)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        
        self.title_label = ctk.CTkLabel(self.main_container, text="super market", 
                                        font=("Arial Bold", 60), text_color="#1a1a1a")
        self.title_label.pack(pady=(30, 10), padx=50, anchor="nw")

        self.scroll_frame = ctk.CTkScrollableFrame(self.main_container, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=40, pady=10)

        self.draw_product_grid()

        # --- RIGHT SIDE: CART SIDEBAR ---
        self.cart_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", width=320, corner_radius=30)
        self.cart_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.cart_frame.grid_propagate(False)

        self.cart_label = ctk.CTkLabel(self.cart_frame, text="CART", font=("Arial Bold", 28))
        self.cart_label.pack(pady=(40, 20))

        # Placeholder items in cart
        for _ in range(6):
            self.create_cart_item()

        # Checkout button at bottom
        self.checkout_btn = ctk.CTkButton(self.cart_frame, text="cheak out", 
                                          fg_color="#7EE37E", text_color="black",
                                          hover_color="#6BC96B", height=45, corner_radius=12,
                                          font=("Arial Bold", 15))
        self.checkout_btn.pack(side="bottom", fill="x", padx=25, pady=30)

    def draw_product_grid(self):
        for r in range(3):
            for c in range(5):
                # Product Card
                card = ctk.CTkFrame(self.scroll_frame, fg_color="#242424", 
                                    width=120, height=250, corner_radius=15)
                card.grid(row=r, column=c, padx=12, pady=12)
                card.grid_propagate(False)

                ctk.CTkLabel(card, text="text\nsometing", font=("Arial Bold", 20)).pack(pady=(45, 5))
                ctk.CTkLabel(card, text="150EP", font=("Arial", 12), 
                             text_color="#888888").pack()
                ctk.CTkFrame(card, width=120, height=1, fg_color="#888888").pack()
                ctk.CTkButton(card, 
                              text="Add to cart", 
                              fg_color="#D9D9D9", 
                              text_color="#1a1a1a", 
                              hover_color="#6BC96B",
                              width=100,      
                              height=30,     
                              corner_radius=8, 
                              font=("Arial Bold", 12)
                              ).pack(side="bottom", pady=20)

    def create_cart_item(self):
        item_row = ctk.CTkFrame(self.cart_frame, fg_color="#D9D9D9", height=40, corner_radius=10)
        item_row.pack(fill="x", padx=20, pady=6)
        item_row.pack_propagate(False)

        ctk.CTkLabel(item_row, text="text", text_color="black", font=("Arial", 13)).pack(side="left", padx=12)
        
        # Quantity controls
        ctk.CTkButton(item_row, text="🗑", width=10,fg_color="transparent", font=("Arial Bold", 15), text_color="black", hover_color="#AF3030",).pack(side="right", padx=1)
        ctk.CTkButton(item_row, text="+", width=24, height=24, fg_color="#1e1e1e", corner_radius=5).pack(side="right", padx=5)
        ctk.CTkLabel(item_row, text="1", text_color="black", font=("Arial Bold", 12)).pack(side="right", padx=2)
        ctk.CTkButton(item_row, text="-", width=27, height=27, fg_color="#1e1e1e", font=("Arial Bold", 12), corner_radius=5).pack(side="right", padx=5)
        

if __name__ == "__main__":
    app = SuperMarketGUI()
    app.mainloop()
