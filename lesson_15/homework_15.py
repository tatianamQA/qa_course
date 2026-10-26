import csv
from pathlib import Path

csv_folder = Path(__file__).parent/"ideas_for_test"/"work_with_csv"
csv_file_1 = csv_folder/"random.csv"
csv_file_2 = csv_folder/"random-michaels.csv"
# print(csv_file_1.exists())
# print(csv_file_2.exists())


all_rows = []
with open(csv_file_1, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[-1] == "":
            row.pop()
        row[4] = row[4].replace("/", ".")
        all_rows.append(tuple(row))
# print(len(all_rows))

with open(csv_file_2, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[-1] == "":
            row.pop()
        row[4] = row[4].replace("/", ".")
        all_rows.append(tuple(row))
# print(len(all_rows))

dict_with_rows = dict.fromkeys(all_rows)
final_list = list(dict_with_rows)
# print(len(dict_with_rows))
# print(final_list[0])

new_file_csv = Path(__file__).parent/"result_medvedchuk.csv"

with open(new_file_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(final_list)


# for row in all_rows:
#     if row[0] == '1885':
#         print(row)
""" перевірила чим відрізняються строки,
щоб привести їх в однаковий вигляд і тоді дійсно видалити дублікат"""
