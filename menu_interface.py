from operations import Variants
import sqlite3


conn = sqlite3.connect("task3_sales_db.db")

cursor = conn.cursor()
def display_menu():
    print("""
    _____________MENU_____________
    [1] - All purchases;
    [2] - All purchases from a specific salesperson;
    [3] - The largest amount of sales;
    [4] - The smallest amount of sales;
    [5] - The greatest amount of sales for a specific salesperson;
    [6] -The smallest amount of sales for a specific salesperson;
    [7] - The largest amount of purchase for a specific customer;
    [8] - The smallest amount of purchase for a specific customer;
    [9] - The salesperson who has the largest amount of sales;
    [10] - The customer who has the largest amount of purchase;       
    [0] - Finish
    """)

def user_input():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))

            if choice == '1':
                purchases = display_all_purchases()
                for purchase in purchases:
                    print(purchase)
            elif choice == '2':
                salesperson_id = int(input("Enter salesperson ID: "))
                purchases = display_purchases_by_salesperson(salesperson_id)
                for purchase in purchases:
                    print(purchase)
            elif choice == '3':
                print("Largest amount of sales:", display_largest_amount_of_sales())
            elif choice == '4':
                print("Smallest amount of sales:", display_smallest_amount_of_sales())
            elif choice == '5':
                salesperson_id = int(input("Enter salesperson ID: "))
                print("Largest amount of sales for salesperson:",
                      display_largest_amount_of_sales_for_salesperson(salesperson_id))
            elif choice == '6':
                salesperson_id = int(input("Enter salesperson ID: "))
                print("Smallest amount of sales for salesperson:",
                      display_smallest_amount_of_sales_for_salesperson(salesperson_id))
            elif choice == '7':
                customer_id = int(input("Enter customer ID: "))
                print("Largest amount of purchase for customer:", display_largest_purchase_for_customer(customer_id))
            elif choice == '8':
                customer_id = int(input("Enter customer ID: "))
                print("Smallest amount of purchase for customer:", display_smallest_purchase_for_customer(customer_id))
            elif choice == '9':
                result = Variants.display_salesperson_with_largest_amount_of_sales()
                print(f"Salesperson with largest amount of sales: {result[0]} with total sales {result[1]}")
            elif choice == '10':
                result = Variants.display_customer_with_largest_purchase()
                print(f"Customer with largest amount of purchase: {result[0]} with total purchases {result[1]}")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
            break




user_input()
