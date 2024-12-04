#The engineers are trying to figure out which reports are safe. 
#The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
#So, a report only counts as safe if both of the following are true:
#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.
def part1():
    total_valid = 0
    with open ('.\\inputs\\day2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            arr = line.split()
            if arr == sorted(arr, key=int) or arr == sorted(arr, key=int, reverse=True): # if the sorted version matches the list, continue, else, end the iteration
                sortedarr = sorted(arr, key=int)                
                index = 0
                valid = True
                while index < len(sortedarr) -1:
                    diff = int(sortedarr[index+1]) - int(sortedarr[index])
                    if 1 <= diff <= 3:
                        index += 1
                    else:
                        valid = False
                        break
                if valid:
                    total_valid += 1
    return total_valid
print(part1())