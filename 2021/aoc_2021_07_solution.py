import numpy as np
from numpy.lib.type_check import real
test_input = '''16,1,2,0,4,2,7,1,2,14'''
real_data_file = '/Users/andrewemmett/Projects/adventofcode/2021/data/aoc_2021_07.data'

def day_7_part_1(input_file):
    with open(input_file, 'r') as file:
        line = file.read()
    data = np.array(line.split(','), dtype=int)
    middle = np.median(data)
    print(int(np.median(data)), int(np.mean(data)))
    sum_moves = data - middle
    return np.sum(np.abs(sum_moves), dtype=int)

#print(day_7_part_1(real_data_file))



def read_file(input_file):
    with open(input_file, 'r') as file:
        data = file.read()
    return data

def triangle(n):
    return n*(n+1)//2

def day_7_part_2(input_file):
    best = 999999999999
    for mid in range(440,450):
        data = np.array(input_file.split(','), dtype=int)
        middle = int((np.mean(data)))
        abs_moves = np.abs(data - mid)
        triangle_moves = np.apply_along_axis(triangle, 0, abs_moves)
        print(np.sum(triangle_moves), mid)
        if np.sum(triangle_moves) < best:
            best = np.sum(triangle_moves)
    return best
print(day_7_part_2(test_input))
print(day_7_part_2(read_file(real_data_file)))

