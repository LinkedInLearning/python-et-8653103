import json
from data_8_3 import json_data
from datetime import datetime
import csv 

def parse_dates(object):
    datetime_fields = ["generatedAt", "updateTime", "startTime", "endTime"]
    for key, val in object.items():
        if key in datetime_fields:
            object[key] = datetime.fromisoformat(val)
    return object

data = json.loads(json_data, object_hook=parse_dates)

"""
            {
                "number": 13,
                "name": "Sunday",
                "startTime": "2026-05-31T06:00:00-04:00",
                "endTime": "2026-05-31T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 69,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 19
                },
                "windSpeed": "6 to 9 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,20?size=medium",
                "shortForecast": "Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers. Mostly sunny, with a high near 69. North wind 6 to 9 mph."
            },
"""

periods = data["properties"]["periods"]

def get_csv_row(p):
    return [
        p.get("startTime").strftime(f"%b %d, %Y at %I%p"),
        f"{p.get('temperature')}°{p.get('temperatureUnit')}",
        f"{p.get("probabilityOfPrecipitation", {}).get("value")}%",
        p.get("shortForecast")
    ]

with open("weather.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'temperature', 'probability of precipitation', 'short forecast'])
    writer.writerows([get_csv_row(p) for p in periods])

with open("weather.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)