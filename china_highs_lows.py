import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/2975555.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置字体为楷体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置图形的格式
ax.set_title("2020年每日最高最低温度\n上海", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
