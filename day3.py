import re

def part1():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)" # pattern for mul(x,x) where x is a number between 1-3 digits
    total = 0
    with open('inputs\\day3.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.findall(pattern, line)
            for mul in match:
                total += int(mul[1]) * int(mul[0])
    return total
print(part1())