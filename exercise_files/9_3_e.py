import requests

ip = "72.74.186.87"

response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()
lat, lon = data.get('lat'), data.get('lon')

response = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
data = response.json()

forecast_url = data.get('properties').get('forecast')

response = requests.get(forecast_url)
data = response.json()
print(data["properties"]["periods"][0]["detailedForecast"])