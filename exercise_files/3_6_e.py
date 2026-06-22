from data_3_4 import data 

from collections import defaultdict
from pprint import pprint
from datetime import datetime

def format_date(date_str):
    return datetime.fromisoformat(date_str).strftime("%Y-%m-%d")

"""
{
    "2025-02-01": {
        "PRCP": (),

    }
}

"""

structured_weather = defaultdict(dict)

for m in data:
    formatted_date = format_date(m.get("date"))

    if formatted_date not in structured_weather:
        structured_weather[formatted_date] = {}
    
    structured_weather[formatted_date][m.get("datatype")] = (m.get("value"), m.get("attributes"))

pprint(structured_weather)