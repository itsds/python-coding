# P4: Parse and Clean CSV Data
import csv, io
import json

csv_data = """name,email,amount,date
Alice, alice@example.com, 150.50, 2024-01-15
Bob, bob@example.com, , 2024-01-16
, charlie@example.com, 200, 2024-01-17
Dave, dave@example.com, not_a_number, 2024-01-18
Eve, eve@example.com, 300.75, 2024-01-19

"""

def parse_and_clean(csv_data):
    with open("file.jsonl") as f:
        for line in f:
            if not line.strip():
                continue
            json.loads(line)
    with open("file.json") as f:
        dict = json.load(f)
        
    pass


valid, errors = parse_and_clean(csv_data)
print("Valid:", valid)
print("Errors:", errors)
# expected valid: Alice + Eve; errors for Bob (empty amount), row 4 (empty name), Dave (bad amount)
