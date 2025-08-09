"""
Ohio Unemployment Graph

David Kiener
08-09-2025

This progam graphs the Ohio unemployment rate from 1976 to 2022 obtained by FRED Economic Data.

"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, col_title in enumerate(header_row):
    print(f"{index} {col_title}, ", end=' ')
print()

dates = []
percentages = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        percent = float(row[1])
    except ValueError as e:
        print(current_date)
    else:
        dates.append(current_date)
        percentages.append(percent)

# plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, percentages, color='blue')
# graph.fill_between(dates, high_temps, low_temps, color='blue', alpha=0.5)

graph.set_title('Ohio Unemployment (by Month): 1976 - 2022', fontsize='24')
graph.set_xlabel('Date', fontsize=16)
graph.set_ylabel('Unemp Rate', fontsize=16)
figure.autofmt_xdate()

plt.show()