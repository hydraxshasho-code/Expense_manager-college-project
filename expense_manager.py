from validators import validate_amount, validate_category, validate_date
def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if not validate_amount(amount):
            print("Invalid amount. Please enter a positive number.")
            continue
        
        category = input("Enter category: ").strip()
        if not validate_category(category):
            print("Invalid category. Please enter a valid category name.")
            continue

        date = input("Enter date (YYYY-MM-DD): ").strip()
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

        choice = input("Add another expense? (y/n): ").lower().strip()
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

def filter_expenses_by_category(expenses):
    if not expenses:
        print("No expenses to filter.")
        return
    
    cat = input("Enter category to search: ").strip().lower()
    filtered = [e for e in expenses if e['category'].lower() == cat]
    
    if not filtered:
        print(f"No expenses found for category '{cat}'.")
        return
    
    print(f"\n------ EXPENSES FOR '{cat.upper()}' ------")
    for i, e in enumerate(filtered, start=1):
        print(f"{i}. ₹{e['amount']} | {e['date']}")



