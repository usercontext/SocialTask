import json
import gensim
import numpy as np
import iso8601
import datetime
import csv

global count
count = 0

global datelist
datelist = []

with open('scraped_data3.json') as f:
    data_root = json.load(f)

def recurse(data, depth=0):
    global count, datelist
    if data["children"]:
        for i in data["children"]:
            recurse(i)
    if data["content"]:
        for ii in data["content"]:
            if ii["meta"]["stats"]["updated"]:
                datelist.append(iso8601.parse_date(ii["meta"]["stats"]["updated"]).strftime('%Y-%m-%d'))
        # exit()
    count += 1


recurse(data_root)

with open('dates.csv', 'w') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(datelist)