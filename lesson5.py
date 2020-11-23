REVERSE = True

my_str = 'blablacarbla'
my_symbol = "bla"
"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
2
"""
count = my_str.count(my_symbol)
print(count)

print('-------------------------')
"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacarbla", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
res = [my_symbol] * count
# 1
res_str = "\n".join(res)
print(res_str)
print('______')
# 2
for value in res:
    print(value)


"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
my_str_upper = my_str.upper()
# exists = []
exists = ''
for symbol in my_str_upper:
    if symbol not in exists:
        # exists.append(symbol)
        exists += symbol
print(len(exists), exists)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке
"""
my_list = []
print(my_str)
for symbol in my_str[::2]:
    my_list.append(symbol)
# my_list = list(res)
print(my_list)

# ИНДЕКСЫ ))

for index, value in enumerate(my_str):
    if not index % 2:
        my_list.append(value)
print(my_list)


"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_str = "qwerty"
my_list = []
str_index = [1,2,1,4,5,3,0,0,2,1,6,4,4,5,5,5]
for index in str_index:
    if index < len(my_str):
        my_list.append(my_str[index])
print(my_list)

"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное
"""
my_list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list_2 = [1, 2, 3, 4, 5, 6]
my_result = []

if len(my_list_1) == len(my_list_2):
    for index in range(len(my_list_1)):
        my_result.append(my_list_1[index])
        my_result.append(my_list_2[index])
    # for index, value in enumerate(my_list_1):
    #     my_result.append(value)
    #     my_result.append(my_list_2[index])
else:
    count = min(len(my_list_1), len(my_list_2))
    for index in range(count):
        my_result.append(my_list_1[index])
        my_result.append(my_list_2[index])
####### Оставить my_list_1, my_list_2 без изменения
    if len(my_list_1) < len(my_list_2):
        my_list_1, my_list_2 = my_list_2, my_list_1
    my_result = my_result + my_list_1[count:]

print(my_result)








"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить 
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2.
"""






"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""

value = 1273412374627
result = len(str(value))
print(result)










"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""

res = max(str(value))
print(res)










"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""

value = 1200001
res = int(str(value)[::-1])
print(res)






"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""


value = 1200001
val_list = list(str(value))
val_list.sort(reverse=REVERSE)
print(val_list)
res = int(''.join(val_list))
print(res)
# сортировка списка
val_list.sort()
for value in val_list:
    print("Value", value)

# сортировка копии списка

for value in sorted(val_list, reverse=REVERSE):
    print("Value", value)
print(val_list)


"""
Цикл с условием(while)
Игра с угадыванием числа.

"""
VALUE = 12
my_value = int(input("Введи число от 1 до 99"))
win_flag = False
while not win_flag:
    if my_value > VALUE:
        my_value = int(input("Введи число меньше"))
    else:
        my_value = int(input("Введи число больше"))
    win_flag = my_value == VALUE

# while my_value != VALUE:
#     if my_value > VALUE:
#         my_value = int(input("Введи число меньше"))
#     else:
#         my_value = int(input("Введи число больше"))




print("Победа!")




### chr, ord