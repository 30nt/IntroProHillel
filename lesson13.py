# Class Атрибуты
import random
import os
import string


class DemoFiles:
    def __init__(self, path_dir):
        self.path_dir = path_dir
        self.create_dir()

    def create_dir(self):
        try:
            os.mkdir(self.path_dir)
        except FileExistsError:
            pass

    def create_files(self):
        for symbol in string.ascii_lowercase:
            with open(os.path.join(self.path_dir, f"{symbol}.txt"), 'w') as file:
                file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def tanos_click(self):
        tanos_list = os.listdir(self.path_dir)
        tanos_list = list(set(tanos_list))
        for filename in tanos_list[: len(tanos_list) // 2]:
            os.remove(os.path.join(self.path_dir, filename))


path_dir = "alphabet"

demo_files = DemoFiles(path_dir)
# demo_files.create_files()
demo_files.tanos_click()

# class FolderInfo:
#     def __init__(self, path):
#         files = os.listdir(path)
#         self.files = [os.path.join(path, file) for file in files if os.path.isfile(os.path.join(path, file))]
#         self.dirs = [os.path.join(path, file) for file in files if os.path.isdir(os.path.join(path, file))]
#
#
# path = "Homeworks"
# f_info = FolderInfo(path)
# print(f_info.dirs)


# class Point:
#     def __init__(self, x=0, y=0, random_mode=True):
#         self.x = x if not random_mode else random.randint(1, 10)
#         self.y = y if not random_mode else random.randint(1, 10)
#
#     def __str__(self):
#         return f'x={self.x} y={self.y}'
#
#     def __repr__(self):
#         return f"({self.x}; {self.y})"
#
# A = Point(1,2)
# B = Point(3,4)
# C = Point()
#
# print(A.x, B.x)
# print(C)

# triangle = (A, B, C)
# print(triangle)


# class MyClass:
#     number = 1000 # атрибут класса
#     # string = "I'm a string!"
#
#     def __init__(self, number, string):
#         self.number = number
#         self.string = string
#
# # Экземпляр класса
# # MyClass.string = "TEST STRING"
#
# my_class_instance = MyClass(10, "test")
# new_class_instance = MyClass(-10, "test")
#
# print(my_class_instance.number, my_class_instance.string)
# print(new_class_instance.number, new_class_instance.string)
# print(my_class_instance.number == new_class_instance.number)
# print(MyClass.number)
# print(my_class_instance.string)
#
# MyClass.number = 100
# print(my_class_instance.number)
# print(new_class_instance.number)
#
# my_class_instance.number = 12 # атрибут экземпляра класса
# print("my_class_instance.number", my_class_instance.number)
# print("new_class_instance.number", new_class_instance.number)
#
# MyClass.number = 10
# print("my_class_instance.number", my_class_instance.number)
# print("new_class_instance.number", new_class_instance.number)
# # my_class_instance.test = 'TEST'
# # print(my_class_instance.test)
