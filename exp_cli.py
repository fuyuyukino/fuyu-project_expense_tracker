# Expense Tracker CLI
import argparse
import json
import os
from datetime import datetime

# Define the path to the JSON file
DATA_FILE = 'expenses.json'

# Load JSON data from the file
def load_data():
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


# Save JSON data to the file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


# Add a new expense to the JSON file
def add_expense(description, amount):
    data = load_data()
    expense_id = len(data) + 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "description": description,
        "amount": amount
    }
    data.append(expense)
    save_data(data)
    print(f"Expense added successfully (ID: {expense_id})")


# List all expenses from the JSON file
def list_expenses():
    pass


# Show summary of expenses for a all months or a specific month
def show_summary(month=None):
    pass


# Delete an expense by ID from the JSON file
def delete_expense(expense_id):
    pass


# Main function to handle command-line arguments and perform actions
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Setup 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument("--description", type=str, required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

    # Setup 'list' command
    subparsers.add_parser('list', help='List all expenses')

    # Setup "summary" command
    summary_parser = subparsers.add_parser('summary', help='Show summary of all expenses')
    summary_parser.add_argument("--month", type=int, help="Start date in 1 - 12 format")

    # Setup "delete" command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense by ID')
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == 'add':
        add_expense(args.description, args.amount)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'summary':
        show_summary(args.month)
    elif args.command == 'delete':
        delete_expense(args.id)

# Entry point of the script
if __name__ == "__main__":
    main()