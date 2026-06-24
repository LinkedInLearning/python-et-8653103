from data_3_4 import data
from pprint import pprint
from collections import defaultdict
from datetime import datetime

#{ 
#  "2025-02-01": {
#		"SNOW": (0.1, ",,W,"),
#		"PRCP": (0.1, ",,W,"),
#		"AWND": (0.1, ",,W,"),
#	},
#	"2025-02-02": {
#		"PRCP": (0.1, ",,W,"),
#		"AWND": (0.1, ",,W,"),
#	}
#}


def format_date(date_str):
    return datetime.fromisoformat(date_str).strftime("%Y-%m-%d")
structured_weather = defaultdict(dict)

for m in data:
  formatted_date = format_date(m.get("date"))

  structured_weather[formatted_date][m.get("datatype")] = (m.get("value"), m.get("attributes"))


pprint(structured_weather)