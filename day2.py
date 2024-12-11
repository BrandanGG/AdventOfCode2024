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
def is_safe_report(arr: list):
    """Check if a report is safe based on updated rules."""
    # Sanitize input and convert to integers
    arr = [int(x) for x in arr if x.strip().isdigit()]
    
    # Determine if strictly increasing or decreasing
    increasing = all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
    decreasing = all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))
    
    # Check level differences
    valid_differences = all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

    return (increasing or decreasing) and valid_differences

def part2():
    #Count safe reports considering the Problem Dampener.
    safe_count = 0
    
    with open('.\\inputs\\day2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Sanitize line and split into levels
            arr = [x.strip() for x in line.split() if x.strip()]
            if is_safe_report(arr):
                # The report is already safe
                safe_count += 1
            else:
                # Check if removing one level makes it safe
                for i in range(len(arr)):
                    modified_report = arr[:i] + arr[i+1:]
                    if is_safe_report(modified_report):
                        safe_count += 1
                        break  # No need to check further for this report
    return safe_count
print(part2())