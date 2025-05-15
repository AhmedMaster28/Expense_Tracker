# Expense_Tracker
It's a uni lab task 

# 💸 Simple Expense Tracker

This is a simple command-line based Expense Tracker written in Python. It helps you manage your personal expenses by allowing you to:

- Add new expense entries
- View all recorded expenses
- Get the total expenses for a specific category
- Delete an expense entry by its number
- Exit the program

## 🛠 Features

1. **Add Expense**  
   Add a new expense with the following details:
   - Date (optional — defaults to today)
   - Category (e.g., Food, Travel, Shopping)
   - Amount
   - Description

2. **View Expenses**  
   View a numbered list of all the expenses recorded in the system.

3. **Total by Category**  
   View the total amount spent in a specific category.

4. **Delete Expense**  
   Delete an expense from the record by selecting its number from the list.

5. **Persistent Storage**  
   All expenses are stored in a `CSV` file (`expenses.csv`) for persistence across sessions.

## 📂 File Structure

- `expense_tracker.py` - Main Python script that runs the tracker
- `expenses.csv` - CSV file where expenses are saved (auto-created)
- `README.md` - This documentation file

## ▶️ How to Run

Make sure you have Python 3 installed. Then run:

```bash
python expense.py
