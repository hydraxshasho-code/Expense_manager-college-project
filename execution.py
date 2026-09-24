from expense_manager import add_expense, view_expenses, delete_expense
from storage import save_expenses, load_expenses
from reports import calculate_total, category_summary, highest_expense
from validators import validate_amount, validate_category, validate_date
from utils import display_title
def main():
    expenses = load_expenses()
    while True:
        display_title("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "4":
            total = calculate_total(expenses)
            summary = category_summary(expenses)
            highest = highest_expense(expenses)

            print(f"\nTotal Expenses: ₹{total}")
            print("\nCategory Summary:")
            for category, amount in summary.items():
                print(f"{category}: ₹{amount}")

            if highest:
                print(
                    f"\nHighest Expense: ₹{highest['amount']} | "
                    f"{highest['category']} | "
                    f"{highest['date']}"
                )
            else:
                print("\nNo expenses found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
