from data_4_1_2023 import data as data_2023
from data_4_1_2024 import data as data_2024
from data_4_1_2025 import data as data_2025
from data_4_1_dates import dates
import statistics

YEAR_LENGTH = 365

def get_windiest_year(date1, date2, date3):
  windspeed_to_years = {
    date1["AWND"][0]: date1["date"].split("-")[0],
    date2["AWND"][0]: date2["date"].split("-")[0],
    date3["AWND"][0]: date3["date"].split("-")[0],
  }

  highest_windspeed = max(windspeed_to_years)
  return windspeed_to_years[highest_windspeed]

assert len(data_2023) == len(data_2024) == len(data_2025) == YEAR_LENGTH

results = [get_windiest_year(data_2023[i], data_2024[i], data_2025[i]) for i in range(0, YEAR_LENGTH)]

results = [get_windiest_year(date1, date2, date3) for date1, date2, date3 in zip(data_2023, data_2024, data_2025)]

print(statistics.mode(results))

for i, date in enumerate(dates):
  print(f"On {date} the windiest year was: {get_windiest_year(data_2023[i], data_2024[i], data_2025[i])}")