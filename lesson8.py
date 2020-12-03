# параметры функций
# *args, **kwargs
# распаковка словарей
# time, sys, os, os.path
# работа с файлами

from random import randint, shuffle

DEBUG_MODE = False


def create_random_list(limit_value, limit_number, dummy_value):
    # def create_random_list(*args, **kwargs):
    """Create list with random values"""
    result = [randint(1, limit_value) for _ in range(randint(1, limit_number))]
    return result


def my_pow(a, b, print_mode=DEBUG_MODE):
    result = a ** b
    if print_mode:
        print(f"{a} ** {b} = {result}")
    return result


# result = my_pow(3, 3, True)
limit_value = 10
limit_number = 5

result = create_random_list(limit_value=limit_value,
                            limit_number=limit_number,
                            dummy_value='')

print(result)

my_dict_1 = {1:"1", 2:"2"}
my_dict_2 = {3:"3", 4:"4", 2: "6"}
my_dict_3 = {**my_dict_1, ** my_dict_2}
print(my_dict_3)

import time
import sys

print(sys.argv)

start_time = time.time()
value = int(sys.argv[1])
sum = 0
for value in range(value):
    sum += value
print(f"Time: {time.time() - start_time} Sum = {sum}")

import os
import string
list_dir = os.listdir("Homeworks")
print(list_dir)
list_dir = os.listdir(".")  # Текущая директория
print(list_dir)


# V1
# file = open("lesson3.py", "r")
# # data = file.read()  # Считать одной строкой
# # data = file.readlines()  # Считать по строкам
# data = []
# for line in file.readlines():
#     data.append(line.strip())
#     # print(">>>>", line.strip())
# print(data)
# file.close()

#V2 менеджер контекста
with open("lesson3.py", "r") as file:
    data = []
    for line in file.readlines():
        data.append(line.strip())
print(data)

data_str = "QWERTY\nASDFG"
data_list = ["asd", "zxc"]

with open("test.txt", "w") as file:
    # file.write("\n".join(data_list))
    for line in data_list:
        file.write(f"{line}\n")


################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

path_dir = "alphabet"
try:
    os.mkdir(path_dir)
except FileExistsError:
    pass

for symbol in string.ascii_lowercase:
    with open(os.path.join(path_dir, f"{symbol}.txt"), 'w') as file:
        file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

tanos_list = os.listdir(path_dir)
tanos_list = list(set(tanos_list))
for filename in tanos_list[: len(tanos_list) // 2]:
    os.remove(os.path.join(path_dir, filename))

