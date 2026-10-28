import csv
import json
import sys
import xml.etree.ElementTree as ET
import logging
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


json_folder = Path(__file__).parent/"ideas_for_test"/"work_with_json"

json_loger = logging.getLogger("json_file_checking")
json_loger.setLevel(logging.ERROR)
file_handler = logging.FileHandler(Path(__file__).parent/"json_medvedchuk.log", encoding="utf-8")
json_loger.addHandler(file_handler)


for file in json_folder.iterdir():
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError:
        json_loger.error(f"Цей файл є невалідним {file.name} ")


xml_file = Path(__file__).parent/"ideas_for_test"/"work_with_xml"/"groups.xml"

tree = ET.parse(xml_file)
root = tree.getroot()


def find_incoming_for_number(number):
    for group in root:
        if group.find("number").text == str(number):
            incoming_group = group.find("timingExbytes/incoming")
            if incoming_group is None:
                return None
            return incoming_group.text

xml_logger = logging.getLogger("xml_file_checking")
xml_logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
xml_logger.addHandler(console_handler)


number = 2
result = find_incoming_for_number(number)
xml_logger.info(f"Group {number}, timingExbytes/incoming {result}")




