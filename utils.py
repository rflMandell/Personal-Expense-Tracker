import csv
from database import *

def export_to_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactnios")
    transactions = cursor.fetchall()
    conn.close()
    
    with open("statement.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Type", "Description", "Amount", "Date"])
        writer.writerows(transactions)