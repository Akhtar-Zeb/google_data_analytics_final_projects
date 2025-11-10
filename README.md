# 🧾 Customer Sales Database Project

## Overview
This project demonstrates the complete workflow of **data cleaning**, **database design**, and **data loading automation** using both **Python** and **SQL**.  
It simulates a real-world system where a company manages customer information, product catalogs, and sales transactions.

---

## Project Steps

### Data Cleaning
- Raw data contained:
  - Extra spaces and no clear delimiters.
  - Inconsistent spacing.
  - Missing or invalid values such as `NILL`.
- Cleaned using:
  - **Python (Regex + CSV)**
  - **Excel Power Query**

**Key tasks performed:**
- Removed hidden spaces and blank lines.
- Split text correctly into columns.
- Merged extra columns.
- Sorted and removed duplicates.
- Logged invalid or skipped rows.
- Exported to `clean.csv`.

---

### 2️⃣ Database Setup
Created a relational database with **three tables**:
- `customers`  
- `products`  
- `transactions`

Each table was created with proper **primary keys** and **foreign key relationships**.

#### 🪶 SQLite Schema
```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    location TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    product_rate REAL
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    sale_month TEXT NOT NULL,
    sale_year TEXT NOT NULL,
    unit_sales INTEGER,
    product_rate REAL,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

