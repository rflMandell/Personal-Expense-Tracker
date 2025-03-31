from database import *
from datetime import datetime

def add_transaction(type, description, amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, description, amount, date) VALUES (?, ?, ?, ?)", 
                   (type, description, amount, date))
    conn.commit()
    conn.close()
    
def list_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transaction = cursor.fetchall()
    conn.close()
    return transaction

def calculate_balance():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    incomes = cursor.fetchone()[0] or 0
    cursor.execute("DELECT SUM(amount) FROM transactions WHERE type='expense'")
    expenses = cursor.fetchone()[0] or 0
    conn.close()
    return incomes - expenses

def filter_transactions_by_period(start, end):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE date BETWEEN ? and ?", (start, end))
    transaction = cursor.fetchall()
    conn.close()
    return transaction