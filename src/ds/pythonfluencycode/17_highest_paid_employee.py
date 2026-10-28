# Q17: Highest-paid employee per department
rows = [
    {"name": "Asha", "dept": "HR", "salary": 50},
    {"name": "Meena", "dept": "HR", "salary": 40},
    {"name": "Ravi", "dept": "IT", "salary": 90},
    {"name": "Tom", "dept": "IT", "salary": 70},
]

def top_earner(rows):
    result_dict = {}

    for row in rows:
        dept = row["dept"]
        name = row["name"]
        salary = row["salary"]
        if dept not in result_dict:

            result_dict[dept] = {"name": name, "salary": salary}
        else:
            current_sal = result_dict[dept]["salary"]
            if salary > current_sal:
                result_dict[dept]["name"] = name
                result_dict[dept]["salary"] = salary


    return {dept:row["name"] for dept,row in result_dict.items()}

    # for key in result_dict:
    #     name = result_dict[key]["name"]
    #     result_list.append({key: name})
    # return result_list


print(top_earner(rows))
# expected: {'HR': 'Asha', 'IT': 'Ravi'}

#=====================================================
# RECENT Learnings in Python Coding
# Dict Comprehension
# dict.get("",0)
# Tuple for duplicacy
# Lambda function
# sort() and sorted()
# dict.items() , dict.keys(), dict.values()
# list(dict.values()) instead of simply returning dict.value()
# Direct dict initialization using {key : value}
# enumerate : "Python enumerate and zip - Claude" https://claude.ai/chat/4fb2c192-b003-4e26-91f1-527faf1e524a

