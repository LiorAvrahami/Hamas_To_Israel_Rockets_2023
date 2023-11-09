from extract_alert_data import date_times,locations,all_locations_unique,location_alert_distribution
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
import matplotlib
import datetime

csv_text = ""
for i in range(len(date_times)):
    csv_text += f"{date_times[i]}, {locations[i]}\n"

with open("alert_data_exported_to_csv.csv","w+", encoding="utf-8") as f:
    f.write(csv_text)
