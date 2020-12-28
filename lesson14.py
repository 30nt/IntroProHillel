# from lesson13 import DemoFiles
# import shutil

# print(dir(DemoFiles))
# path = './tmp'
#
# demo_file = DemoFiles(path)
# print(dir(demo_file))

# shutil.rmtree(path)
#
# demo_file._create_dir()


# class FileWriter:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def generate_data_to_write(self):
#         pass
#
#     def write_file(self):
#         pass
import json


class JsonWorker:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._read_file()

    def _read_file(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def sort(self):
        """This method should implement in child classes"""
        raise Exception ("This method should implement in child classes")

class ListWorker(JsonWorker):
    def __init__(self, filename):
        super().__init__(filename)

    def sort(self):
        return sorted(self.data)

class DictWorker(JsonWorker):
    def __init__(self, filename):
        super().__init__(filename)

    def sort(self):
        sort_data = {}
        keys = list(self.data.keys())
        for key in sorted(keys):
            sort_data[key] = self.data[key]
        return sort_data

class IWorker(JsonWorker):
    def __init__(self, filename):
        super().__init__(filename)

# test_1 = JsonWorker("test1.json")
# test_2 = JsonWorker("test2.json")
#
# print(type(test_1.data))
# print(type(test_2.data))

test_2 = ListWorker("test2.json")
print(test_2.data)
print(test_2.sort())

test_1 = DictWorker("test1.json")
print(test_1.data)
print(test_1.sort())

test_3 = IWorker("test2.json")
print(test_3.sort())