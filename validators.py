from datetime import datetime

def validate_amount(amount):
    return amount > 0

def validate_category(category):
    return bool(category.strip()) and any(char.isalpha() for char in category)

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False