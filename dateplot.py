import csv
from collections import defaultdict
import matplotlib.pylab as plt
import pandas as pd

with open('dates.csv', 'r') as f:
    read = csv.reader(f)
    data = list(read)

data = data[0]


d = defaultdict(int)
for word in data:
    d[word] += 1

df = pd.DataFrame.from_dict(d, orient='index')
df = df.rename(index=str, columns={0: "freq"})

df = df.sort_index(ascending=False)
# print(df.head())
# df.plot()
# plt.show(block=True)
df.to_csv('freqdates.csv')

