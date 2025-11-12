import csv
import sqlite3
import os

def main():

    input_file = input("Enter file name: ")

    file_name = os.path.basename(input_file)

    if file_name == "customers_clean.csv":
        add_customer(input_file)
    elif file_name == "products_clean.csv":
        add_product(input_file)
    elif file_name == "transactions_clean.csv":
        add_transaction(input_file)
    else:
        print("File not found or Unsupported format")


def add_customer(file):
    conn = sqlite3.connect("sales.db")
    cur = conn.cursor()

    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO customers(customer_id, customer_name, customer_location) VALUES(?, ?, ?);", row)

        
    conn.commit()
    print("✅ Data successfully inserted into SQLite!")

    cur.close()
    conn.close()

def add_product(file):
    conn = sqlite3.connect("sales.db")
    cur = conn.cursor()

    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO products(product_id, company_name, product_name, product_rate) VALUES (?, ?, ?, ?);", row)


    conn.commit()
    print("✅ Data successfully inserted into SQLite!")
    cur.close()
    conn.close()

def add_transaction(file):
    conn = sqlite3.connect("sales.db")
    cur = conn.cursor()

    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO transactions(customer_id, product_id, sale_month, sale_year, unit_sales, product_rate, total_amount) VALUES (?, ?, ?, ?, ?, ?, ?);", row[:8])


    conn.commit()
    print("✅ Data successfully inserted into SQLite!")
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()