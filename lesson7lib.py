import random
import string


def create_ip():
    ip = ".".join([str(random.randrange(256)) for _ in range(4)])
    # print("---->", ip_1) # ООООЧЕНЬ плохо
    return ip


def create_list_ip(count: int):
    return [create_ip() for _ in range(count)]

def special_print(*args):
    new_list = []
    for str_ in args:
        if random.randrange(2):
            str_ = str_[::-1]
        new_list.append(str_)
    print(*new_list)

special_print("QWE", "ASD", "ZXC", "wer", "xcvbnmm")


def modified_list(my_list):
    my_list.append(my_list[-1])

new_list = some_list = [1,2,3,4,5]
# new_list  = [1,2,3,4,5]
# some_list = [1,2,3,4,5]
print(new_list == some_list)

modified_list(some_list)
print(new_list == some_list)


rand_value = random.randrange(9, 10)
rand_int = random.randint(9, 10)
print(rand_value, rand_int)

values = [2,4,"66",1,"88","99",10]
rand_choice = random.choice(values)
print(rand_choice)

random.shuffle(values)
print(values)

# плохая практика использовать одинаковые имена в программе и функции
ip_1 = 123
print(ip_1)
ip = create_ip()
print(ip)
print(ip_1)

count_ip = 5
ip_1 = ".".join([str(random.randrange(256)) for _ in range(4)])
ip_2 = ".".join([str(random.randrange(256)) for _ in range(4)])
ip_3 = ".".join([str(random.randrange(256)) for _ in range(4)])
ip_list_1 = [".".join([str(random.randrange(256)) for _ in range(4)]) for _ in range(count_ip)]


count_ip = 5
count_ip_server = 10

ip_list_client = create_list_ip(count_ip)
ip_list_server = create_list_ip(count_ip_server)
print(ip_list_server)
