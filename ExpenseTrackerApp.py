import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        # Data structure to store expenses
        self.expenses = []

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for entering expense description
        tk.Label(self.master, text="Expense Description:").pack(pady=5)
        self.expense_description_entry = tk.Entry(self.master, width=30)
        self.expense_description_entry.pack(pady=5)

        # Label and Entry for entering expense amount
        tk.Label(self.master, text="Expense Amount:").pack(pady=5)
        self.expense_amount_entry = tk.Entry(self.master, width=15)
        self.expense_amount_entry.pack(pady=5)

        # Button to add expense
        tk.Button(self.master, text="Add Expense", command=self.add_expense).pack(pady=10)

        # Listbox to display expenses
        self.expense_listbox = tk.Listbox(self.master, width=50, height=10)
        self.expense_listbox.pack(pady=10)

        # Button to display total expenses
        tk.Button(self.master, text="Show Total Expenses", command=self.show_total_expenses).pack(pady=10)

    def add_expense(self):
        description = self.expense_description_entry.get()
        amount = self.expense_amount_entry.get()

        if description and amount:
            self.expenses.append((description, float(amount)))
            self.update_expense_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter both description and amount.")

    def update_expense_list(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, f"{expense[0]}: Rs.{expense[1]:.2f}")

    def show_total_expenses(self):
        total_expenses = sum(expense[1] for expense in self.expenses)
        messagebox.showinfo("Total Expenses", f"Total Expenses: Rs.{total_expenses:.2f}")

    def clear_entries(self):
        self.expense_description_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
