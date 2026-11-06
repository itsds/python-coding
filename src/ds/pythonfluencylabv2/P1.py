# P1: Flatten Nested Transactions
customers = [
    {"name": "Alice", "transactions": [{"id": "T1", "amount": 150.0, "currency": "USD"}, {"id": "T2", "amount": 89.50, "currency": "EUR"}]},
    {"name": "Bob", "transactions": [{"id": "T3", "amount": 200.0, "currency": "USD"}]}
]

def flatten_transactions(customers):
    list_of_dict=[]

    for customer in customers:
        cust_map={}
        name=customer["name"]

        for txn in customer["transactions"]:
            cust_map={"customer":name, **txn}
            list_of_dict.append(cust_map)
            cust_map = {}

    return list_of_dict

print(flatten_transactions(customers))
# expected: [{"customer": "Alice", "id": "T1", ...}, ...]
