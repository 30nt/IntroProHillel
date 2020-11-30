### chr, ord

print(ord("a"))
print(chr(96))
for index in range(100):
    print(index, chr(index))

alphabet = ''
for index in range(ord("A"), ord("Z") + 1):
    alphabet += chr(index)

print(alphabet)

# Генератор

for symbol in alphabet:
    print(symbol)

[print(symbol) for symbol in alphabet]

numbers = [1, 3, 5, 6, 7, -2]

new_numbers = []
for number in numbers:
    if number > 0:
        new_numbers.append(number ** 2)

new_numbers = [number ** 2 for number in numbers]

print(new_numbers)

print(print("Hello"))
res = [print(number) for number in numbers]
print(res)

new_numbers = [number ** 2 for number in numbers if not number % 2]
print(new_numbers)

alphabet = [chr(index) for index in range(ord('a'), ord('z') + 1)]
alphabet = ''.join(alphabet)
print(alphabet)

# Множество Set

example_string = 'jshdbajhskskahbcjanscbcmn`zcabnx`'

my_list = list(example_string)
print(my_list)

my_random = ''.join(list(set(example_string))[:5])
print(my_random)

my_list = ["3", "6", "2", 8, 1, 9]
my_list = list(set(my_list))
print(my_list)
my_list = list(set(my_list))
print(my_list)

ip_list_1 = ["23.123.45.1", "23.123.45.107", "23.124.45.107"]
ip_list_2 = ["23.123.45.10", "23.123.45.107", "23.124.45.17"]

ip_set_1 = set(ip_list_1)
ip_set_2 = set(ip_list_2)

ip_intersect = ip_set_1.intersection(ip_set_2)
ip_union = ip_set_1.union(ip_set_2)
# ip_set_1.update(ip_set_2)

print(ip_set_1)
print(ip_set_2)
print(ip_intersect)
print(ip_union)

# Словарь Dict
friend = "Iron Arny"
kolobok = {'title': 'kolobok', 'author': None, 'country': "Russia"}

pers = ['John', 'Conor']

person = {'name': 'John',
          'lastname': 'Conor',
          'age': 30,
          "friend": friend,
          'favorit_book': kolobok,
          'function': len}
print(person['name'], pers[0])

print(person["function"]('qwerty'))  # todo ????

my_dict = {1: "1" * 10,
           2: "2" * 10,
           0: "0" * 10}
print(my_dict[1], example_string)

value = 122

# print(my_dict[value % 2])

tup_1 = (1,2,3)
tup_2 = (4,5)
list_1 = [1,2,3]
list_2 = [4,5]
# tup_3 = (list_1, list_2)
#
# list_1 = tuple(list_1)

my_dict = {tup_1: "One", tup_2: "Two", 3: "???"}

my_dict["new_key"] = "VALUE"

print(my_dict)
