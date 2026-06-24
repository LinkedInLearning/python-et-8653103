from data_4_1_2023 import data as data_2023
from data_4_1_2024 import data as data_2024
from data_4_1_2025 import data as data_2025
from datetime import datetime

data = data_2023 + data_2024 + data_2025

for d in data:
  d["date"] = datetime.fromisoformat(d["date"])