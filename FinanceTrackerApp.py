import tkinter as tk
from tkinter import messagebox

class FinanceTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Finance Tracker")

        # Data structure to store transactions
        self.transactions = []

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for entering transaction description
        tk.Label(self.master, text="Transaction Description:").pack(pady=5)
        self.transaction_description_entry = tk.Entry(self.master, width=30)
        self.transaction_description_entry.pack(pady=5)

        # Label and Entry for entering transaction amount
        tk.Label(self.master, text="Transaction Amount:").pack(pady=5)
        self.transaction_amount_entry = tk.Entry(self.master, width=15)
        self.transaction_amount_entry.pack(pady=5)

        # Radio buttons for selecting transaction type (income or expense)
        self.transaction_type_var = tk.StringVar()
        self.transaction_type_var.set("Expense")
        tk.Radiobutton(self.master, text="Income", variable=self.transaction_type_var, value="Income").pack(pady=5)
        tk.Radiobutton(self.master, text="Expense", variable=self.transaction_type_var, value="Expense").pack(pady=5)

        # Button to add transaction
        tk.Button(self.master, text="Add Transaction", command=self.add_transaction).pack(pady=10)

        # Listbox to display transactions
        self.transaction_listbox = tk.Listbox(self.master, width=50, height=10)
        self.transaction_listbox.pack(pady=10)

        # Button to display total balance
        tk.Button(self.master, text="Show Balance", command=self.show_balance).pack(pady=10)

    def add_transaction(self):
        description = self.transaction_description_entry.get()
        amount = self.transaction_amount_entry.get()
        transaction_type = self.transaction_type_var.get()

        if description and amount:
            amount = float(amount) if transaction_type == "Income" else float(amount) * -1
            self.transactions.append((description, amount))
            self.update_transaction_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter both description and amount.")

    def update_transaction_list(self):
        self.transaction_listbox.delete(0, tk.END)
        for transaction in self.transactions:
            self.transaction_listbox.insert(tk.END, f"{transaction[0]}: Rs.{transaction[1]:.2f}")

    def show_balance(self):
        total_balance = sum(transaction[1] for transaction in self.transactions)
        messagebox.showinfo("Total Balance", f"Total Balance: Rs.{total_balance:.2f}")

    def clear_entries(self):
        self.transaction_description_entry.delete(0, tk.END)
        self.transaction_amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()
