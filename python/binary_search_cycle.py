
from random import randint

array = list(range(100))
item = randint(0, 100)
first = 0
last = 100
number = 999
print(item)
print()

found = False

while first <= last and not found:
    midpoint = (first + last)//2

    if array[midpoint] == item:
        found = True
        number = array[midpoint]
    else:
        if item < array[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    print(first, last)

print(number)
