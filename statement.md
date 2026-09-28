# Project Statement - Personal Expense Tracker

## Problem Statement
Managing daily personal expenses manually often leads to poor budget tracking and untracked spending. Most available applications are cluttered with unnecessary online features or require continuous internet access and account sign-ups. There is a need for a lightweight, terminal-based tool that allows users to quickly record daily transactions, organize them by category, and maintain local control over their expense data.

## Scope of the Project
This project is a Command Line Interface (CLI) application developed in Python. It provides an offline, file-based mechanism to record, categorize, view, and remove expenses. The system features modular input validation to prevent invalid entries and generates concise financial summaries without reliance on external databases or third-party APIs.

## Target Users
- Students and individuals who need a quick, distraction-free tool to monitor daily spending.
- Users looking for a local, terminal-first alternative to heavy mobile apps.
- Developers or terminal enthusiasts who prefer running quick utilities directly from their command line interface.

## High-Level Features
- **Transaction Management**: Interactive options to log new expenses and delete existing entries.
- **Input Validation**: Dynamic checks for positive transaction amounts, proper date formatting (`YYYY-MM-DD`), and non-empty category labels.
- **Financial Reports**: Built-in aggregations to compute total spend, category-wise breakdown, and identify the highest single transaction.
- **Persistent Data Storage**: Automatic read and write operations using a structured local `expenses.json` file.
