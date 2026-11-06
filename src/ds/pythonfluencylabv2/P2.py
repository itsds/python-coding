# P2: Deduplicate by Latest Timestamp
events = [
    {"event_id": "E1", "timestamp": "2024-03-15T10:00:00", "status": "pending"},
    {"event_id": "E2", "timestamp": "2024-03-15T09:00:00", "status": "done"},
    {"event_id": "E1", "timestamp": "2024-03-15T14:00:00", "status": "done"},
    {"event_id": "E3", "timestamp": "2024-03-15T08:00:00", "status": "pending"},
    {"event_id": "E2", "timestamp": "2024-03-15T12:00:00", "status": "failed"},
]

def dedup_latest(events):
    event_dict = {}
    for event in events:
        event_id = event["event_id"]
        if event_id not in event_dict:
            event_dict[event_id] = event
        else:
            current_ts = event["timestamp"]
            previous_ts = event_dict[event_id]["timestamp"]
            if previous_ts < current_ts:
                event_dict[event_id] = event

    return list(event_dict.values())


print(dedup_latest(events))
# expected: E1 at 14:00 (done), E2 at 12:00 (failed), E3 at 08:00 (pending)
