import datetime
import re

import matplotlib.pyplot as plt

NUM_PACKS_TO_REACH = 100000
PYPI = 'https://pypi.python.org/pypi'
DATA = './data.txt'

if __name__ == "__main__":
    dates = []
    counts = []
    re_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2}):(\d+)')
    with open(DATA) as data_file:
        for line in data_file:
            year, month, day, hour, minute, second, count = map(int, re_pattern.match(line).groups())
            dates.append(datetime.datetime(year, month, day,
                                           hour, minute, second))
            counts.append(count)

    plt.plot(dates, counts)
    plt.show()
