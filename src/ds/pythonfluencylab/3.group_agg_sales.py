from collections import defaultdict

sales = [
    {"region": "APAC", "product": "Widget",  "amount": 500},
    {"region": "EMEA", "product": "Gadget",  "amount": 300},
    {"region": "APAC", "product": "Gizmo",   "amount": 700},
    {"region": "APAC", "product": "Widget",  "amount": 200},
    {"region": "EMEA", "product": "Widget",  "amount": 450},
    {"region": "EMEA", "product": "Gadget",  "amount": 150},
]

def agg_sales(sales):
    result_dict = defaultdict(lambda: {"total_revenue": 0, "num_transactions": 0})

    for dict_obj in sales:
        region=dict_obj["region"]
        existing_dict=result_dict[region]
        existing_dict["total_revenue"] +=dict_obj["amount"]
        existing_dict["num_transactions"] +=1

    return result_dict

result_dict= agg_sales(sales)
print(result_dict)