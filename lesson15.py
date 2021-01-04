import requests
from requests_oauthlib import OAuth1
import os
import time


def time_decorator(some_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = some_function(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return result

    return wrapper


class IconGetter:
    def __init__(self, save_dir="tmp"):
        key = os.environ["KEY"]
        secret = os.environ["SECRET"]
        self.auth = OAuth1(key, secret)
        self.endpoint = "http://api.thenounproject.com/icon"
        self.save_dir = save_dir

    @time_decorator
    def get_and_save_icon(self, id):
        response = requests.get(f"{self.endpoint}/{id}", auth=self.auth)
        res_json = response.json()
        # print(res_json["icon"])
        icon_url = res_json["icon"]["icon_url"]
        img = requests.get(icon_url)
        with open(os.path.join(self.save_dir, f"{id}.svg"), "wb") as file:
            file.write(img.content)


icon_getter = IconGetter()
icon_getter.get_and_save_icon(3)

class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        return f"({self._x0}, {self._y0}, {self._x1}, {self._y1})"

    def get_area(self):
        return (self._x1 - self._x0) * (self._y1 - self._y0)

    def __add__(self, other):
        x0 = min(self._x0, other._x0)
        y0 = min(self._y0, other._y0)
        x1 = max(self._x1, other._x1)
        y1 = max(self._y1, other._y1)
        return Bbox(x0, y0, x1, y1)

    @staticmethod
    def dummy_add_numbers(a, b):
        return a + b

    @property
    def x0(self):
        return self._x0

    @property
    def y0(self):
        return self._y0

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1


bbox_1 = Bbox(1, 1, 3, 3)
bbox_2 = Bbox(1, 2, 4, 5)

bbox_3 = bbox_1 + bbox_2

# print(bbox_3.y1)
res = bbox_3.dummy_add_numbers(3, 3)
print(res)
