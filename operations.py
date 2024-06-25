import sqlite3

Class Variants:
    @staticmethod
    def display_all_purchases():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT sale_id, Salespeople.name, Customers.name, amount, date
            FROM Sales
            JOIN Salespeople ON Sales.salesperson_id = Salespeople.salesperson_id
            JOIN Customers ON Sales.customer_id = Customers.customer_id
        ''')
        rows = cursor.fetchall()
        conn.close()
        return rows
    @staticmethod

    def display_purchases_by_salesperson(salesperson_id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT sale_id, Salespeople.name, Customers.name, amount, date
            FROM Sales
            JOIN Salespeople ON Sales.salesperson_id = Salespeople.salesperson_id
            JOIN Customers ON Sales.customer_id = Customers.customer_id
            WHERE Sales.salesperson_id = ?
        ''', (salesperson_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    @staticmethod
    def display_largest_amount_of_sales():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MAX(amount) FROM Sales
        ''')
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_smallest_amount_of_sales():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MIN(amount) FROM Sales
        ''')
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_largest_amount_of_sales_for_salesperson(salesperson_id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MAX(amount) FROM Sales WHERE salesperson_id = ?
        ''', (salesperson_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_smallest_amount_of_sales_for_salesperson(salesperson_id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MIN(amount) FROM Sales WHERE salesperson_id = ?
        ''', (salesperson_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_largest_purchase_for_customer(customer_id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MAX(amount) FROM Sales WHERE customer_id = ?
        ''', (customer_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_smallest_purchase_for_customer(customer_id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT MIN(amount) FROM Sales WHERE customer_id = ?
        ''', (customer_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0]
    @staticmethod
    def display_salesperson_with_largest_amount_of_sales():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Salespeople.name, SUM(amount) as total_sales
            FROM Sales
            JOIN Salespeople ON Sales.salesperson_id = Salespeople.salesperson_id
            GROUP BY Sales.salesperson_id
            ORDER BY total_sales DESC
            LIMIT 1
        ''')
        result = cursor.fetchone()
        conn.close()
        return result
    @staticmethod
    def display_customer_with_largest_purchase():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Customers.name, SUM(amount) as total_purchase
            FROM Sales
            JOIN Customers ON Sales.customer_id = Customers.customer_id
            GROUP BY Sales.customer_id
            ORDER BY total_purchase DESC
            LIMIT 1
        ''')
        result = cursor.fetchone()
        conn.close()
        return result