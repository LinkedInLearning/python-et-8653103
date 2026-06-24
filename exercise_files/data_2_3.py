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
        "generatedAt": "2026-06-22T20:47:26+00:00",
        "updateTime": "2026-06-22T16:01:27+00:00",
        "validTimes": "2026-06-22T10:00:00+00:00/P7DT15H",
        "elevation": {
            "unitCode": "wmoUnit:m",
            "value": 11.8872
        },
        "periods": [
            {
                "number": 1,
                "name": "This Afternoon",
                "startTime": "2026-06-22T16:00:00-04:00",
                "endTime": "2026-06-22T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 79,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 54
                },
                "windSpeed": "7 mph",
                "windDirection": "SE",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,50?size=medium",
                "shortForecast": "Rain Showers Likely",
                "detailedForecast": "Rain showers likely. Mostly cloudy, with a high near 79. Southeast wind around 7 mph. Chance of precipitation is 50%. New rainfall amounts less than a tenth of an inch possible."
            },
            {
                "number": 2,
                "name": "Tonight",
                "startTime": "2026-06-22T18:00:00-04:00",
                "endTime": "2026-06-23T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 61,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 92
                },
                "windSpeed": "8 mph",
                "windDirection": "SE",
                "icon": "https://api.weather.gov/icons/land/night/tsra,90?size=medium",
                "shortForecast": "Showers And Thunderstorms",
                "detailedForecast": "Rain showers before 8pm, then showers and thunderstorms between 8pm and 9pm, then patchy fog and showers and thunderstorms between 9pm and 11pm, then patchy fog and showers and thunderstorms. Cloudy, with a low around 61. Southeast wind around 8 mph. Chance of precipitation is 90%. New rainfall amounts between a half and three quarters of an inch possible."
            },
            {
                "number": 3,
                "name": "Tuesday",
                "startTime": "2026-06-23T06:00:00-04:00",
                "endTime": "2026-06-23T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 76,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 92
                },
                "windSpeed": "5 to 8 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/tsra,90/tsra,60?size=medium",
                "shortForecast": "Patchy Fog",
                "detailedForecast": "Patchy fog and showers and thunderstorms before 8am, then patchy fog and showers and thunderstorms. Mostly cloudy, with a high near 76. Southwest wind 5 to 8 mph. Chance of precipitation is 90%. New rainfall amounts between a quarter and half of an inch possible."
            },
            {
                "number": 4,
                "name": "Tuesday Night",
                "startTime": "2026-06-23T18:00:00-04:00",
                "endTime": "2026-06-24T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 61,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 26
                },
                "windSpeed": "6 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,30/bkn?size=medium",
                "shortForecast": "Chance Rain Showers then Mostly Cloudy",
                "detailedForecast": "A chance of rain showers before 9pm. Mostly cloudy, with a low around 61. Northwest wind around 6 mph. Chance of precipitation is 30%. New rainfall amounts less than a tenth of an inch possible."
            },
            {
                "number": 5,
                "name": "Wednesday",
                "startTime": "2026-06-24T06:00:00-04:00",
                "endTime": "2026-06-24T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 85,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 3
                },
                "windSpeed": "6 to 9 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/day/few?size=medium",
                "shortForecast": "Sunny",
                "detailedForecast": "Sunny, with a high near 85. Northwest wind 6 to 9 mph."
            },
            {
                "number": 6,
                "name": "Wednesday Night",
                "startTime": "2026-06-24T18:00:00-04:00",
                "endTime": "2026-06-25T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 63,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "2 to 8 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/few?size=medium",
                "shortForecast": "Mostly Clear",
                "detailedForecast": "Mostly clear, with a low around 63. Northwest wind 2 to 8 mph."
            },
            {
                "number": 7,
                "name": "Thursday",
                "startTime": "2026-06-25T06:00:00-04:00",
                "endTime": "2026-06-25T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 86,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 2
                },
                "windSpeed": "1 to 7 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/day/sct?size=medium",
                "shortForecast": "Mostly Sunny",
                "detailedForecast": "Mostly sunny, with a high near 86. South wind 1 to 7 mph."
            },
            {
                "number": 8,
                "name": "Thursday Night",
                "startTime": "2026-06-25T18:00:00-04:00",
                "endTime": "2026-06-26T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 65,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 58
                },
                "windSpeed": "6 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/night/bkn/tsra_hi,60?size=medium",
                "shortForecast": "Mostly Cloudy then Showers And Thunderstorms Likely",
                "detailedForecast": "A slight chance of rain showers between midnight and 2am, then showers and thunderstorms likely. Mostly cloudy, with a low around 65. South wind around 6 mph. Chance of precipitation is 60%."
            },
            {
                "number": 9,
                "name": "Friday",
                "startTime": "2026-06-26T06:00:00-04:00",
                "endTime": "2026-06-26T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 85,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 56
                },
                "windSpeed": "5 to 10 mph",
                "windDirection": "S",
                "icon": "https://api.weather.gov/icons/land/day/tsra_sct,60/tsra_sct,50?size=medium",
                "shortForecast": "Showers And Thunderstorms Likely",
                "detailedForecast": "Showers and thunderstorms likely. Partly sunny, with a high near 85. South wind 5 to 10 mph. Chance of precipitation is 60%."
            },
            {
                "number": 10,
                "name": "Friday Night",
                "startTime": "2026-06-26T18:00:00-04:00",
                "endTime": "2026-06-27T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 66,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 42
                },
                "windSpeed": "3 to 8 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/tsra_hi,40/tsra_hi,20?size=medium",
                "shortForecast": "Chance Showers And Thunderstorms",
                "detailedForecast": "A chance of showers and thunderstorms. Mostly cloudy, with a low around 66. Southwest wind 3 to 8 mph. Chance of precipitation is 40%."
            },
            {
                "number": 11,
                "name": "Saturday",
                "startTime": "2026-06-27T06:00:00-04:00",
                "endTime": "2026-06-27T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 86,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 33
                },
                "windSpeed": "3 to 7 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Partly sunny, with a high near 86. Southwest wind 3 to 7 mph. Chance of precipitation is 30%."
            },
            {
                "number": 12,
                "name": "Saturday Night",
                "startTime": "2026-06-27T18:00:00-04:00",
                "endTime": "2026-06-28T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 66,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 31
                },
                "windSpeed": "2 to 6 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,30/rain_showers,20?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers before 2am. Partly cloudy, with a low around 66. Southwest wind 2 to 6 mph. Chance of precipitation is 30%."
            },
            {
                "number": 13,
                "name": "Sunday",
                "startTime": "2026-06-28T06:00:00-04:00",
                "endTime": "2026-06-28T18:00:00-04:00",
                "isDaytime": True,
                "temperature": 87,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 16
                },
                "windSpeed": "2 to 7 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/sct/rain_showers,20?size=medium",
                "shortForecast": "Mostly Sunny then Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers after 4pm. Mostly sunny, with a high near 87. North wind 2 to 7 mph."
            },
            {
                "number": 14,
                "name": "Sunday Night",
                "startTime": "2026-06-28T18:00:00-04:00",
                "endTime": "2026-06-29T06:00:00-04:00",
                "isDaytime": False,
                "temperature": 66,
                "temperatureUnit": "F",
                "temperatureTrend": None,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 14
                },
                "windSpeed": "5 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/sct?size=medium",
                "shortForecast": "Partly Cloudy",
                "detailedForecast": "Partly cloudy, with a low around 66. Northwest wind around 5 mph."
            }
        ]
    }
}