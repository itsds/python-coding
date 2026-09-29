"""
GENERATOR PIPELINE PRACTICE EXERCISES
======================================

Instructions:
  1. Run setup_data.py FIRST to create sample data files.
  2. Complete each exercise by filling in the function body where it says:
         # YOUR CODE HERE
  3. Run validate.py to check your answers.
  4. Each exercise builds on concepts from the previous one.

Difficulty: [*] Easy  [**] Medium  [***] Hard

Tips:
  - A generator function uses 'yield' instead of 'return'.
  - 'yield' pauses the function and sends one value out.
  - The function resumes from where it paused on the next iteration.
  - Think of each stage as: receive item -> process -> yield result.
"""
import csv


# ============================================================
# EXERCISE 1: Basic Generator [*]
# ============================================================
# Write a generator that yields numbers from 1 to n.
#
# Example:
#   gen = count_up(5)
#   print(list(gen))  # [1, 2, 3, 4, 5]
#
# Hint: Use a loop and yield each number.
# ============================================================
def count_up(n):
    for i in range(n):
        yield i+1


# ============================================================
# EXERCISE 2: Read Lines Generator [*]
# ============================================================
# Write a generator that reads a file line by line,
# stripping the newline character from each line.
#
# Example:
#   for line in read_lines("data/users.csv"):
#       print(line)
#   # prints each line without trailing \n
#
# Hint: Use 'with open(filepath) as f' and yield
#       each line after stripping whitespace.
# ============================================================
def read_lines(filepath):
    with open(filepath,"r") as f:
        for line in f:
            yield line.strip()
    pass


# ============================================================
# EXERCISE 3: Skip Empty Lines Generator [*]
# ============================================================
# Write a generator that takes an iterable of lines
# and yields only non-empty lines (after stripping whitespace).
#
# Example:
#   lines = ["hello", "", "  ", "world", ""]
#   print(list(skip_empty(lines)))  # ["hello", "world"]
#
# Hint: Use strip() to check if a line is empty.
# ============================================================
def skip_empty(lines):
    for line in lines:
        if line.strip():
            yield line
    pass


# ============================================================
# EXERCISE 4: Parse CSV Generator [**]
# ============================================================
# Write a generator that takes an iterable of CSV lines
# and yields each line as a dictionary.
# The FIRST line is the header (column names).
# Each subsequent line becomes a dict with header keys.
#
# Example:
#   lines = ["name,age,city", "Alice,30,NYC", "Bob,25,LA"]
#   print(list(parse_csv(lines)))
#   # [{'name': 'Alice', 'age': '30', 'city': 'NYC'},
#   #  {'name': 'Bob', 'age': '25', 'city': 'LA'}]
#
# Hint:
#   - Use next() to grab the first line (header).
#   - Split the header by comma to get column names.
#   - For each remaining line, split by comma and zip
#     with the header to create a dict.
# ============================================================
def parse_csv(lines):

    header=next(lines)
    fields=header.split(",")
    for line in lines:
        if line.strip():
            values=line.split(",")
            yield dict(zip(fields,values))
    pass


# ============================================================
# EXERCISE 5: Filter by Field Generator [**]
# ============================================================
# Write a generator that takes an iterable of dicts
# and yields only those where dict[field] == value.
#
# Example:
#   records = [
#       {'name': 'Alice', 'status': 'active'},
#       {'name': 'Bob', 'status': 'inactive'},
#       {'name': 'Charlie', 'status': 'active'},
#   ]
#   print(list(filter_by(records, 'status', 'active')))
#   # [{'name': 'Alice', 'status': 'active'},
#   #  {'name': 'Charlie', 'status': 'active'}]
# ============================================================
def filter_by(records, field, value):
    for record in records:
        if record.get(field) == value:
            yield record

    pass


# ============================================================
# EXERCISE 6: Build the Full Pipeline [**]
# ============================================================
# Chain exercises 2-5 together to build a complete pipeline:
#   read_lines -> skip_empty -> parse_csv -> filter_by
#
# The function should:
#   1. Read lines from "data/users.csv"
#   2. Skip empty lines
#   3. Parse CSV into dicts
#   4. Filter where status == "active"
#   5. Return a LIST of the active user names (just the names)
#
# Expected output (list of names):
#   ['Alice', 'Charlie', 'Diana', 'Frank', 'Grace', 'Ivy', 'Jack']
#
# Hint: Chain generators like:
#   stage1 = read_lines(...)
#   stage2 = skip_empty(stage1)
#   stage3 = parse_csv(stage2)
#   stage4 = filter_by(stage3, ...)
#   Then extract names from stage4.
# ============================================================
def get_active_user_names():
    return_list=[]
    row_dict=filter_by(parse_csv(skip_empty((read_lines("data/users.csv")))), "status", "active")
    for r in row_dict:
        return_list.append(r['name'])

    return return_list


# ============================================================
# EXERCISE 7: Transform Generator [**]
# ============================================================
# Write a generator that takes an iterable of dicts (orders)
# and yields new dicts with only selected fields, plus a
# computed field.
#
# For each order dict, yield a new dict with:
#   - 'order_id': same as input
#   - 'product': same as input
#   - 'amount': converted to float
#   - 'amount_with_tax': amount * 1.08 (8% tax), rounded to 2 decimals
#
# Example:
#   orders = [{'order_id': '101', 'user_id': '1',
#              'product': 'Laptop', 'amount': '999.99',
#              'date': '2024-01-15'}]
#   print(list(transform_orders(orders)))
#   # [{'order_id': '101', 'product': 'Laptop',
#   #   'amount': 999.99, 'amount_with_tax': 1079.99}]
# ============================================================
def transform_orders(records):
    fields=('order_id','product','amount','amount_with_tax')
    for record in records:
        amount = float(record['amount'])
        value = (record['order_id'], record['product'], amount, round(amount * 1.08, 2))
        #value=(record['order_id'],record['product'],float(record['amount']),float(record['amount'])*1.08)
        yield dict(zip(fields,value))


# ============================================================
# EXERCISE 8: Orders Pipeline [***]
# ============================================================
# Build a full pipeline for orders data:
#   1. Read lines from "data/orders.csv"
#   2. Skip empty lines
#   3. Parse CSV into dicts
#   4. Transform orders (using transform_orders from Ex 7)
#   5. Return a list of all transformed orders
#
# Expected: A list of dicts, each with keys:
#   order_id, product, amount (float), amount_with_tax (float)
# ============================================================
def get_all_orders_with_tax():
    list_output=[]
    with open("data/orders.csv") as f:

        for row in f:
            if row.strip():
                list_output.append(row)

        return list_output


# ============================================================
# EXERCISE 9: Aggregation with Generators [***]
# ============================================================
# Using a generator pipeline on "data/orders.csv":
#   1. Read and parse the orders (reuse your pipeline stages)
#   2. Use sum() with a generator expression to calculate
#      the total amount of ALL orders (before tax).
#
# Hint: sum() can take a generator expression directly:
#       sum(expression for item in iterable)
#
# Expected output: 2189.89
# ============================================================
def total_order_amount():
    # YOUR CODE HERE
    pass


# ============================================================
# EXERCISE 10: Log Parser Pipeline [***]
# ============================================================
# Parse "data/server.log" to extract ERROR entries.
# Each log line looks like:
#   [2024-03-15 14:30:45] ERROR: Failed to connect to payment gateway
#
# Write these generators:
#
# a) parse_log_line(lines):
#    Takes lines, yields dicts with keys:
#      'timestamp', 'level', 'message'
#    - timestamp = text between [ and ]
#    - level = word before the colon (after ] )
#    - message = everything after "LEVEL: "
#
# b) filter_errors(records):
#    Takes parsed log dicts, yields only those
#    where level == "ERROR"
#
# c) get_error_messages():
#    Chains: read_lines -> skip_empty -> parse_log_line
#            -> filter_errors
#    Returns a LIST of error message strings (just the messages).
# ============================================================
def parse_log_line(lines):
    # YOUR CODE HERE
    pass


def filter_errors(records):
    # YOUR CODE HERE
    pass


def get_error_messages():
    # YOUR CODE HERE
    pass


# ============================================================
# EXERCISE 11: yield from [**]
# ============================================================
# Write a generator that reads MULTIPLE CSV files and
# yields all parsed records from all files combined.
# Use 'yield from' to delegate to your parse pipeline.
#
# It should:
#   1. For each filepath in the list:
#      - read_lines -> skip_empty -> parse_csv
#      - yield from that pipeline
#   2. The caller gets a single flat stream of dicts
#      from all files.
#
# Example:
#   files = ["data/users.csv", "data/orders.csv"]
#   for record in read_multiple_csv(files):
#       print(record)  # dicts from users, then dicts from orders
# ============================================================
def read_multiple_csv(filepaths):
    # YOUR CODE HERE
    pass


# ============================================================
# EXERCISE 12: Generator vs List Comparison [*]
# ============================================================
# This exercise demonstrates WHY generators matter.
# Read "data/numbers.txt" (10,000 numbers, one per line).
#
# a) sum_with_list():
#    - Read ALL lines into a list
#    - Convert each to int
#    - Return the sum
#    (This loads everything into memory at once)
#
# b) sum_with_generator():
#    - Use a generator pipeline (read_lines -> convert to int)
#    - Use sum() with the generator
#    - Return the sum
#    (This processes one number at a time)
#
# Both should return the SAME number.
# The difference is memory usage (not visible here,
# but critical with millions of rows).
# ============================================================
def sum_with_list():
    # YOUR CODE HERE
    pass


def sum_with_generator():
    # YOUR CODE HERE
    pass


# ============================================================
# BONUS EXERCISE 13: Category Summary Pipeline [***]
# ============================================================
# Read "data/products.csv" and produce a summary dict
# where keys are categories and values are dicts with:
#   - 'count': number of products in that category
#   - 'total_value': sum of (price * stock) for that category
#   - 'avg_price': average price in that category (rounded to 2)
#
# Use generator pipeline stages for reading and parsing,
# then aggregate into the summary dict.
#
# Expected output (approximately):
# {
#   'Electronics': {'count': 5, 'total_value': ..., 'avg_price': ...},
#   'Stationery': {'count': 4, 'total_value': ..., 'avg_price': ...},
#   'Furniture': {'count': 3, 'total_value': ..., 'avg_price': ...},
# }
# ============================================================
def category_summary():
    # YOUR CODE HERE
    pass


# ============================================================
# Quick test area - uncomment to test individual exercises
# ============================================================
if __name__ == "__main__":
    # --- Exercise 1 ---
    print("Ex 1:", list(count_up(5)))

    # --- Exercise 2 ---
    for line in read_lines("data/users.csv"):
         print(line)

    # --- Exercise 3 ---
    lines = read_lines("data/users.csv")
    for line in skip_empty(lines):
        print(repr(line))

    # --- Exercise 4 ---
    lines = skip_empty(read_lines("data/users.csv"))
    for record in parse_csv(lines):
        print(record)

    # --- Exercise 5 ---
    pipeline = parse_csv(skip_empty(read_lines("data/users.csv")))
    for user in filter_by(pipeline, 'status', 'active'):
        print(user['name'])

    # --- Exercise 6 ---
    print("Ex 6:", get_active_user_names())

    # --- Exercise 7 ---
    pipeline = parse_csv(skip_empty(read_lines("data/orders.csv")))
    for order in transform_orders(pipeline):
        print(order)

    # --- Exercise 8 ---
    print("Ex 8:", get_all_orders_with_tax())

    # --- Exercise 9 ---
    # print("Ex 9:", total_order_amount())

    # --- Exercise 10 ---
    # print("Ex 10:", get_error_messages())

    # --- Exercise 11 ---
    # for rec in read_multiple_csv(["data/users.csv", "data/orders.csv"]):
    #     print(rec)

    # --- Exercise 12 ---
    # print("Ex 12 (list):", sum_with_list())
    # print("Ex 12 (gen):", sum_with_generator())

    # --- Exercise 13 ---
    # print("Ex 13:", category_summary())

    #print("Uncomment the exercises above to test them one by one!")
