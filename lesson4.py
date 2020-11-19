# Методы строк join split
my_list = list("qwerty")
my_list.reverse()
result = []
print(my_list)
for value in my_list:
    result.append(value * 2)
print(result)

new_str = ".".join(result)
print(new_str)

new_result = new_str.split("e")
print(new_result)

# list - список. Изменяемый набор объектов.

any_list = [3, 5, 1, 5, 0, 7]
another_list = any_list.copy()
any_list.sort()
print(any_list)
print(another_list)
my_l = [1, 2, 3, 2, 3]

value = my_l[1]
# index = my_l.index(value)
# index = -2
del my_l[-2]
# my_l.remove(my_l[index])

print(my_l)

my_l_2 = [my_l.copy()] * 2
my_l.append(4)
print(my_l_2)

my_tuple = tuple(my_l)
print(my_tuple, type(my_tuple))
my_list = list(my_tuple)
print(my_list, type(my_list))




my_list = [(1, "111"), (2,  "222"), (3, "333")]
my_list_2 = ("one", "two")
# print(my_list[-3])
# print(my_list[::-1])
# for item_1, item_2 in my_list:
#     print(item_2)

my_list[0] = ""
my_list.append("Hello")
my_list.append([4, "444"])
my_list.extend(my_list_2)
last_one = my_list.pop()
print(my_list, last_one)
my_list.insert(0, "Im first")
print(my_list)
my_list.remove("one")
print(my_list)


# int, float, str, bool
# tuple - кортеж. Неизменяемый набор объектов

server_response = (None, "Hello", "19/11/2020", "", "", "")
# server_response[1] = "Hi!"
status, text, *_ = server_response
# text = server_response[1]

print(status, text, _)

my_tuple = (1, 2, 3, "1", "2", "3")
a, b, c, d, e, f = my_tuple
print(e, a)

# print(my_tuple, type(my_tuple))
print(my_tuple[::-1])
print(my_tuple[2:-1])
for item in my_tuple:
    print(item)

val_1 = 3
val_2 = 4

val_1, val_2 = val_2, val_1

some_tuple = val_2, val_1
print(some_tuple, type(some_tuple))

tmp = val_1
val_1 = val_2
val_2 = tmp

print(val_1, val_2)


value = input("Введи целое число")

if value.isdigit():
    if int(value) != 0:
        value = int(value)
        result = 1 / value
        print(result)
    else:
        print("Division by zero")
else:
    print("This value isn't digit")

try:
    value = int(value)
    result = 1 / value
    print(result)
# except ZeroDivisionError:
#     print("Division by zero")
# except ValueError:
#     print("This value isn't digit")
except (ZeroDivisionError, ValueError):
    print("Some error in this case")
