# Count the difference between each index in 2 lists sorted from lowest to highest return the sum
def part1() -> int:
    arr1, arr2 = [],[]
    with open (".\\inputs\\day1.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line.strip
            x = line.split()
            arr1.append(int(x[0]))
            arr2.append(int(x[1]))
    return sum(abs(a - b) for a, b in zip(sorted(arr1), sorted(arr2)))
print(part1())

# Count the frequency of each number in the first list and multiply it by the number in the second list with the same frequency
def part2() -> int:
    arr1, arr2 = [],[]
    with open (".\\inputs\\day1.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            line.strip
            x = line.split()
            arr1.append(int(x[0]))
            arr2.append(int(x[1]))
    test = 0
    for x in arr1:    
        if x in arr2:
            test += (x*arr2.count(x))
    return test
print(part2())