from pandas import value_counts

events = [
   {"user_id": 1, "event_time": "2024-01-01T10:00:00", "value": 100},
   {"user_id": 1, "event_time": "2024-01-01T10:00:00", "value": 100},
   {"user_id": 1, "event_time": "2024-01-01T10:01:00", "value": 200},
   {"user_id": 2, "event_time": "2024-01-01T10:00:00", "value": 50},
]

# [
#    {"user_id": 1, "event_time": "2024-01-01T10:00:00", "value": 100, "running_total": 100},
#    {"user_id": 2, "event_time": "2024-01-01T10:00:00", "value": 50, "running_total": 50},
#    {"user_id": 1, "event_time": "2024-01-01T10:01:00", "value": 200, "running_total": 300},
# ]


def dedup_events(events):
    result_list= []
    result_dict={}
    result_dict_2 = {}


    for i in range(len(events)):
        event_dict = events[i]
        user_id_2=event_dict["user_id"]
        event_time_2=event_dict["event_time"]
        value_2=event_dict["value"]

        concat_key=str(user_id_2)+"_"+str(event_time_2)+"_"+str(value_2)

        result_dict[concat_key]=events[i]

    for key in result_dict:
        row = key.split("_")
        result_dict_2["user_id"]=row[0]
        result_dict_2["event_time"] = row[1]
        result_dict_2["value"] = row[2]
        result_list.append(result_dict_2)

    return result_list

result = dedup_events(events)
print(result)
