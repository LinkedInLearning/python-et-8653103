from data_3_4 import data
import statistics


def get_aggregate(param, func):
  dailies = [m.get("value") for m in data if m.get("datatype") == param]

  if func == "sum":
    return sum(dailies)
  if func == "avg":
    return statistics.mean(dailies)

agg = get_aggregate("AWND", "sum")

print(agg)