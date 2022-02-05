import numpy as np
from aocd import get_data
from aoc_helper import submit_correct
test_input = '3,4,3,1,2'
test_answer = 5934
test_answer_2 = 26984457539

real_data_file = '/Users/andrewemmett/Projects/adventofcode/2021/data/aoc_2021_06.data'


day=6

def read_data(input_file):
    with open(input_file, 'r') as file:
        #data = read_data(real_data_file)#[int(line.strip()) for line in read_data(real_data_file)).split(',')]
        data = file.read()
    return data



# make array with elements
def count_fish(data, days):
    new_school = np.array(data.split(','), dtype=int)
    unique_fish, fish_counts = np.unique(new_school, return_counts=True)
    print(unique_fish)
    for day in range(0,days):
        # new_fish = count elements with value 0
        new_fish = np.count_nonzero(new_school == 0)
        # add new_fish elements of value 8 to array
        new_fish_array = np.full(new_fish, 9, dtype=int)
        bigger_school = np.append(new_school, new_fish_array)
        # any element = 0 adds 7 to itself
        fresh_school = np.where(bigger_school != 0, bigger_school, 7)
        # minus one from each array element
        new_school = fresh_school - 1
    return np.count_nonzero(new_school >-1 )


#print(count_fish(read_data(real_data_file),80))
#print(count_fish(read_data(real_data_file), 80))
#submit_correct(test_answer, count_fish(test_input, 256), count_fish(get_data(day=day), 256))


def breed_fish(x):
    count = x * 2



def read_data_2(input_file):
    with open(input_file, 'r') as file:
        #data = read_data(real_data_file)#[int(line.strip()) for line in read_data(real_data_file)).split(',')]
        data = file.read()
        new_school = np.array(data.split(','), dtype=int)
        unique_fish, fish_counts = np.unique(new_school, return_counts=True)
    return unique_fish, fish_counts

def new_fish(start, days, cycle):
    if days >= 0:
        print('new fish:',max(0,((days + (cycle-start)) // cycle)), 'days:', days)
        return 2*max(1, ((days + cycle-start) // cycle)) * new_fish(8, days-cycle, cycle)
    else:
        #print('new fish:','zero', 'days:', days)
        return 1

print(2**(80//6))

def run_fish(input_file):
    unique_fish, fish_counts = read_data_2(input_file)
    print(unique_fish, fish_counts)
    total = 0
    exp = 0
    print('zero')
    for x, i in enumerate(unique_fish):
        exp += 2**13*fish_counts[x]
        #print(i, 'result', new_fish(i,80,6), 'fish count', fish_counts[x])
        total += new_fish(i,80,6) * fish_counts[x]
        print(total)
    return total , exp

def two_power(exponenet):
    if exponenet > 0:
        return 2*two_power(exponenet-1)
    else:
        return 1

print(run_fish(real_data_file))