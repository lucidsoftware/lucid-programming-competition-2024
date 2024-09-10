from random import randint, random


def rand_with_log_density(max_num_digits: float):
    maximum = round(10 ** (random() * max_num_digits))
    return randint(1, maximum + 1)
