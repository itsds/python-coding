# P17: Top N Customers by Spend per Category
from collections import defaultdict

transactions = [
    {"txn_id": "T1",  "customer": "Alice",   "category": "Grocery",     "amount": 120.5},
    {"txn_id": "T2",  "customer": "Bob",     "category": "Grocery",     "amount": 200.0},
    {"txn_id": "T3",  "customer": "Alice",   "category": "Grocery",     "amount": 80.0},
    {"txn_id": "T4",  "customer": "Charlie", "category": "Electronics", "amount": 450.0},
    {"txn_id": "T5",  "customer": "Bob",     "category": "Electronics", "amount": 300.0},
    {"txn_id": "T6",  "customer": "Alice",   "category": "Electronics", "amount": 600.0},
    {"txn_id": "T7",  "customer": "Diana",   "category": "Grocery",     "amount": 350.0},
    {"txn_id": "T8",  "customer": "Charlie", "category": "Grocery",     "amount": 90.0},
    {"txn_id": "T9",  "customer": "Diana",   "category": "Electronics", "amount": 150.0},
    {"txn_id": "T10", "customer": "Bob",     "category": "Grocery",     "amount": 175.0},
]

def top_customers_by_category(transactions, n):
    category_customer_dict = {}
    result_dict = {}

    for txn in transactions:
        category = txn["category"]
        customer = txn["customer"]
        amount = txn["amount"]

        if category not in category_customer_dict:
            category_customer_dict[category]={customer:amount}

        else:
            category_customer_dict[category][customer] = category_customer_dict[category].get(customer,0)+amount

    for category,category_customer in category_customer_dict.items():
        sorted_value = sorted(category_customer.items(), key= lambda x : x[1], reverse=True)[:n]
        result_dict[category]=sorted_value

    return result_dict


print(top_customers_by_category(transactions, 2))
# expected: {"Grocery": [("Bob", 375.0), ("Diana", 350.0)], "Electronics": [("Alice", 600.0), ("Charlie", 450.0)]}
