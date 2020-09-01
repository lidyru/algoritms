
with open("data/sort_input.txt", "r") as input_file:
    input_data = [line for line in input_file]

input_array = [int(element) for element in input_data[1].split()]
out_array = list()
max_integer = 10000

array_with_counters = [0 for _ in range(max_integer*2 + 2)]

for element in input_array:
    array_with_counters[element + max_integer] += 1

for index, element in enumerate(array_with_counters):

    for _ in range(element):

        out_array.append(index - max_integer)

print(" ".join([str(element) for element in out_array]))
