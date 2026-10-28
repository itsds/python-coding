# Q3: Dedupe events + running total per user
events = [
    {"user_id": 1, "event_time": "2024-01-01T10:00:00", "value": 100},
    {"user_id": 1, "event_time": "2024-01-01T10:00:00", "value": 100},
    {"user_id": 1, "event_time": "2024-01-01T10:01:00", "value": 200},
    {"user_id": 2, "event_time": "2024-01-01T10:00:00", "value": 50},
]

def running_totals(events):
    result_dict={}
    for event in events:
        user_dict={}
        user_id=event["user_id"]
        event_time=event["event_time"]
        value=event["value"]
        user_dict["user_id"]= user_id
        user_dict["event_time"] =event_time
        user_dict["value"] = value

        key=(user_id,event_time)

        if key not in result_dict:
            total_keys = result_dict.keys()
            for indikey in total_keys:
                if user_id in indikey:
                    current_running_total=result_dict[indikey]
                    user_dict["running_total"]=value+current_running_total
            result_dict[key]=user_dict
    return result_dict


print(running_totals(events))
# expected:
# [
# {'user_id': 1, 'event_time': '2024-01-01T10:00:00', 'value': 100, 'running_total': 100},
# {'user_id': 2, 'event_time': '2024-01-01T10:00:00', 'value': 50, 'running_total': 50},
# {'user_id': 1, 'event_time': '2024-01-01T10:01:00', 'value': 200, 'running_total': 300}
# ]
