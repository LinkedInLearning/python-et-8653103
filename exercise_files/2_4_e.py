from datetime import datetime
from data_2_4 import weather_data as data

def format_forecast(forecast):
	start_time = forecast["startTime"]
	start_time = datetime.fromisoformat(start_time)
	now = datetime.now().astimezone()
	delta = start_time - now
	return f"""
{start_time.strftime("%B %d, %Y at %I:%M%p")}
{delta.days} days, {delta.seconds//3600} hours
{forecast["detailedForecast"]}"""


forecasts = data["properties"]["periods"]

for forecast in forecasts:
	print(format_forecast(forecast))