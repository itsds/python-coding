# P9: Build a Schema Validator
schema = {
    "name":  {"type": str, "required": True},
    "age":   {"type": int, "required": True},
    "email": {"type": str, "required": False},
    "score": {"type": float, "required": True},
}
records = [
    {"name": "Alice", "age": 30, "score": 95.5},
    {"name": "Bob", "age": "twenty", "email": "bob@x.com", "score": 88.0},
    {"name": "", "age": 25, "score": None},
]

def validate_records(records, schema):
    error_list=[]
    
    pass


print(validate_records(records, schema))
# expected: row 0 clean, row 1 age type error, row 2 empty name + None score
