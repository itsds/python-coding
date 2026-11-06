# P3: Group and Aggregate Sales
from collections import defaultdict

sales = [
    {"region": "APAC", "product": "Widget", "amount": 500},
    {"region": "EMEA", "product": "Gadget", "amount": 300},
    {"region": "APAC", "product": "Gizmo", "amount": 700},
    {"region": "APAC", "product": "Widget", "amount": 200},
    {"region": "EMEA", "product": "Widget", "amount": 450},
    {"region": "EMEA", "product": "Gadget", "amount": 150},
]

def summarize_sales(sales):
    result_dict = {}
    for sale in sales:
        region = sale["region"]
        amount = sale["amount"]
        product = sale["product"]
        if region not in result_dict:
            result_dict[region] = {"total_revenue":amount, "num_transactions": 1, "top_product": product, "current_max": amount}
        else:
            existing_dict=result_dict[region]
            if amount > existing_dict["current_max"]:

    pass


print(summarize_sales(sales))
# expected: {"APAC": {"total_revenue": 1400, "num_transactions": 3, "top_product": "Gizmo"}, "EMEA": {...}}
