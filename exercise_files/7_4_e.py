import requests
from datetime import datetime
import time
import traceback
import logging

logging.basicConfig(
    filename='app.log', 
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

USERNAME = "ryan"
PASSWORD = "snake"

class AuthError(Exception):
    pass

class UsernameError(AuthError):
    pass

class PasswordError(AuthError):
    pass

class LocationError(Exception):
    pass

class UpstreamError(Exception):
    pass

def get_grid_points(latitude, longitude):
    url = f"https://aasdflkjasdfi.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    data = response.json()
    properties = data["properties"]
    raise Exception()
    return properties["gridId"], properties["gridX"], properties["gridY"]

def get_forecast(office, grid_x, grid_y):
    url = f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast"
    response = requests.get(url)
    data = response.json()
    return data["properties"]["periods"]

def get_weather_for_location(latitude, longitude, retry=0):
    try:
        office, grid_x, grid_y = get_grid_points(latitude, longitude)
        return get_forecast(office, grid_x, grid_y)
    except Exception as e:
        if retry > 4:
            raise UpstreamError("Error getting data from upstream service") from e
        time.sleep(0.5)
        return get_weather_for_location(latitude, longitude, retry=retry+1)

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
        raise LocationError(f"Need two comma separated parts, got {coord_string}")

    try:
        lat = float(parts[0].strip())
        lon = float(parts[1].strip())
    except ValueError:
        raise LocationError(f"Both parts must be floats. Got {type(parts[0])}, {type(parts[1])}")

    in_conus   = 24 <= lat <= 49 and -125 <= lon <= -66
    in_alaska  = 51 <= lat <= 71 and -180 <= lon <= -130
    in_hawaii  = 18 <= lat <= 23 and -161 <= lon <= -154

    if not (in_conus or in_alaska or in_hawaii):
        raise LocationError(f"Coordinates must be in United States.")

    return parts[0].strip(), parts[1].strip()


def auth(username, password):
    if username != USERNAME:
        raise UsernameError()
    if password != PASSWORD:
        raise PasswordError()
    return True


def do_workflow():
    username = input("username: ")
    password = input("password: ")

    auth(username, password)
    coordinates = input("lat, long: ")
    latitude, longitude = parse_coordinates(coordinates)
    weather = get_weather_for_location(latitude, longitude)
    print(format_weather(weather))

try:
    do_workflow()
except AuthError as e:
    logging.info(traceback.format_exception(e))
    print("Bad credentials")
except LocationError as e:
    print(e)
except UpstreamError as e:
    traceback.print_exception(e)
    print(e)
except Exception as e:
    print("Something bad happened!")

# 42.4025077778, -71.122014925
