weather_data = {
    "@context": [
        "https://geojson.org/geojson-ld/geojson-context.jsonld",
        {
            "@version": "1.1",
            "wx": "https://api.weather.gov/ontology#",
            "geo": "http://www.opengis.net/ont/geosparql#",
            "unit": "http://codes.wmo.int/common/unit/",
            "@vocab": "https://api.weather.gov/ontology#"
        }
    ],
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    -71.1062,
                    42.3998
                ],
                [
                    -71.101,
                    42.4212
                ],
                [
                    -71.13,
                    42.425
                ],
                [
                    -71.1351,
                    42.4036
                ],
                [
                    -71.1062,
                    42.3998
                ]
            ]
        ]
    },
    "properties": {
        "units": "us",
        "forecastGenerator": "BaselineForecastGenerator",
        "generatedAt": "2026-04-11T13:10:52+00:00",
        "updateTime": "2026-04-11T09:14:08+00:00",
        "validTimes": "2026-04-11T03:00:00+00:00/P7DT22H",
        "elevation": {
            "unitCode": "wmoUnit:m",
            "value": 11.8872
        },
        "periods": [
            {
                "number": 1,
                "name": "Today",
                "startTime": "2026-04-11T09:00:00-04:00",
                "endTime": "2026-04-11T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 59,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "18 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/day/few?size=medium",
                "shortForecast": "Sunny",
                "detailedForecast": "Sunny, with a high near 59. Northwest wind around 18 mph, with gusts as high as 31 mph."
            },
            {
                "number": 2,
                "name": "Tonight",
                "startTime": "2026-04-11T18:00:00-04:00",
                "endTime": "2026-04-12T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 35,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "5 to 16 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/skc?size=medium",
                "shortForecast": "Clear",
                "detailedForecast": "Clear, with a low around 35. Northwest wind 5 to 16 mph, with gusts as high as 26 mph."
            },
            {
                "number": 3,
                "name": "Sunday",
                "startTime": "2026-04-12T06:00:00-04:00",
                "endTime": "2026-04-12T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 53,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 2
                },
                "windSpeed": "5 to 10 mph",
                "windDirection": "NE",
                "icon": "https://api.weather.gov/icons/land/day/sct?size=medium",
                "shortForecast": "Mostly Sunny",
                "detailedForecast": "Mostly sunny, with a high near 53. Northeast wind 5 to 10 mph."
            },
            {
                "number": 4,
                "name": "Sunday Night",
                "startTime": "2026-04-12T18:00:00-04:00",
                "endTime": "2026-04-13T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 44,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 51
                },
                "windSpeed": "7 to 12 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,50?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers after 7pm. Cloudy, with a low around 44. South wind 7 to 12 mph. Chance of precipitation is 50%. New rainfall amounts less than a tenth of an inch possible."
            },
            {
                "number": 5,
                "name": "Monday",
                "startTime": "2026-04-13T06:00:00-04:00",
                "endTime": "2026-04-13T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 69,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 44
                },
                "windSpeed": "13 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,40/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Mostly cloudy, with a high near 69. Southwest wind around 13 mph, with gusts as high as 26 mph. Chance of precipitation is 40%."
            },
            {
                "number": 6,
                "name": "Monday Night",
                "startTime": "2026-04-13T18:00:00-04:00",
                "endTime": "2026-04-14T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 59,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 24
                },
                "windSpeed": "6 to 12 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,20/sct?size=medium",
                "shortForecast": "Slight Chance Rain Showers then Partly Cloudy",
                "detailedForecast": "A slight chance of rain showers before midnight. Partly cloudy, with a low around 59. Southwest wind 6 to 12 mph, with gusts as high as 23 mph. Chance of precipitation is 20%."
            },
            {
                "number": 7,
                "name": "Tuesday",
                "startTime": "2026-04-14T06:00:00-04:00",
                "endTime": "2026-04-14T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 77,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 8
                },
                "windSpeed": "7 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/bkn?size=medium",
                "shortForecast": "Partly Sunny",
                "detailedForecast": "Partly sunny, with a high near 77. Southwest wind around 7 mph."
            },
            {
                "number": 8,
                "name": "Tuesday Night",
                "startTime": "2026-04-14T18:00:00-04:00",
                "endTime": "2026-04-15T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 58,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 40
                },
                "windSpeed": "7 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,40?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers after 8pm. Mostly cloudy, with a low around 58. South wind around 7 mph. Chance of precipitation is 40%."
            },
            {
                "number": 9,
                "name": "Wednesday",
                "startTime": "2026-04-15T06:00:00-04:00",
                "endTime": "2026-04-15T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 77,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 29
                },
                "windSpeed": "5 to 9 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Partly sunny, with a high near 77. Southwest wind 5 to 9 mph. Chance of precipitation is 30%."
            },
            {
                "number": 10,
                "name": "Wednesday Night",
                "startTime": "2026-04-15T18:00:00-04:00",
                "endTime": "2026-04-16T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 59,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 33
                },
                "windSpeed": "5 to 8 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Mostly cloudy, with a low around 59. Southwest wind 5 to 8 mph. Chance of precipitation is 30%."
            },
            {
                "number": 11,
                "name": "Thursday",
                "startTime": "2026-04-16T06:00:00-04:00",
                "endTime": "2026-04-16T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 79,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 26
                },
                "windSpeed": "5 to 9 mph",
                "windDirection": "W",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,30/rain_showers,20?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Partly sunny, with a high near 79. West wind 5 to 9 mph. Chance of precipitation is 30%."
            },
            {
                "number": 12,
                "name": "Thursday Night",
                "startTime": "2026-04-16T18:00:00-04:00",
                "endTime": "2026-04-17T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 56,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 21
                },
                "windSpeed": "7 mph",
                "windDirection": "W",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,20?size=medium",
                "shortForecast": "Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers. Mostly cloudy, with a low around 56. West wind around 7 mph."
            },
            {
                "number": 13,
                "name": "Friday",
                "startTime": "2026-04-17T06:00:00-04:00",
                "endTime": "2026-04-17T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 72,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 20
                },
                "windSpeed": "5 to 8 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,20?size=medium",
                "shortForecast": "Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers. Partly sunny, with a high near 72. South wind 5 to 8 mph."
            },
            {
                "number": 14,
                "name": "Friday Night",
                "startTime": "2026-04-17T18:00:00-04:00",
                "endTime": "2026-04-18T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 53,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 21
                },
                "windSpeed": "7 mph",
                "windDirection": "SE",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,20?size=medium",
                "shortForecast": "Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers before 4am. Partly cloudy, with a low around 53. Southeast wind around 7 mph."
            }
        ]
    }
}