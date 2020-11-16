value_str = 'qwerFGHtyu23745tubfvacksn3299  //.,io'
value_str_new = value_str.upper()
for symbol in value_str_new:
    if symbol.isalnum():
        print(f"Symbol: {symbol}")
print(value_str, value_str_new)


filename = "my_jdhfbvjhdbvj"
img_jpg = f"{filename}.jpg"
img_png = f"{filename}.png"
img_bmp = f"{filename}.bmp"
print(f"My result: {img_jpg}")



# функция()
# объект.метод()

my_url = "google.com.ua"
res = my_url.find("ua")
new_url = my_url.replace("ua", "kz")
print(new_url)


str_value = input("Введи строку")
template = "df"
if template in str_value:
    print("Такой шаблон есть!")
if str_value.find(template) >= 0:
    print("Такой шаблон есть!")

value = input("Введи целое число")
if value.isdigit():
    int_value = int(value)
    revers_str = str(int_value)[::-1]
    revers_str_clean = str(int(revers_str))
    result = len(revers_str) - len(revers_str_clean)
    print(result)
else:
    print("Это не целое число")

if str(int_value)[-1] == '1':
    print("УРА!!!")
else:
    print('Жаль ((')

print(len(str(int_value)))

str_value = input("Введи строку")
new_str = str_value[0] + str_value[-1]
print(new_str)




########################
my_ip_mask = "255.255.255.0"

print(my_ip_mask[:3])
print(my_ip_mask[100:])
print(my_ip_mask[-5:-3])

print(my_ip_mask[-3:-5:-1])
print(my_ip_mask[3:13:2])

print("Hello!")
value = int(input("Введи целое число"))

if value > 0:
    result = value ** 2
else:
    result = 0
# переменная = знач_если_да if УСЛОВИЕ else знач_если_нет
strange_result = 0 if value < -10 else -1
result = value ** 2 if value > 0 else 0
print(result)

