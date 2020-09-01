
with open("input.txt", "r") as input_file:
    for number_line, line in enumerate(input_file):

        if number_line == 0:
            buyer_size = int(line)

        if number_line == 1:
            count_shoes = int(line)

        if number_line == 2:
            shoes = [int(size) for size in line.split()]

shoes = sorted(shoes)

count = 0
flag = True
count_cycles = 0

while flag:

    flag = False
    # if buyer_size > 99:
    #     break

    for shoe in shoes:

        if count_cycles == 0:

            if buyer_size <= shoe:

                buyer_size = shoe
                count += 1
                flag = True
                break

        else:

            if buyer_size < shoe - 2:

                buyer_size = shoe
                count += 1
                flag = True
                break

    # print(buyer_size, count)
    count_cycles += 1

print(count)
