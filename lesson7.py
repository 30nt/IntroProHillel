# Словари

alphabet = {chr(index): index for index in range(ord('a'), ord('z') + 1)}

alphabet["a"] = 98
print(alphabet)
my_str = "this is string"

print("!!!!!!!", 100 in alphabet)

new_str = ''
for symbol_key in my_str:
    # print(symbol, symbol in alphabet)
    if symbol_key in alphabet:
        new_str += str(alphabet[symbol_key])
    else:
        new_str += symbol_key
print(new_str)

invert_alphabet = {alphabet[key]: key for key in alphabet}
# invert_alphabet = {value: key for key, value in alphabet.items()}

print(invert_alphabet)

# Модули (библиотеки)

import string

print(string.ascii_lowercase)











# Функции (начало)