def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    return total
def category_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    return summary
def highest_expense(expenses):
    if not expenses:
        return None
    highest = max(expenses, key=lambda x: x['amount'])
    return highest