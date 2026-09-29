


data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Bengaluru",
            "zip": "560001"
        },
        "scores": [85, 92, 78]
    },
    "active": True
}
"""
Expected Output:
{
    "user.name": "Alice",
    "user.address.city": "Bengaluru",
    "user.address.zip": "560001",
    "user.scores": [85, 92, 78],
    "active": True
}
"""


def flatten_jsonn(data,separator=".",prefix="" ):
    result_dict = {}

    for key, value in data.items():
        full_key = f"{prefix}{separator}{key}" if prefix else key
        if isinstance(value,dict):
            result_dict.update(flatten_jsonn(value, separator, full_key))
        else:
            result_dict[full_key] = value

    return result_dict


print(flatten_jsonn(data,'.',""))