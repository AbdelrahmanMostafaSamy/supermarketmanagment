import customtkinter as ctk
from tkinter import ttk
from classes.main import Cart, LISTOFPRODUCTS
# Colors config
C_SIDE = "#1B4D3E"  # Dark Green
C_BG = "#F2F0E4"    # Beige
C_ACCENT = "#E6A526" # Orange

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

class SupermarketGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # window setup
        self.title("Supermarket System")
        self.geometry("1100x700")
        self.resizable(False, False)

        self.cart = Cart() # call backend class

        # grid layout 
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        # 1. Sidebar Frame
        self.side_fr = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color=C_SIDE)
        self.side_fr.grid(row=0, column=0, sticky="nsew")

        lbl = ctk.CTkLabel(self.side_fr, text="التوحيد و النور", font=ctk.CTkFont(size=25, weight="bold"), text_color="white")
        lbl.pack(pady=30)
        
        # menu buttons
        btns = ["Invoice", "Add Items", "History"]
        for b_text in btns:
            btn = ctk.CTkButton(self.side_fr, text=b_text, fg_color="transparent", hover_color="#143A2F", anchor="w", height=40)
            btn.pack(fill="x", padx=10, pady=5)

        # exit button
        ext_btn = ctk.CTkButton(self.side_fr, text="End Shift", fg_color="#922B21", hover_color="#641E16", anchor="w", command=self.destroy)
        ext_btn.pack(fill="x", padx=10, pady=20, side="bottom")

        # 2. Main Center Area
        self.main_fr = ctk.CTkFrame(self, corner_radius=0, fg_color=C_BG)
        self.main_fr.grid(row=0, column=1, sticky="nsew")

        # input row
        in_fr = ctk.CTkFrame(self.main_fr, fg_color="transparent")
        in_fr.pack(fill="x", padx=20, pady=20)

        self.prod_var = ctk.StringVar(value="Select Product")
        self.combo = ctk.CTkOptionMenu(in_fr, variable=self.prod_var, fg_color="white", text_color="black", button_color=C_ACCENT, button_hover_color="#C58B1F")
        self.combo.pack(side="left", fill="x", expand=True, padx=(0,10))

        add = ctk.CTkButton(in_fr, text="+ Add", fg_color=C_ACCENT, text_color="black", font=ctk.CTkFont(weight="bold"), command=self.add_item)
        add.pack(side="right")

        # Table area
        tbl_fr = ctk.CTkFrame(self.main_fr, fg_color="transparent")
        tbl_fr.pack(fill="both", expand=True, padx=20)
        
        # treeview styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=30, background="white", font=("Arial", 12))
        style.configure("Treeview.Heading", background="#E0E0E0", font=("Arial", 12, "bold"))

        cols = ("Name", "Price", "Qty", "Total")
        self.tree = ttk.Treeview(tbl_fr, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c)
            w = 150 if c == "Name" else 80
            self.tree.column(c, width=w)
        self.tree.pack(fill="both", expand=True)

        # total row
        tot_fr = ctk.CTkFrame(self.main_fr, fg_color="#E0E0E0", height=60)
        tot_fr.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(tot_fr, text="Total:", font=("Arial", 16), text_color="black").pack(side="left", padx=20)
        self.lbl_tot = ctk.CTkLabel(tot_fr, text="0.0 EGP", font=("Arial", 24, "bold"), text_color=C_SIDE)
        self.lbl_tot.pack(side="right", padx=20)

        # save button
        ctk.CTkButton(self.main_fr, text="Print Receipt", fg_color="#C0392B", hover_color="#A93226", command=self.print_rec).pack(fill="x", padx=20, pady=(0,20))

        # 3. Receipt Preview (Right side)
        rec_fr = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color="#FAF9F6")
        rec_fr.grid(row=0, column=2, sticky="nsew", padx=(2,0))
        
        ctk.CTkLabel(rec_fr, text="Receipt Preview", font=("Arial", 18, "bold"), text_color=C_SIDE).pack(pady=20)
        self.txt_rec = ctk.CTkTextbox(rec_fr, fg_color="white", text_color="black", font=("Courier", 12))
        self.txt_rec.pack(fill="both", expand=True, padx=15, pady=10)
        self.txt_rec.configure(state="disabled")

    def load_products(self):
        # fill combobox from main list
        p_names = [p.name for p in LISTOFPRODUCTS]
        self.combo.configure(values=p_names)
        if p_names: self.prod_var.set(p_names[0])

    def add_item(self):
        name = self.prod_var.get()
        # simple search
        found = next((p for p in LISTOFPRODUCTS if p.name == name), None)
        if found:
            self.cart.addProduct(found, 1)
            self.refresh_ui()

    def refresh_ui(self):
        # clean table
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # get data
        items, tot = self.cart.getCart()
        for i, d in items.items():
            row = (d['obj'].name, f"{d['obj'].price}", d['quantity'], f"{d['itemtotal']}")
            self.tree.insert("", "end", values=row)
            
        self.lbl_tot.configure(text=f"{tot} EGP")
        
        # update preview
        lines = self.cart.checkout()
        self.txt_rec.configure(state="normal")
        self.txt_rec.delete("0.0", "end")
        for l in lines:
            self.txt_rec.insert("end", l + "\n")
        self.txt_rec.configure(state="disabled")

    def print_rec(self):
        self.cart.saveReceipt()

if __name__ == "__main__":
    app = SupermarketGUI()
    app.mainloop()