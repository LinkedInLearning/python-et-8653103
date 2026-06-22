json_data = """
{
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
        "generatedAt": "2026-05-25T18:00:46+00:00",
        "updateTime": "2026-05-25T10:12:03+00:00",
        "validTimes": "2026-05-25T04:00:00+00:00/P7DT21H",
        "elevation": {
            "unitCode": "wmoUnit:m",
            "value": 11.8872
        },
        "periods": [
            {
                "number": 1,
                "name": "Memorial Day",
                "startTime": "2026-05-25T14:00:00-04:00",
                "endTime": "2026-05-25T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 72,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 7
                },
                "windSpeed": "8 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/day/fog?size=medium",
                "shortForecast": "Areas Of Fog",
                "detailedForecast": "Areas of fog before 3pm. Mostly cloudy, with a high near 72. Northwest wind around 8 mph."
            },
            {
                "number": 2,
                "name": "Tonight",
                "startTime": "2026-05-25T18:00:00-04:00",
                "endTime": "2026-05-26T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 57,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "3 to 7 mph",
                "windDirection": "W",
                "icon": "https://api.weather.gov/icons/land/night/sct?size=medium",
                "shortForecast": "Partly Cloudy",
                "detailedForecast": "Partly cloudy, with a low around 57. West wind 3 to 7 mph."
            },
            {
                "number": 3,
                "name": "Tuesday",
                "startTime": "2026-05-26T06:00:00-04:00",
                "endTime": "2026-05-26T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 82,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "3 to 13 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/day/sct?size=medium",
                "shortForecast": "Mostly Sunny",
                "detailedForecast": "Mostly sunny, with a high near 82. Southwest wind 3 to 13 mph."
            },
            {
                "number": 4,
                "name": "Tuesday Night",
                "startTime": "2026-05-26T18:00:00-04:00",
                "endTime": "2026-05-27T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 64,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 0
                },
                "windSpeed": "6 to 13 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/few?size=medium",
                "shortForecast": "Mostly Clear",
                "detailedForecast": "Mostly clear, with a low around 64. Southwest wind 6 to 13 mph."
            },
            {
                "number": 5,
                "name": "Wednesday",
                "startTime": "2026-05-27T06:00:00-04:00",
                "endTime": "2026-05-27T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 87,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 24
                },
                "windSpeed": "6 to 10 mph",
                "windDirection": "W",
                "icon": "https://api.weather.gov/icons/land/day/sct/tsra_hi,20?size=medium",
                "shortForecast": "Mostly Sunny then Slight Chance Showers And Thunderstorms",
                "detailedForecast": "A slight chance of showers and thunderstorms after 2pm. Mostly sunny, with a high near 87. West wind 6 to 10 mph. Chance of precipitation is 20%."
            },
            {
                "number": 6,
                "name": "Wednesday Night",
                "startTime": "2026-05-27T18:00:00-04:00",
                "endTime": "2026-05-28T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 59,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 24
                },
                "windSpeed": "5 to 8 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/tsra_hi,20/sct?size=medium",
                "shortForecast": "Slight Chance Showers And Thunderstorms then Partly Cloudy",
                "detailedForecast": "A slight chance of showers and thunderstorms before 10pm. Partly cloudy, with a low around 59. Northwest wind 5 to 8 mph. Chance of precipitation is 20%."
            },
            {
                "number": 7,
                "name": "Thursday",
                "startTime": "2026-05-28T06:00:00-04:00",
                "endTime": "2026-05-28T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 72,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 30
                },
                "windSpeed": "6 to 9 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,30/tsra_hi,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers between 8am and 2pm, then a chance of showers and thunderstorms. Mostly sunny, with a high near 72. North wind 6 to 9 mph. Chance of precipitation is 30%."
            },
            {
                "number": 8,
                "name": "Thursday Night",
                "startTime": "2026-05-28T18:00:00-04:00",
                "endTime": "2026-05-29T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 53,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 23
                },
                "windSpeed": "3 to 7 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/night/tsra_hi,20/sct?size=medium",
                "shortForecast": "Slight Chance Showers And Thunderstorms then Partly Cloudy",
                "detailedForecast": "A slight chance of showers and thunderstorms before 10pm. Partly cloudy, with a low around 53. North wind 3 to 7 mph."
            },
            {
                "number": 9,
                "name": "Friday",
                "startTime": "2026-05-29T06:00:00-04:00",
                "endTime": "2026-05-29T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 67,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 30
                },
                "windSpeed": "3 to 8 mph",
                "windDirection": "NE",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,20/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers after 11am. Partly sunny, with a high near 67. Northeast wind 3 to 8 mph. Chance of precipitation is 30%."
            },
            {
                "number": 10,
                "name": "Friday Night",
                "startTime": "2026-05-29T18:00:00-04:00",
                "endTime": "2026-05-30T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 53,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 36
                },
                "windSpeed": "7 mph",
                "windDirection": "SW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,30/rain_showers,40?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Mostly cloudy, with a low around 53. Southwest wind around 7 mph. Chance of precipitation is 40%."
            },
            {
                "number": 11,
                "name": "Saturday",
                "startTime": "2026-05-30T06:00:00-04:00",
                "endTime": "2026-05-30T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 69,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 35
                },
                "windSpeed": "6 to 12 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,40/rain_showers,30?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Partly sunny, with a high near 69. Northwest wind 6 to 12 mph. Chance of precipitation is 40%."
            },
            {
                "number": 12,
                "name": "Saturday Night",
                "startTime": "2026-05-30T18:00:00-04:00",
                "endTime": "2026-05-31T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 51,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 28
                },
                "windSpeed": "5 to 9 mph",
                "windDirection": "NW",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,30/rain_showers,20?size=medium",
                "shortForecast": "Chance Rain Showers",
                "detailedForecast": "A chance of rain showers. Partly cloudy, with a low around 51. Northwest wind 5 to 9 mph. Chance of precipitation is 30%."
            },
            {
                "number": 13,
                "name": "Sunday",
                "startTime": "2026-05-31T06:00:00-04:00",
                "endTime": "2026-05-31T18:00:00-04:00",
                "isDaytime": true,
                "temperature": 69,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 19
                },
                "windSpeed": "6 to 9 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/rain_showers,20?size=medium",
                "shortForecast": "Slight Chance Rain Showers",
                "detailedForecast": "A slight chance of rain showers. Mostly sunny, with a high near 69. North wind 6 to 9 mph."
            },
            {
                "number": 14,
                "name": "Sunday Night",
                "startTime": "2026-05-31T18:00:00-04:00",
                "endTime": "2026-06-01T06:00:00-04:00",
                "isDaytime": false,
                "temperature": 52,
                "temperatureUnit": "F",
                "temperatureTrend": null,
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 17
                },
                "windSpeed": "6 mph",
                "windDirection": "W",
                "icon": "https://api.weather.gov/icons/land/night/rain_showers,20/sct?size=medium",
                "shortForecast": "Slight Chance Rain Showers then Partly Cloudy",
                "detailedForecast": "A slight chance of rain showers before 8pm. Partly cloudy, with a low around 52. West wind around 6 mph."
            }
        ]
    }
}
"""