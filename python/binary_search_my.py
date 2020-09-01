
from random import randint

start_array = range(100)
item = randint(0, 100)


def binary_search(array: list, number: int):

    top_border = len(array)
    bottom_border = 0
