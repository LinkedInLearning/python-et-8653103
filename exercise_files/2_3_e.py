from data_2_3 import weather_data


def deconstruct_forecast(forecast):
  forecast = forecast.split(".")
  cleaned = []

  for f in forecast:
    cleaned.append(f.strip())

  categorized = {
    "temp": [],
    "wind": [],
    "prec": [],
    "other": []
  }

  for c in cleaned:
    if "wind" in c.lower():
      categorized["wind"].append(c)
    elif ", with a" in c:
      categorized["temp"].append(c)
    elif "rain" in c:
      categorized["prec"].append(c)
    elif "snow" in c:
      categorized["prec"].append(c)
    elif "precipitation" in c:
      categorized["prec"].append(c)
    else:
      if len(c) > 0:
        categorized["other"].append(c)
  print(categorized)

weather_periods = weather_data["properties"]["periods"]

forecast = weather_periods[0]["detailedForecast"]

print(deconstruct_forecast(forecast))