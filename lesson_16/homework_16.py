import csv

way = "randominfo-master/randominfo/data.csv"
states = set()

with open(way, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) > 8:
            states.add(row[8])
print(states)
print(len(states))