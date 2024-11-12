from random import randint, random
from typing import Union


def rand_with_log_density(num_digits: Union[float, tuple[float, float]]):
    if isinstance(num_digits, tuple):
        (min_num_digits, max_num_digits) = num_digits
    else:
        (min_num_digits, max_num_digits) = (0, num_digits)
    assert min_num_digits <= max_num_digits
    num = 0
    while num < 10 ** min_num_digits:
        num = round(10 ** (random() * max_num_digits))
    return num
