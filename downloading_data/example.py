import csv
from datetime import datetime

from matplotlib import pyplot as plt 

# get dates and high and low temperatures from file
filename = '/Users/spacetrav/Documents/Files/Python/downloading_data/death_valley_2014.csv'
filename1 = '/Users/spacetrav/Documents/Files/Python/downloading_data/sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

with open(filename1) as f:
    reader1 = csv.reader(f)
    header_row1 = next(reader1)

    dates1, highs1, lows1 = [], [], []
    for row in reader1:
        try:
            current_date1 = datetime.strptime(row[0], "%Y-%m-%d")
            high1 = int(row[1])
            low1 = int(row[3])
        except ValueError:
            print(current_date1, 'missing data')
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)

# plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates1, highs1, c='blue', alpha = 0.5)
# plt.fill_between(dates, highs, highs1, facecolor='blue', alpha=0.1)

# format plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()