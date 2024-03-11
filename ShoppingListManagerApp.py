import tkinter as tk
from tkinter import ttk, messagebox

class ShoppingListManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping List Manager")

        # Data structure to store shopping items
        self.shopping_items = []

        # Predefined list of shopping item categories
        self.categories = [
            "Groceries",
            "Household Essentials",
            "Personal Care",
            "Clothing and Accessories",
            "Electronics",
            "Home Decor",
            "Office and School Supplies",
            "Appliances",
            "Health and Wellness",
            "Pet Supplies",
            "Outdoor and Sporting Goods",
            "Baby and Kids"
        ]

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for entering shopping item
        tk.Label(self.master, text="Shopping Item:").pack(pady=5)
        self.shopping_item_entry = tk.Entry(self.master, width=30)
        self.shopping_item_entry.pack(pady=5)

        # Label and Dropdown for selecting item category
        tk.Label(self.master, text="Item Category:").pack(pady=5)
        self.item_category_var = tk.StringVar()
        self.item_category_dropdown = ttk.Combobox(self.master, textvariable=self.item_category_var, values=self.categories, state="readonly")
        self.item_category_dropdown.set(self.categories[0])  # Set default category
        self.item_category_dropdown.pack(pady=5)

        # Label and Entry for entering store name
        tk.Label(self.master, text="Store Name:").pack(pady=5)
        self.store_name_entry = tk.Entry(self.master, width=20)
        self.store_name_entry.pack(pady=5)

        # Button to add shopping item
        tk.Button(self.master, text="Add Item to List", command=self.add_shopping_item).pack(pady=10)

        # Listbox to display shopping items
        self.shopping_items_listbox = tk.Listbox(self.master, width=50, height=10)
        self.shopping_items_listbox.pack(pady=10)

        # Button to show categorized shopping list
        tk.Button(self.master, text="Show Categorized List", command=self.show_categorized_list).pack(pady=10)

    def add_shopping_item(self):
        item_name = self.shopping_item_entry.get()
        category = self.item_category_var.get()
        store_name = self.store_name_entry.get()

        if item_name:
            self.shopping_items.append((item_name, category, store_name))
            self.update_shopping_items_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter the shopping item.")

    def update_shopping_items_list(self):
        self.shopping_items_listbox.delete(0, tk.END)
        for item in self.shopping_items:
            self.shopping_items_listbox.insert(tk.END, f"{item[0]} - {item[1]} - {item[2]}")

    def show_categorized_list(self):
        if not self.shopping_items:
            messagebox.showinfo("Empty List", "The shopping list is empty.")
            return

        categorized_list_str = "Shopping List:\n\n"
        for item in self.shopping_items:
            categorized_list_str += f"{item[0]} - {item[1]} - {item[2]}\n"

        messagebox.showinfo("Shopping List", categorized_list_str)

    def clear_entries(self):
        self.shopping_item_entry.delete(0, tk.END)
        self.item_category_dropdown.set(self.categories[0])  # Set default category
        self.store_name_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListManagerApp(root)
    root.mainloop()
