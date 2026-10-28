import random


def event_stream(start_id=1):
    event_types = ["click", "view", "purchase", "scroll", "logout"]
    current_id = start_id
    while True:
        yield {
            "id": current_id,
            "type": random.choice(event_types),
            "ts": f"2024-03-15T{10 + current_id // 3600:02d}:"
                  f"{(current_id % 3600) // 60:02d}:"
                  f"{current_id % 60:02d}",
        }
        current_id += 1
def take_n(stream, n):
    pass

def take_until(stream, predicate):
    pass

def sample_every(stream, k):
    pass

