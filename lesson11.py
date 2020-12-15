# import tools
# from tools import *
from tools import read_json, generate_string, get_slise
# from lesson10 import generate_string
import os

print(__name__)

filename = "Homeworks/data.json"

result = read_json(filename)

print(result)

res = generate_string(10, 3)
res = get_slise([1,2,3,4,5], 10, 3)
print(res)

folder_name = "Homeworks"

files = [file for file in os.listdir(folder_name) if ".json" in file]
# files = [file for file in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, file))]
print(files)
for file in files:
    res = read_json(os.path.join(folder_name, file))
    print(res)