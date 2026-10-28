transactions = [
    {"txn_id": "T1",  "customer": "Alice",   "amount": 500.0,  "status": "completed"},
    {"txn_id": "T2",  "customer": "Alice",   "amount": 150.0,  "status": "completed"},
    {"txn_id": "T3",  "customer": "Alice",   "amount": 80.0,   "status": "refunded"},
    {"txn_id": "T4",  "customer": "Bob",     "amount": 1200.0, "status": "completed"},
    {"txn_id": "T5",  "customer": "Charlie", "amount": 300.0,  "status": "completed"},
    {"txn_id": "T6",  "customer": "Charlie", "amount": 250.0,  "status": "completed"},
    {"txn_id": "T7",  "customer": "Charlie", "amount": 100.0,  "status": "completed"},
    {"txn_id": "T8",  "customer": "Diana",   "amount": 900.0,  "status": "completed"},
    {"txn_id": "T9",  "customer": "Diana",   "amount": 50.0,   "status": "refunded"},
    {"txn_id": "T10", "customer": "Diana",   "amount": 400.0,  "status": "completed"},
    {"txn_id": "T11", "customer": "Eve",     "amount": 2000.0, "status": "completed"},
    {"txn_id": "T12", "customer": "Frank",   "amount": 100.0,  "status": "completed"},
    {"txn_id": "T13", "customer": "Frank",   "amount": 120.0,  "status": "completed"},
    {"txn_id": "T14", "customer": "Frank",   "amount": 130.0,  "status": "refunded"},
]


def top_customers(transactions, n, min_txns):
    cust_txn_dict={}
    for txn in transactions:
        cust=txn["customer"]
        amount=txn["amount"]
        status=txn["status"]
        if cust not in cust_txn_dict and status=="completed":
            cust_dict={}
            cust_dict["customer"]=cust
            cust_dict["amount"] = amount
            cust_dict["count"] = 1
            cust_txn_dict[cust]=cust_dict

        elif cust in cust_txn_dict:
            if status == "completed":
                cust_txn_dict[cust]["amount"] += amount
                cust_txn_dict[cust]["count"] += 1

        dict_2=cust_txn_dict.values()
        details_list=[]
    for detail in dict_2:
        if detail["count"] >= min_txns:
            details_list.append((detail["customer"],detail["amount"],detail["count"]))
    details_list_sorted = sorted(details_list,key=lambda x : x[1], reverse=True)[:n]

    return details_list_sorted

print(top_customers(transactions, n=2, min_txns=2))