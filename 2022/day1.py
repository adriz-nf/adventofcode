input = 'day1/input'
test_input=['1000','2000','3000','','4000','','','5000','6000','','7000','8000','9000',"",'10000']

10000
# real_input = '/Users/andrewemmett/Projects/adventofcode/2021/day1input.data'

def day1(input_file):
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]
    
    max_value = 0
    running_total = 0
    for line in data:
        if line == "":
            max_value = max(max_value,running_total)
            running_total = 0
        else:
            running_total += int(line)
    return max_value
    
def day1_2(input_file):
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]
    
    total_values = []
    running_total = 0
    for line in data:
        if line == "":
            total_values.append(running_total)
            running_total = 0
        else:
            running_total += int(line)
    total_values.append(running_total)
    total_values.sort(reverse=True)
    return sum(total_values[0:3])

def tday1(input_file):
    data = input_file
    
    max_value = 0
    running_total = 0
    for line in data:
        if line == "":
            max_value = max(max_value,running_total)
            running_total = 0
        else:
            running_total += int(line)
    return max_value

def tday1_2(input_file):
    data = input_file
    total_values = []
    running_total = 0
    for line in data:
        if line == "":
            total_values.append(running_total)
            running_total = 0
        else:
            running_total += int(line)
    total_values.append(running_total)
    total_values.sort(reverse=True)
    return sum(total_values[0:3])

print(tday1_2(input))    
print(day1_2(input))
