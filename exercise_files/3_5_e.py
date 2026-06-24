from data_3_4 import data

from datetime import datetime

def format_date(date):
  return datetime.fromisoformat(date).strftime("%Y-%m-%d")


snowfall_by_date = {
  format_date(m.get("date")): m.get("value") 
  for m in data 
  if m.get("datatype") == "SNOW"
}


print(snowfall_by_date)