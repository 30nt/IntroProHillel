# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.

import random


def generate_string(min_limit=100, max_limit=1000) -> str:
    str_len = random.randint(min_limit, max_limit)
    res_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(str_len)]
    return ''.join(res_list)


def transformation_with_spaces(str_to_transform: str) -> str:
    count_spaces = len(str_to_transform) // 5
    spaces_indexes = []
    while len(spaces_indexes) < count_spaces:
        index = random.randint(5, len(str_to_transform) - 5)
        if index not in spaces_indexes:
            spaces_indexes.append(index)
    for index in spaces_indexes:
        str_to_transform = str_to_transform[:index] + " " + str_to_transform[index + 1:]
    return str_to_transform


def change_first_symbol(word: str) -> str:
    return word.capitalize()


def change_last_symbol(word: str) -> str:
    puntcuations = ",.!?"
    word = word[:-1] + random.choice(puntcuations) if len(word) > 3 else word
    return word


def change_word_to_number(word):
    if len(word) <= 3:
        number_list = [str(random.randint(0, 9)) for _ in range(len(word))]
        word = "".join(number_list)
    return word


# TRANSFORM_FUNCTIONS = {
#     1: change_first_symbol,
#     2: change_last_symbol,
#     3: change_word_to_number,
#
# }


def random_word_transformation(word):
    state = random.randint(1, 4)
    # word = TRANSFORM_FUNCTIONS[state](word)
    if state == 1:
        word = change_first_symbol(word)
    elif state == 2:
        word = change_last_symbol(word)
    elif state == 3:
        word = change_word_to_number(word)
    return word


def transform_by_words(str_to_transform):
    words = str_to_transform.split()
    new_words = []
    for word in words:
        new_word = random_word_transformation(word)
        new_words.append(new_word)
    return " ".join(new_words)


# print(__name__)

if __name__ == "__main__":
    result = generate_string()
    result = transformation_with_spaces(result)
    result = transform_by_words(result)
    print(result)

    # Функции сортировки!

    my_list = [2, 4, 1, 5, -3]
    new_list = sorted(my_list, key=abs)
    print(new_list)

    my_list_2 = ["qwe", "as", "123zzz"]
    new_list_2 = sorted(my_list_2, key=len)
    print(new_list_2)

    my_list_3 = [{"name": "Joh", "age": 25},
                 {"name": "Jucz", "age": 15},
                 {"name": "Jack", "age": 45}]


    def sort_by_age(person):
        age = person["age"]
        return age


    def sort_by_name_alphabet(person):
        name = person["name"]
        return name


    def sort_by_name_len(person):
        name = person["name"]
        return len(name), name


    new_list_3 = sorted(my_list_3, key=sort_by_name_len)
    print(new_list_3)

    # Регулярные выражения!
    import re

    my_str = "Server response 2003 from 123.0.0.12, Wrong 123-0-0-12"

    pattern = r"[0-9]+"  # все числа из строки
    # pattern = r"\d+"
    pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"  # символ . это один любой символ

    my_str = "Kolobok 235-234 BC"
    pattern = r"\d+"

    result = re.findall(pattern, my_str)
    print(result)
