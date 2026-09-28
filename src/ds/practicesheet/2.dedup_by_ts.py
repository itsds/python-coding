

def dedup(events):

    result_dict={}
    for event in events:
        event_id=event["event_id"]

        if event_id not in result_dict:
            result_dict[event_id] = event
        else :
            value_dict = result_dict.get(event_id)
            existing_ts = value_dict["timestamp"]
            current_ts=event["timestamp"]
            if current_ts > existing_ts:
                result_dict[event_id] = event

    return list(result_dict.values())

events = [
    {"event_id": "E1", "timestamp": "2024-03-15T10:00:00", "status": "pending"},
    {"event_id": "E2", "timestamp": "2024-03-15T09:00:00", "status": "done"},
    {"event_id": "E1", "timestamp": "2024-03-15T14:00:00", "status": "done"},
    {"event_id": "E3", "timestamp": "2024-03-15T08:00:00", "status": "pending"},
    {"event_id": "E2", "timestamp": "2024-03-15T12:00:00", "status": "failed"},
]

"""
Expected Output (order doesn't matter):
[
    {"event_id": "E1", "timestamp": "2024-03-15T14:00:00", "status": "done"},
    {"event_id": "E2", "timestamp": "2024-03-15T12:00:00", "status": "failed"},
    {"event_id": "E3", "timestamp": "2024-03-15T08:00:00", "status": "pending"}
]
"""

result=dedup(events)
print(result)