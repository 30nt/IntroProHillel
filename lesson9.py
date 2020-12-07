# Разбор ДЗ

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
#
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# 7. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = "qqqqqqqqqqqqqqqqsgfajsnkcasjdcvajsjzdfgchjabstgfvb"
my_str_2 = "qqqqqqqqkcasjdcvajsjzdfgcsjdfghajsdbcjhjabstgfvb"
# result = []
# for symbol in my_str:
#     if my_str.count(symbol) == 1:
#         result.append(symbol)
# print(result)
result = []
my_str_set = set(my_str_1).intersection(set(my_str_2))
print(my_str_set)
for symbol in my_str_set:
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        result.append(symbol)
print(result)

# О json

import json

person = {"name": "Chuck",
          "last_name": "Norris",
          "age": None,
          "skills": {"1":"face",
                     "2": "arm"}}

# person = [1,2,3,4,5]

with open("test_json.json", "w") as file:
    json.dump(person, file)

with open("test_json.json", "r") as file:
    person_json = json.load(file)

# person_json = json.loads(person)
print(person_json[3], type(person_json))


# О cvs

import csv

data = []
with open("test_csv.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        data.append(line)
print(data[0])
data.append({'Url': 'google.com.ua',
             'Date': '8.12.20',
             'Value': '1000',
             'Comment': 'Cool',
             'Comment2': 'SUPER'})

for row in data:
    print(row["Date"])

with open("test_csv_w.csv", "w") as csv_file:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

data = []
with open("test_csv.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        data.append(line)
print(data)
data[0].append("Comment")
for line in data[1:]:
    line.append("Cool")

with open("test_csv.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
    for line in data[1:]:
        writer.writerow(line)


# О ДЗ

# def generate_and_write_file(filename):
#     text = create_txt()
#     write_txt(text)
#
# generate_and_write_file("my_new_file.txt")
# generate_and_write_file("my_new_file.json")
# generate_and_write_file("my_new_file.csv")
# generate_and_write_file("my_new_file.exe")
#
# def create_txt():
#     return "asdascjasbcjn"
#
# def write_txt(text):
#     pass
#
# text = create_txt()
# write_txt(text)