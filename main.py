import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import date

# CSV Files
EXPENSE_FILE = "expenses.csv"
INCOME_FILE = "income.csv"
BUDGET_FILE = "budget.csv"


# Create CSV Files
def create_files():

    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

    if not os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Description"])

    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Budget"])


# Read Income
def get_income():

    with open(INCOME_FILE, "r") as file:
        return list(csv.DictReader(file))


# Read Expenses
def get_expenses():

    with open(EXPENSE_FILE, "r") as file:
        return list(csv.DictReader(file))


# Calculate Total
def calculate_totals():

    income = get_income()
    expenses = get_expenses()

    total_income = sum(float(i["Amount"]) for i in income)
    total_expense = sum(float(e["Amount"]) for e in expenses)

    balance = total_income - total_expense

    return total_income, total_expense, balance


# Update Dashboard
def update_dashboard():

    income, expense, balance = calculate_totals()

    income_label.config(text=f"₹ {income:.2f}")
    expense_label.config(text=f"₹ {expense:.2f}")
    balance_label.config(text=f"₹ {balance:.2f}")


# Add Income Function
def add_income():

    try:
        amount = float(income_amount.get())
        description = income_description.get()

        if amount <= 0:
            messagebox.showerror("Error", "Enter a positive amount!")
            return

        with open(INCOME_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), amount, description])

        messagebox.showinfo("Success", "Income Added Successfully!")

        income_amount.delete(0, tk.END)
        income_description.delete(0, tk.END)

        update_dashboard()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")


# Add Expense Function
def add_expense():

    try:
        category = category_box.get()
        amount = float(expense_amount.get())
        description = expense_description.get()

        if not category:
            messagebox.showerror("Error", "Please select a category!")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Enter a positive amount!")
            return

        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                date.today(), category, amount, description
            ])

        messagebox.showinfo("Success", "Expense Added Successfully!")

        expense_amount.delete(0, tk.END)
        expense_description.delete(0, tk.END)

        update_dashboard()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount!")


# Start Application
create_files()

root = tk.Tk()
root.title("Personal Expense & Budget Tracker")
root.geometry("1100x750")
root.configure(bg="#F2F4F8")


# Heading
heading = tk.Label(
    root,
    text="PERSONAL EXPENSE & BUDGET TRACKER",
    font=("Arial", 22, "bold"),
    bg="#263238",
    fg="white",
    pady=20
)

heading.pack(fill="x")


# Welcome Message
welcome = tk.Label(
    root,
    text="Manage Your Money, Track Your Expenses!",
    font=("Arial", 15),
    bg="#F2F4F8",
    fg="#263238"
)

welcome.pack(pady=15)


# Dashboard
dashboard = tk.Frame(root, bg="#F2F4F8")
dashboard.pack(pady=15)


# Dashboard Cards
def create_card(title, color):

    frame = tk.Frame(
        dashboard,
        bg="white",
        width=230,
        height=100
    )

    frame.pack(side="left", padx=12)
    frame.pack_propagate(False)

    tk.Label(
        frame,
        text=title,
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#555555"
    ).pack(pady=10)

    label = tk.Label(
        frame,
        text="₹ 0.00",
        font=("Arial", 18, "bold"),
        bg="white",
        fg=color
    )

    label.pack()

    return label


income_label = create_card("Total Income", "#16A085")
expense_label = create_card("Total Expenses", "#E74C3C")
balance_label = create_card("Available Balance", "#2980B9")


# Main Form Area
form_frame = tk.Frame(root, bg="#F2F4F8")
form_frame.pack(pady=25)


# Income Form
income_frame = tk.LabelFrame(
    form_frame,
    text="ADD INCOME",
    font=("Arial", 13, "bold"),
    bg="white",
    padx=25,
    pady=20
)

income_frame.pack(side="left", padx=20)


tk.Label(
    income_frame,
    text="Income Amount",
    bg="white"
).pack(anchor="w")

income_amount = tk.Entry(income_frame, width=30)
income_amount.pack(pady=8)


tk.Label(
    income_frame,
    text="Description",
    bg="white"
).pack(anchor="w")

income_description = tk.Entry(income_frame, width=30)
income_description.pack(pady=8)


tk.Button(
    income_frame,
    text="ADD INCOME",
    bg="#16A085",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_income,
    width=22
).pack(pady=15)


# Expense Form
expense_frame = tk.LabelFrame(
    form_frame,
    text="ADD EXPENSE",
    font=("Arial", 13, "bold"),
    bg="white",
    padx=25,
    pady=20
)

expense_frame.pack(side="left", padx=20)


tk.Label(
    expense_frame,
    text="Select Category",
    bg="white"
).pack(anchor="w")


category_box = ttk.Combobox(
    expense_frame,
    values=[
        "Food",
        "Travel",
        "Shopping",
        "Education",
        "Bills",
        "Entertainment",
        "Other"
    ],
    state="readonly",
    width=27
)

category_box.pack(pady=8)


tk.Label(
    expense_frame,
    text="Expense Amount",
    bg="white"
).pack(anchor="w")

expense_amount = tk.Entry(expense_frame, width=30)
expense_amount.pack(pady=8)


tk.Label(
    expense_frame,
    text="Description",
    bg="white"
).pack(anchor="w")

expense_description = tk.Entry(expense_frame, width=30)
expense_description.pack(pady=8)


tk.Button(
    expense_frame,
    text="ADD EXPENSE",
    bg="#E74C3C",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_expense,
    width=22
).pack(pady=15)


# Footer
footer = tk.Label(
    root,
    text="Personal Expense Tracker | Python Tkinter Project",
    font=("Arial", 10),
    bg="#263238",
    fg="white",
    pady=12
)

footer.pack(side="bottom", fill="x")


# Update Dashboard
update_dashboard()


# Run Application
root.mainloop()