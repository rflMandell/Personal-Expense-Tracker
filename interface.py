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
        
        if option == "1"
            description = input("Income descriptions: ")
            amount = float(input("Amount: "))
            add_transaction("income", description, amount)