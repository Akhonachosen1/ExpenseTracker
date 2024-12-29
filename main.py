import os
import tkinter as tk
from tkinter import messagebox


# Save expenses to a file
def save_expenses(expenses, file_name="expenses.txt"):
    with open(file_name, "w") as file:
        for exp in expenses:
            file.write(f"{exp['category']},{exp['amount']}\n")


# Load expenses from a file
def load_expenses(file_name="expenses.txt"):
    expenses = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({"category": category, "amount": float(amount)})
    return expenses


# Add a new expense
def add_expense():
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()

    if not category or not amount:
        messagebox.showerror("Error", "Both fields are required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    expenses.append({"category": category, "amount": amount})
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    update_display()
    messagebox.showinfo("Success", "Expense added successfully!")


# Update the display area with all expenses
def update_display():
    expense_list.delete(0, tk.END)
    total_expenses = 0

    for exp in expenses:
        expense_list.insert(tk.END, f"{exp['category']}: {exp['amount']:.2f}")
        total_expenses += exp['amount']

    total_label.config(text=f"Total Expenses: {total_expenses:.2f}")


# Save and Exit
def save_and_exit():
    save_expenses(expenses)
    root.destroy()


# Load existing expenses
expenses = load_expenses()

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# UI Elements
category_label = tk.Label(root, text="Category:")
category_label.grid(row=0, column=0, padx=10, pady=5)

category_entry = tk.Entry(root)
category_entry.grid(row=0, column=1, padx=10, pady=5)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=1, column=0, padx=10, pady=5)

amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

expense_list = tk.Listbox(root, width=40, height=10)
expense_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

total_label = tk.Label(root, text="Total Expenses: 0.00", font=("Arial", 12))
total_label.grid(row=4, column=0, columnspan=2, pady=10)

save_exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)
save_exit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Populate the display area with any preloaded expenses
update_display()

# Start the main loop
root.mainloop()
