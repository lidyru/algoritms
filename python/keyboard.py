
with open("input.txt", "r") as input_file:
    input_data = [line for line in input_file]

max_pressing = [int(pressing) for pressing in input_data[1].split()]
pressings = [int(pressing) for pressing in input_data[3].split()]

for pressing in pressings:
    max_pressing[pressing - 1] -= 1

for button in max_pressing:
    if button < 0:
        print("yes")
    else:
        print("no")
