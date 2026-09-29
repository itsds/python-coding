import json

def parse_and_stream(filepath):
    count=0
    result_list= []
    with open(filepath,"r") as f:
        data = json.load(f)
        for record in data :
            count +=1
            result_list.append(record)
            if count == 2:
                count=0
                yield result_list
                result_list=[]

        if result_list:
            yield result_list


count = 0
for batch in parse_and_stream("data/events.json"):
    count += 1
    print(f"Batch {count}: {batch}")

