# Expense Tracker
An interactive, modular command-line interface application built with python to help users manage, organize, and analyze personal finances locally . The system enforces strict input validation, maintains persistent JSON storage, provides category filtering, and alerts users upon exceeding budget thresholds.

---

## key Features

- **Expense Management**: Add new expenses with dynamic field checks or delete existing entries interactively.
- **Data Validation**: Built-in verification for non-negative amounts, accurate date formatting (`YYYY-MM-DD`), and valid string categories.
- **Category Filtering**: Search and filter logged expenses dynamically by category name.
- **Budget Alerts**: Automatic warnings in reports when total spending exceeds the limit (default: ₹10,000).
- **Analytical Reports**: View total cumulative spending, category-wise breakdowns, and the single highest transaction.
- **Persistent Storage**: Automatic read and write operations using a structured local `expenses.json` file.

---

## Project Structure

```text
ExpenseTracker/
│
├── execution.py        # Main application entry point & CLI menu loop
├── expense_manager.py  # Handlers for adding, viewing, deleting, and filtering expenses
├── reports.py          # Logic for calculations, summaries, and budget alerts
├── storage.py          # JSON reading and writing functions
├── validators.py       # Input validation logic (dates, amounts, categories)
├── utils.py            # CLI display utilities and UI headers
├── .gitignore          # Keeps temporary Python files and local JSON out of git
└── README.md           # Project documentation
```

## Technologies Used
- Python 3.8 or higher
- Standard modules (json for storage)
- Git and GitHub for version control

## Installation & Setup
1. Repository clone karein:
   ```bash
   git clone https://github.com/hydraxshasho-code/Expense_manager-college-project.git
   ```
2. Directory enter karein:
   ```bash
   cd Expense_manager-college-project
   ```
3. Run the project:
   ```bash
   python execution.py
   ```