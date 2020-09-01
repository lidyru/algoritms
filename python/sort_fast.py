
from random import choice

with open("data/sort_input.txt", "r") as input_file:
    input_lines = [line for line in input_file]

input_array = [int(number) for number in input_lines[1].split()]
empty_set = set()


def quik_sort(array: list, bearing_elements: set):

    smaller = list()
    more = list()

    bearing_element = choice(list(set(input_array) - bearing_elements))
    bearing_elements.add(bearing_element)

    for element in array:
        if element <= bearing_element:
            smaller.append(element)
        else:
            more.append(element)

    smaller.extend(more)
    array = smaller

    if bearing_elements == set(array):
        return array

    return quik_sort(array, bearing_elements)


sorted_array = quik_sort(input_array, empty_set)
print(" ".join([str(element) for element in sorted_array]))
