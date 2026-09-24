import json as j
FILE_NAME = "expenses.json"
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        j.dump(expenses, file, indent=4)
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = j.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses
