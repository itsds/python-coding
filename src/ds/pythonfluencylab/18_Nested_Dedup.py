# P18: Flatten Nested Orders + Deduplicate Keeping Latest
orders = [
    {"order_id": "ORD001", "customer": "Alice",
     "items": [{"sku": "SKU100", "name": "Milk", "qty": 2, "price": 1.5},
               {"sku": "SKU101", "name": "Bread", "qty": 1, "price": 2.0}],
     "timestamp": "2026-10-20T10:30:00"},
    {"order_id": "ORD002", "customer": "Bob",
     "items": [{"sku": "SKU100", "name": "Milk", "qty": 3, "price": 1.5},
               {"sku": "SKU102", "name": "Eggs", "qty": 1, "price": 3.0}],
     "timestamp": "2026-10-20T11:00:00"},
    {"order_id": "ORD003", "customer": "Alice",
     "items": [{"sku": "SKU100", "name": "Milk", "qty": 5, "price": 1.4},
               {"sku": "SKU103", "name": "Butter", "qty": 1, "price": 4.0}],
     "timestamp": "2026-10-21T09:00:00"},
]

def flatten_and_deduplicate(orders):
    order_dict={}
    for order in orders:
        items=order["items"]
        for item in items:
            orders_dict = {}
            order_id = order["order_id"]
            customer = order["customer"]
            timestamp = order["timestamp"]
            sku=item["sku"]
            name=item["name"]
            qty=item["qty"]
            price=item["price"]
            orders_dict["sku"]=sku
            orders_dict["name"]=name
            orders_dict["qty"]=qty
            orders_dict["price"]=price
            orders_dict["order_id"] = order_id
            orders_dict["customer"] = customer
            orders_dict["timestamp"] = timestamp
            key=(customer,sku)
            if key not in order_dict:
                order_dict[key]=orders_dict
            elif key in order_dict and order_dict[key]["timestamp"]<timestamp:
                order_dict[key]=orders_dict

    return order_dict.values()

for row in flatten_and_deduplicate(orders):
    print(row)
# expected: 5 rows — Alice SKU100 from ORD001 replaced by ORD003 (newer)
