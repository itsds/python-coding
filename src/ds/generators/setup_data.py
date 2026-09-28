"""
SETUP SCRIPT - Run this FIRST to create sample data files.
Usage: python setup_data.py
"""
import os
import random


def create_data_directory():
    os.makedirs("data", exist_ok=True)
    print("Created 'data/' directory.")


def create_users_csv():
    """Creates data/users.csv with mixed data (some empty lines, some inactive)."""
    header = "id,name,email,status,age"
    rows = [
        "1,Alice,alice@example.com,active,30",
        "2,Bob,bob@example.com,inactive,25",
        "",                                        # empty line
        "3,Charlie,charlie@example.com,active,35",
        "4,Diana,diana@example.com,active,28",
        "   ",                                     # whitespace-only line
        "5,Eve,eve@example.com,inactive,22",
        "6,Frank,frank@example.com,active,40",
        "7,Grace,grace@example.com,active,33",
        "",                                        # empty line
        "8,Hank,hank@example.com,inactive,29",
        "9,Ivy,ivy@example.com,active,26",
        "10,Jack,jack@example.com,active,45",
    ]
    with open("data/users.csv", "w") as f:
        f.write(header + "\n")
        for row in rows:
            f.write(row + "\n")
    print("Created data/users.csv (10 users, some empty lines)")


def create_orders_csv():
    """Creates data/orders.csv with order records."""
    header = "order_id,user_id,product,amount,date"
    rows = [
        "101,1,Laptop,999.99,2024-01-15",
        "102,3,Mouse,29.99,2024-01-16",
        "",
        "103,1,Keyboard,79.99,2024-02-01",
        "104,4,Monitor,349.99,2024-02-10",
        "105,6,Headphones,149.99,2024-02-15",
        "   ",
        "106,7,Webcam,89.99,2024-03-01",
        "107,9,USB Hub,24.99,2024-03-05",
        "108,10,Desk Lamp,44.99,2024-03-10",
        "109,3,Chair,299.99,2024-03-15",
        "",
        "110,1,SSD,119.99,2024-03-20",
    ]
    with open("data/orders.csv", "w") as f:
        f.write(header + "\n")
        for row in rows:
            f.write(row + "\n")
    print("Created data/orders.csv (10 orders, some empty lines)")


def create_server_log():
    """Creates data/server.log with mixed log entries."""
    levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = {
        "INFO": [
            "User login successful",
            "Page loaded in 230ms",
            "Cache refreshed",
            "Session started for user_id=42",
            "Database connection pool: 5/10 active",
        ],
        "WARNING": [
            "Slow query detected: 2300ms",
            "Memory usage at 85%",
            "Rate limit approaching for IP 192.168.1.100",
        ],
        "ERROR": [
            "Failed to connect to payment gateway",
            "NullPointerException in OrderService.process()",
            "Timeout waiting for response from API",
            "Disk space critically low: 2% remaining",
        ],
        "DEBUG": [
            "Request headers: {'Accept': 'application/json'}",
            "Query plan: sequential scan on users table",
            "Garbage collection completed in 45ms",
        ],
    }

    lines = []
    for i in range(50):
        level = random.choice(levels)
        msg = random.choice(messages[level])
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        timestamp = f"2024-03-{random.randint(1,31):02d} {hour:02d}:{minute:02d}:{second:02d}"
        lines.append(f"[{timestamp}] {level}: {msg}")
        # Sprinkle some empty lines
        if random.random() < 0.1:
            lines.append("")

    with open("data/server.log", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Created data/server.log (50 log entries)")


def create_products_csv():
    """Creates data/products.csv for a bonus exercise."""
    header = "product_id,name,category,price,stock"
    rows = [
        "P001,Laptop,Electronics,999.99,50",
        "P002,Mouse,Electronics,29.99,200",
        "P003,Notebook,Stationery,4.99,500",
        "",
        "P004,Pen,Stationery,1.99,1000",
        "P005,Monitor,Electronics,349.99,30",
        "P006,Eraser,Stationery,0.99,800",
        "P007,Headphones,Electronics,149.99,75",
        "   ",
        "P008,Stapler,Stationery,8.99,150",
        "P009,Webcam,Electronics,89.99,60",
        "P010,Desk Lamp,Furniture,44.99,90",
        "P011,Chair,Furniture,299.99,25",
        "P012,Desk,Furniture,449.99,15",
    ]
    with open("data/products.csv", "w") as f:
        f.write(header + "\n")
        for row in rows:
            f.write(row + "\n")
    print("Created data/products.csv (12 products, some empty lines)")


def create_large_numbers_file():
    """Creates data/numbers.txt - one number per line (for generator vs list exercise)."""
    with open("data/numbers.txt", "w") as f:
        for _ in range(10000):
            f.write(f"{random.randint(1, 1000)}\n")
    print("Created data/numbers.txt (10,000 numbers)")


if __name__ == "__main__":
    print("=" * 50)
    print("  GENERATOR PRACTICE KIT - DATA SETUP")
    print("=" * 50)
    print()

    random.seed(42)  # Fixed seed for reproducible data

    create_data_directory()
    create_users_csv()
    create_orders_csv()
    create_server_log()
    create_products_csv()
    create_large_numbers_file()

    print()
    print("All data files created successfully!")
    print("Now open exercises.py and start coding.")
    print("Run validate.py when you want to check your answers.")
