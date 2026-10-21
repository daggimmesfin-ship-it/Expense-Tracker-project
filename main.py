
import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: The expense file is empty or invalid.")
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount > 0:
                break

            print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty.")
        return

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added and saved successfully!")


# Display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== All Expenses =====")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. Amount: {expense['amount']:.2f} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']}"
        )


# Calculate total expenses
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Display total expenses
def display_total(expenses):
    print(f"Total expenses: {calculate_total(expenses):.2f}")


# Load saved expenses when the program starts
expenses = load_expenses()


# Main menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add expense")
    print("2. Display all expenses")
    print("3. Display total expenses")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        display_expenses(expenses)

    elif choice == "3":
        display_total(expenses)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1-4.")
