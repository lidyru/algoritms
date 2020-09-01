from pip._vendor.distlib.compat import raw_input

len_array = int(input())
array = [int(el) for el in raw_input().split()]
count = len_array

if len_array == 1:
    print(array[0])

else:
    while count != 0:

        count = 0

        for index in range(len_array - 1):

            if array[index] > array[index + 1]:

                array[index], array[index + 1] = array[index + 1], array[index]
                count += 1

    print(" ".join([str(el) for el in array]))
