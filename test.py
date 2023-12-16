num = 0


with open("day1/day_1_numbers.txt", "r") as f:
    for x in f:
        print(x.strip())
        num += int(x.strip())

print(num)
