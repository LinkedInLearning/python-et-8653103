from data_2_2 import weather_data as data


def deconstruct_forecast(forecast):
    forecast = forecast.split('.')
    cleaned = []
    for f in forecast:
        cleaned.append(f.strip())
    print(cleaned)
    categorized = {
        'temp': [],
        'wind': [],
        'prec': [],
        'other': []
    }

    for c in cleaned:
        if 'wind' in c.lower():
            categorized['wind'].append(c)
        elif ", with a" in c:
            categorized["temp"].append(c)
        elif "rain" in c.lower():
            categorized["prec"].append(c)
        elif "snow" in c.lower():
            categorized["prec"].append(c)
        elif "precipitation" in c.lower():
            categorized["prec"].append(c)
        else:
            if len(c) > 0:
                categorized["other"].append(c)

    return categorized

    

weather_periods = data["properties"]["periods"]

forecast = weather_periods[3]["detailedForecast"]

print(deconstruct_forecast(forecast))
