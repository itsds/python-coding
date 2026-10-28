# Q2: Total transaction value per customer (huge file)
# transactions.jsonl, one JSON object per line:
# {"customer_id": "c1", "amount": 120.5}
# {"customer_id": "c2", "amount": 40}
# {"customer_id": "c1", "amount": 50}
import json
from json import loads, load

path = "transactions.jsonl"

def total_per_customer(path):
    result_dict={}
    with open(path) as f:
        for line in f:
            new_line=line.strip()
            if not line:
                continue
            customer = json.loads(line)
            if customer['customer_id'] not in result_dict:
                result_dict[customer['customer_id']]=customer['amount']
            else:
                result_dict[customer['customer_id']] +=customer['amount']


    return result_dict


print(total_per_customer(path))
# expected: {'c1': 170.5, 'c2': 40}
