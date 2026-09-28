from expense_manager import (
    add_expense,
    view_expenses,
    delete_expense,
    filter_expenses_by_category,
)
from storage import save_expenses, load_expenses
from reports import (
    calculate_total,
    category_summary,
    highest_expense,
    check_budget_alert,
)
from utils import display_title


def main():
    expenses = load_expenses()
    while True:
        display_title("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Delete Expense")
        print("5. View Reports & Budget Alert")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            filter_expenses_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "5":
            total = calculate_total(expenses)
            summary = category_summary(expenses)
            highest = highest_expense(expenses)

            print(f"\nTotal Expenses: ₹{total}")
            check_budget_alert(expenses, limit=10000)

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
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()