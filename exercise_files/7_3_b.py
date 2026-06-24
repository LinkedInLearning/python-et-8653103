import requests
from datetime import datetime

USERNAME = "ryan"
PASSWORD = "snake"

def get_grid_points(latitude, longitude):
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    data = response.json()
    properties = data["properties"]
    return properties["gridId"], properties["gridX"], properties["gridY"]

def get_forecast(office, grid_x, grid_y):
    url = f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast"
    response = requests.get(url)
    data = response.json()
    return data["properties"]["periods"]

def get_weather_for_location(latitude, longitude):
    office, grid_x, grid_y = get_grid_points(latitude, longitude)
    return get_forecast(office, grid_x, grid_y)

def format_weather(periods):
    for period in periods:
        dt = datetime.fromisoformat(period["startTime"])
        formatted_time = dt.strftime("%A, %B %d")
        print(f"{formatted_time}")
        print(f"  {period['detailedForecast']}")
        print()

def parse_coordinates(coord_string):

    parts = coord_string.split(",")
    if len(parts) != 2:
        return None, None

    try:
        lat = float(parts[0].strip())
        lon = float(parts[1].strip())
    except ValueError:
        return None, None

    in_conus   = 24 <= lat <= 49 and -125 <= lon <= -66
    in_alaska  = 51 <= lat <= 71 and -180 <= lon <= -130
    in_hawaii  = 18 <= lat <= 23 and -161 <= lon <= -154

    if not (in_conus or in_alaska or in_hawaii):
        return None, None

    return parts[0].strip(), parts[1].strip()

def auth(username, password):
    if username != USERNAME:
        return False
    if password != PASSWORD:
        return False
    return True


username = input("username: ")
password = input("password: ")

if auth(username, password):
    coordinates = input("lat, long: ")
    latitude, longitude = parse_coordinates(coordinates)
    if latitude and longitude:
        weather = get_weather_for_location(latitude, longitude)
        print(format_weather(weather))
    else:
        raise Exception()
else:
    raise Exception()


# 42.4108682, -71.1204441
