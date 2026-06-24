import json
from data_8_3 import json_data
from datetime import datetime

def parse_dates(object):
    datetime_fields = ["generatedAt", "updateTime", "startTime", "endTime"]
    for key, val in object.items():
        if key in datetime_fields:
            object[key] = datetime.fromisoformat(val)
    return object

data = json.loads(json_data, object_hook=parse_dates)
print(data)

"""
header 1, header 2, header 3
some string, 123, 456
another string, 987, 654
"""