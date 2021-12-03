import numpy as np

with open('/Users/andrewemmett/Projects/adventofcode/2020/day9input.txt') as file:
    data = file.readlines()
    data = [int(line.strip()) for line in data]

def find_fault(data):
    
    # for each element in data starting at 26th element
    for i in range(len(data)):
        if i < 25:
            continue
        number = data[i]
        
        # make preamble of previous 25 elements
        preamble = np.array(data[(i-25):i])
        # make set to hold combos
        combos = set()
        
        for element in preamble:
            combos.update(element + preamble)

        #check if number in combo set
        if number not in combos:
            return number
    return 'No faults'


def break_key(key, data):
    for i in range(len(data)):
        row = i
        attempt = []
        while sum(attempt) < key and row < len(data):
            attempt.append(data[row])
            row += 1
        if sum(attempt) == key:
            return (min(attempt) + max(attempt))
        else:
            continue

print(break_key(find_fault(data), data))