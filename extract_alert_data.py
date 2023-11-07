import datetime
import os
import lxml.etree as etree
import lxml.html as html
import re
import numpy as np
from matplotlib import pyplot as plt


def extract_file(html_text):
    date_times = []
    locations = []
    for text in html_text.split("<h3 class=\"alertTableDate\">")[1:]:
        cur_date = re.findall("\d\d\.\d\d\.\d\d\d\d", text)[0]
        cur_date = cur_date.split(".")
        for line in text.split("<h5 class=\"alertTableTime\">")[1:]:
            time, location = re.match("(\d\d:\d\d)</h5>(.*?)</div>", line,re.DOTALL).groups()
            date_times.append(datetime.datetime(
                int(cur_date[2]),
                int(cur_date[1]),
                int(cur_date[0]),
                int(time[:2]),
                int(time[3:])))
            location = location.replace("\n",",")
            location = location.replace("\t"," ")
            location = location.replace("  "," ")
            location = location.replace("  "," ")
            location = location.replace("  "," ")
            locations.append(location)
    return date_times, locations


date_times:list[datetime.datetime] = []
locations:list[str] = []
for file in os.listdir("html_files"):
    with open(os.path.join("html_files", file), "r", encoding="utf-8") as f:
        html_text = f.read()
    new_date_times, new_locations = extract_file(html_text)
    for i in range(len(new_date_times)):
        is_duplicate = False
        for j in range(len(date_times)):
            if new_date_times[i] == date_times[j] and new_locations[i] == locations[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            date_times.append(new_date_times[i])
            locations.append(new_locations[i])

all_locations = []
for l in locations:
    all_locations += l.split(",")
all_locations = [l for l in all_locations if len(l) > 1]
for i, l in enumerate(all_locations):
    if l[0] == " ":
        all_locations[i] = l[1:]
    if l[-1] == " ":
        all_locations[i] = l[:-1]
all_locations = [l for l in all_locations if len(l) > 1]
all_locations = np.array(all_locations)
all_locations_unique = np.unique(all_locations)
location_alert_distribution = np.array([np.sum(all_locations == l) for l in all_locations_unique])
sort_permutation = np.argsort(location_alert_distribution)
all_locations_unique = all_locations_unique[sort_permutation]
location_alert_distribution = location_alert_distribution[sort_permutation]