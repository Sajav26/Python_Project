import datetime
import json
import os

# File to store data
EXPENSE_FILE = 'expenses.json'

# Function to load data from the file
def load_data():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return {"expenses": [], "income": [], "balance": 0.0}

# Function to save data to the file
def save_data(data):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new expense
def add_expense():
    amount = float(input("Enter the expense amount: "))
    date_str = input("Enter the date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    category = input("Enter the category: ")

    expense = {
        'amount': amount,
        'date': date_str,
        'category': category
    }

    data["expenses"].append(expense)
    data["balance"] -= amount  # Deduct the expense from the balance
    save_data(data)
    print("Expense added successfully!\n")

# Function to add a new income
def add_income():
    amount = float(input("Enter the income amount: "))
    date_str = input("Enter the date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    category = input("Enter the category (e.g., salary, freelance, investments): ")

    income = {
        'amount': amount,
        'date': date_str,
        'category': category
    }

    data["income"].append(income)
    data["balance"] += amount  # Add the income to the balance
    save_data(data)
    print("Income added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not data["expenses"]:
        print("No expenses recorded.\n")
        return

    print("All Expenses:")
    for expense in data["expenses"]:
        print(f"Amount: ${expense['amount']:.2f}, Date: {expense['date']}, Category: {expense['category']}")
    print()

# Function to view all income
def view_income():
    if not data["income"]:
        print("No income recorded.\n")
        return

    print("All Income:")
    for income in data["income"]:
        print(f"Amount: ${income['amount']:.2f}, Date: {income['date']}, Category: {income['category']}")
    print()

# Function to view summary of expenses and income by category and by month
def view_summary():
    if not data["expenses"] and not data["income"]:
        print("No expenses or income recorded.\n")
        return

    summary_by_category_expenses = {}
    summary_by_category_income = {}
    summary_by_month_expenses = {}
    summary_by_month_income = {}

    for expense in data["expenses"]:
        category = expense['category']
        month = expense['date'][:7]  # Extract YYYY-MM from date

        # Summary by category (expenses)
        if category not in summary_by_category_expenses:
            summary_by_category_expenses[category] = 0
        summary_by_category_expenses[category] += expense['amount']

        # Summary by month (expenses)
        if month not in summary_by_month_expenses:
            summary_by_month_expenses[month] = 0
        summary_by_month_expenses[month] += expense['amount']

    for income in data["income"]:
        category = income['category']
        month = income['date'][:7]  # Extract YYYY-MM from date

        # Summary by category (income)
        if category not in summary_by_category_income:
            summary_by_category_income[category] = 0
        summary_by_category_income[category] += income['amount']

        # Summary by month (income)
        if month not in summary_by_month_income:
            summary_by_month_income[month] = 0
        summary_by_month_income[month] += income['amount']

    print("Summary by Category (Expenses):")
    for category, total in summary_by_category_expenses.items():
        print(f"{category}: ${total:.2f}")
    print()

    print("Summary by Category (Income):")
    for category, total in summary_by_category_income.items():
        print(f"{category}: ${total:.2f}")
    print()

    print("Summary by Month (Expenses):")
    for month, total in summary_by_month_expenses.items():
        print(f"{month}: ${total:.2f}")
    print()

    print("Summary by Month (Income):")
    for month, total in summary_by_month_income.items():
        print(f"{month}: ${total:.2f}")
    print()

    print(f"Current Balance: ${data['balance']:.2f}\n")

# Main program loop
data = load_data()

while True:
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add Income")
    print("4. View Income")
    print("5. View Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        add_income()
    elif choice == '4':
        view_income()
    elif choice == '5':
        view_summary()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.\n")
