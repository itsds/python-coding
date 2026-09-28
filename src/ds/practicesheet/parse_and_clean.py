

csv_data = """name,email,amount,date
Alice, alice@example.com, 150.50, 2024-01-15
Bob, bob@example.com, , 2024-01-16
, charlie@example.com, 200, 2024-01-17
Dave, dave@example.com, not_a_number, 2024-01-18
Eve, eve@example.com, 300.75, 2024-01-19

"""


def parse_clean_data(csv_data):
    str_arr=csv_data.split("\n")
    header=str_arr[0].trim()

    for line in str_arr:
        fields=line.split(",")



result_dict=parse_clean_data(csv_data)