import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize the file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

# Add new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for idx, row in enumerate(reader, start=1):
            print(f"{idx}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")

# Calculate total for a specific category
def total_by_category():
    category = input("Enter category to get total: ").strip().lower()
    total = 0.0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1].strip().lower() == category:
                total += float(row[2])
    print(f"💰 Total expenses in '{category}' category: {total}")

# Delete an expense by entry number
def delete_expense():
    view_expenses()
    entry_no = int(input("Enter entry number to delete: "))
    with open(FILENAME, mode='r') as file:
        reader = list(csv.reader(file))
    header = reader[0]
    rows = reader[1:]
    if 1 <= entry_no <= len(rows):
        deleted = rows.pop(entry_no - 1)
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"🗑️ Deleted entry: {deleted}")
    else:
        print("❌ Invalid entry number!")

# Main menu
def main():
    initialize_file()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
