import requests
from requests import ConnectionError

class MalformedResponse(Exception):
    pass

class UnreachableServer(Exception):
    pass

def fetch_json(url):
    try:
        response = requests.get(url)
    except ConnectionError:
        raise UnreachableServer(url)
    
    response.raise_for_status()
    
    try:
        data = response.json()
    except Exception:
        raise MalformedResponse(f"Could not parse {response.text}")
    if not data:
        raise MalformedResponse("Received empty JSON")

    return data 

def get_lat_lon(ip):
    data = fetch_json(f"http://ip-api.com/json/{ip}")
    1/0
    return data['lat'], data['lon']

def get_forecast_url(lat, lon):
    data = fetch_json(f"https://api.weather.gov/points/{lat},{lon}")
    return data['properties']['forecast']

def get_forecast(forecast_url):
    data = fetch_json(forecast_url)
    return data["properties"]["periods"][0]["detailedcast"]

def handler(func, *args):
    try:
        return func(*args)
    except MalformedResponse as e:
        raise e
    except UnreachableServer as e:
        raise e
    except KeyError as e:
        raise MalformedResponse(f"{e} is missing in {func.__name__} data")
    except Exception as e:
        print("Some unanticipated error happened!")
        raise e

ip = ""
ip = "150.171.22.12"

lat, lon = handler(get_lat_lon, ip)
forecast_url = handler(get_forecast_url, lat, lon)
forecast = handler(get_forecast, forecast_url)

print(forecast)