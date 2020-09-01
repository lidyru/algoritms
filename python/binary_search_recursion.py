
from random import randint


def binary_search(array, start_index, end_index, number):

    middle = start_index + (end_index - start_index) // 2

    if array[middle] == number:
        return middle

    elif array[middle] > number:
        return binary_search(array, start_index, middle - 1, number)

    else:
        return binary_search(array, middle + 1, end_index, number)


start_array = list(range(1000))
start_number = randint(1, 1000)

print(f"Year number is: {binary_search(start_array, 0, len(start_array) - 1, start_number)}")
