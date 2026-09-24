import unittest

from reports import calculate_total, category_summary, highest_expense
from validators import validate_amount, validate_category, validate_date


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"amount": 500, "category": "Food", "date": "2026-09-24"},
            {"amount": 1200, "category": "Travel", "date": "2026-09-23"},
            {"amount": 300, "category": "Food", "date": "2026-09-22"}
        ]

    def test_calculate_total(self):
        self.assertEqual(calculate_total(self.expenses), 2000)

    def test_category_summary(self):
        summary = category_summary(self.expenses)

        self.assertEqual(summary["Food"], 800)
        self.assertEqual(summary["Travel"], 1200)

    def test_highest_expense(self):
        highest = highest_expense(self.expenses)

        self.assertEqual(highest["amount"], 1200)

    def test_amount_validation(self):
        self.assertTrue(validate_amount(500))
        self.assertFalse(validate_amount(-500))

    def test_date_validation(self):
        self.assertTrue(validate_date("2026-09-24"))
        self.assertFalse(validate_date("24-09-2026"))


if __name__ == "__main__":
    unittest.main()