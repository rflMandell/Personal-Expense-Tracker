from models import *
filter_transactions_by_period
from utils import *

def menu():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. List Transactions")
        print("4. View Current Balance")
        print("5. Filter by Period")
        print("6. Export to CSV")
        print("7. Exit")
        option = input("Choose an option: ")
        
        if option == "1":
            description = input("Income description: ")
            amount = float(input("Amount: "))
            add_transaction("income", description, amount)
        elif option == "2":
            description = input("Expense description: ")
            amount = float(input("Amount: "))
            add_transaction("expense", description, amount)
        elif option == "3":
            transactions = list_transactions()
            for t in transactions:
                print(f"[{t[0]}] {t[4]} - {t[1].capitalize()} - {t[2]}: $ {t[3]:.2f}")
        elif option == "4":
            print(f"Current balance: $ {calculate_balance():.2f}\n")
        elif option == "5":
            start = input("Start date (YYYY-MM-DD HH:MM:SS): ")
            end = input("End date (YYYY-MM-DD HH:MM:SS): ")
            transactions = filter_transactions_by_period(start, end)
            for t in transactions:
                print(f"[{t[0]}] {t[4]} - {t[1].capitalize()} - {t[2]}: $ {t[3]:.2f}")
        elif option == "6":
            export_to_csv()
            print("Statement successfully exported!\n")
        elif option == "7":
            print("Exiting the system...")
            break
        else:
            print("Invalid option. Please try again.\n")