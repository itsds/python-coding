def flatten_transactions(customers):
    result = []
    for customer in customers:
        name = customer["name"]
        for txn in customer.get("transactions") or []:
            result.append({
                "customer": name,
                **txn
            })
    return result

if __name__ == "__main__":
    customers = [
        {
            "name": "Alice",
            "transactions": [
                {"id": "T1", "amount": 150.0, "currency": "USD"},
                {"id": "T2", "amount": 89.50, "currency": "EUR"}
            ]
        },
        {
            "name": "Bob",
            "transactions": [
                {"id": "T3", "amount": 200.0, "currency": "USD"}
            ]
        },
        {
            "name": "DS",
            "transactions": [
                {"id": "T3", "amount": 200.0, "currency": "USD"}
            ]
        }
    ]
    result = flatten_transactions(customers)
    print(result)