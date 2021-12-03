test_input = '/Users/andrewemmett/Projects/adventofcode/2021/day1sample.data'
real_input = '/Users/andrewemmett/Projects/adventofcode/2021/day1input.data'



def day1(input_file):
    with open(input_file, 'r') as file:
        data = [int(line.strip()) for line in file.readlines()]

    # loop through values checking previous value

    changes = []
    base = None
    for i in data:
        if base == None:
            changes.append(False)
            base = i
        else:
            changes.append(i > base)
            base = i
    return sum(changes)




def day1_part2(input_file):
    with open(input_file, 'r') as file:
        #data = file.readlines()
        data = [int(line.strip()) for line in file.readlines()]
    #print(data)
    changes = []
    base0 = 0
    base1 = 0
    base2 = 0
    for i in data:
        if base2== 0:
            base2 = base1
            base1 = base0
            base0 = i
        else:
            prev = base0 + base1 + base2
            current = i + base0 + base1
            changes.append(current > prev) 
            base2 = base1
            base1 = base0
            base0 = i
    return (changes)

def day1_2_better(input_file):
    with open(input_file, 'r') as file:
        data = [int(line.strip()) for line in file.readlines()]

    counter = 0
    for i in range(len(data)-3):
        if (sum(data[i:i+3]) < sum(data[i+1:i+4])):
            counter +=1
    return counter

def day1_best(input_file,interval=3):
    with open(input_file, 'r') as file:
        data = [int(line.strip()) for line in file.readlines()]
    return sum([ sum(data[i:i+interval]) < sum(data[i+1:i+1+interval]) for i in range(len(data)-interval)])


print(day1_best(real_input, 3))