from validators import validate_amount, validate_category, validate_date
def add_expense(expenses):
    while True:
        amount = float(input("Enter amount: "))
        if not validate_amount(amount):
            print("Invalid amount. Please enter a positive number.")
            continue
        
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        if not validate_category(category):
            print("Invalid category. Please enter a valid category.")
            continue

        if not validate_date(date):
            print("Invalid date. Please enter a valid date (YYYY-MM-DD).")
            continue

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)

        print("Expense added successfully!")

        choice = input("Add another expense? (y/n): ").lower()

        if choice != "y":
            break

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n------ EXPENSES ------")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            expenses.pop(number - 1)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


