"""
Pipeline:
1. filter_quality  → drop records where quality != "good"
2. convert_units   → convert Celsius to Fahrenheit (value * 9/5 + 32)
3. group_by_sensor → yield (sensor_id, [values]) when sensor changes or stream ends

Expected final output (after consuming all stages):
{
    "temp_1": {"count": 2, "avg": 72.77},
    "hum_1":  {"count": 2, "avg": 47.6},
    "temp_2": {"count": 2, "avg": 63.38}
}
# Note: humidity values pass through convert_units unchanged (only unit="C" converts)
"""

import json
from collections import defaultdict


def pipeline_filter(param):
    with open(param,"r") as f:
        data= json.load(f)
        for record in data:
            if record.get("quality") == 'good':
                yield record


def convert_units(records):

    for record in records:
        if record["unit"] == "C":
            record["value"]=(record["value"]*9/5+32)
            record["unit"]="F"
        yield record


def aggregate_by_sensor(records):
    result_dict =defaultdict(list)
    result_dict_2={}

    for record in records :
        sensor= record['sensor']
        value=record['value']
        result_dict[sensor].append(value)

    for keys in result_dict:
        count=len(result_dict.get(keys))
        total=sum(result_dict.get(keys))
        avg=round(total/count,2)

        result_dict_2[keys] = {
            "count": count,
            "avg": avg
        }

    return  result_dict_2


outp = aggregate_by_sensor(convert_units(pipeline_filter("data/reading.json")))
print(outp)