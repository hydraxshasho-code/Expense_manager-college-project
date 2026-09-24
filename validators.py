def validate_amount(amount):
    return amount > 0
def validate_category(category):
    return bool(category.strip()) and any(char.isalpha()for char in category for char in category)
def validate_date(date):
    parts = date.split('-')
    return len(parts) == 3 and all(part.isdigit() for part in parts) and len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2