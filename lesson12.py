import requests

url = "http://api.forismatic.com/api/1.0/"
params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
r = requests.get(url, params=params)
quote = r.json()
quote_text = quote["quoteText"]
quote_author = quote["quoteAuthor"]
print(quote_author)













# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_list_3 = [-10, -20]
#
# result = [(my_list_1[index], my_list_2[index], my_list_3[index])
#           for index in range(min(len(my_list_1), len(my_list_2), len(my_list_3)))]
# print(result)
#
# value = list(zip(my_list_1, my_list_2, my_list_3))
# print(value)
# import os
#
# def create_join_path(folder, file):
#     return f"{folder}/{file}"
#
# folders = ["tmp", "text", "test", "home"]
# files = os.listdir("Homeworks")
#
# for item in list(zip(folders, files)):
#     result = create_join_path(*item)
#     print(result)

