from data_5_3 import data
from datetime import datetime
import statistics

for d in data:
    d['date'] = datetime.fromisoformat(d['date'])
 
def get_weather_data(start_date, end_date, attributes=['AWND', 'PRCP', 'TMAX', 'TMIN'], aggregation=None):
    filtered = [d for d in data if d['date'] >= start_date and d['date'] <= end_date]
    filtered = [{a: d[a] for a in attributes + ['date']} for d in filtered]
    if aggregation:
        return {a: aggregation([f[a][0] for f in filtered]) for a in attributes}

    return filtered


filtered = get_weather_data(
    datetime(2024, 6, 1),
    datetime(2024, 6, 7),
    aggregation=statistics.mean
    )

print(filtered)