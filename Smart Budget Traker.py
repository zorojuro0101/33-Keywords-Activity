import random
import time

# Global variables for budget and expenses
budget = 0
expenses = []

# Define the Expense class
class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.name}: ₱{self.amount:.2f}"

# Function to set budget
def set_budget():
    global budget
    while True:
        try:
            budget = float(input("Enter your monthly budget: ₱"))
            if budget > 0:
                print(f"Budget set to ₱{budget:.2f}\n")
                break
            else:
                print("Budget must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to add an expense
def add_expense():
    global expenses
    name = input("Enter the expense name: ")
    while True:
        try:
            amount = float(input("Enter the amount: ₱"))
            if amount > 0:
                break
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount. Try again.")
    
    expenses.append(Expense(name, amount))
    print(f"Expense '{name}' of ₱{amount:.2f} added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\nExpense Summary:")
    total_spent = 0
    for expense in expenses:
        print(expense)
        total_spent += expense.amount

    print(f"\nTotal Spent: ₱{total_spent:.2f}")
    remaining_budget = budget - total_spent

    if remaining_budget > 0:
        print(f"Remaining Budget: ₱{remaining_budget:.2f}\n")
    elif remaining_budget == 0:
        print("Budget exhausted! You’ve spent everything.\n")
    else:
        print(f"Over budget by ₱{-remaining_budget:.2f}! Cut down on expenses.\n")

# Function to delete an expense
def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses()
    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            deleted_expense = expenses.pop(choice - 1)
            print(f"Expense '{deleted_expense.name}' deleted successfully!\n")
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to check if budget is exceeded
# Function to check if budget is exceeded or give updates
def check_budget():
    total_spent = sum(expense.amount for expense in expenses)
    remaining_budget = budget - total_spent

    if remaining_budget < 0:
        print(f"Alert! You've exceeded your budget by ₱{-remaining_budget:.2f}.")
    elif remaining_budget < budget * 0.1:
        print("Warning! You’re about to hit your budget limit. Be cautious!")
    else:
        print(f"Your remaining budget is ₱{remaining_budget:.2f}. You are on track!")


# Main budget tracking function
def main():
    print("Welcome to Smart Budget Tracker!")
    set_budget()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Check Budget")
        print("5. Quit")

        choice = input("Choose an action (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            check_budget()
        elif choice == "5":
            print("Thanks for using Smart Budget Tracker. Stay financially smart!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the main function safely
try:
    main()
except Exception as e:
    print(f"Something went wrong: {e}")
