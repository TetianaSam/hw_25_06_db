import sqlite3




conn = sqlite3.connect("task3_sales_db.db")

cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS Salespeople (
            salesperson_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL)""")


cursor.execute("""CREATE TABLE IF NOT EXISTS Sales (
            sale_id INTEGER PRIMARY KEY,
            salesperson_id INTEGER,
            customer_id INTEGER,
            amount REAL,
            date TEXT,
            FOREIGN KEY (salesperson_id) REFERENCES Salespeople (salesperson_id),
            FOREIGN KEY (customer_id) REFERENCES Customers (customer_id))""")

# Insert sample data into Salespeople
cursor.execute("INSERT INTO Salespeople (name) VALUES ('Alice')")
cursor.execute("INSERT INTO Salespeople (name) VALUES ('Bob')")
cursor.execute("INSERT INTO Salespeople (name) VALUES ('Charlie')")

# Insert sample data into Customers
cursor.execute("INSERT INTO Customers (name) VALUES ('Customer A')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Customer B')")
cursor.execute("INSERT INTO Customers (name) VALUES ('Customer C')")

# Insert sample data into Sales
cursor.execute("INSERT INTO Sales (salesperson_id, customer_id, amount, date) VALUES (1, 1, 100.0, '2024-01-01')")
cursor.execute("INSERT INTO Sales (salesperson_id, customer_id, amount, date) VALUES (1, 2, 200.0, '2024-01-02')")
cursor.execute("INSERT INTO Sales (salesperson_id, customer_id, amount, date) VALUES (2, 1, 150.0, '2024-01-03')")
cursor.execute("INSERT INTO Sales (salesperson_id, customer_id, amount, date) VALUES (3, 3, 300.0, '2024-01-04')")
cursor.execute("INSERT INTO Sales (salesperson_id, customer_id, amount, date) VALUES (2, 3, 50.0, '2024-01-05')")

# Commit changes and close connection
conn.commit()
conn.close()



