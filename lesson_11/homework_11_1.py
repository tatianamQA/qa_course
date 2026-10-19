list_1 = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_numbers(line):
    part = line.split(",")
    numbers = map(int, part)
    return sum(numbers)

for item in list_1:
    try:
        print(sum_numbers(item))
    except ValueError:
        print("Не можу це зробити!")
