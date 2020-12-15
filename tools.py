import json
import random
from typing import List, Tuple


def read_json(filename: str) -> dict:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            result = json.load(file)
        return result
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}


def _create_test_values() -> List[Tuple[int, int]]:
    return [(1, 1), (2, 2), (3, 3)]


def get_slise(some_list, min_limit, max_limit):
    assert min_limit < max_limit, "min >= max"
    return some_list[min_limit: max_limit]


def generate_string(min_limit=100, max_limit=1000) -> str:
    str_len = random.randint(min_limit, max_limit)
    res_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(str_len)]
    return ''.join(res_list)

# print(__name__)
