import numpy as np
from math import copysign
from aocd import get_data
real_data_file = '/Users/andrewemmett/Projects/adventofcode/2021/data/aoc_2021_05.data'

test_answer = 5
test_answer_2 = ''
test_data = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

#real_data = get_data(day=5)

def day_5_part_1(data):
    #data = [line.replace(',', ' ').split() for line in data.strip().split("\n")]
    #data = [num for row in data.strip().split(' -> ') for num in data.strip().split("\n") ]
    #data = [item for row in data.strip().split("\n") for item in row.strip().split(' -> ') ]
    rows = [row.strip().split(' -> ') for row in data.strip().split("\n")]
    final_points = []
    clean_rows = []
    for row in rows:
        clean_pairs = []
        for pair in row:
            split_pair = pair.split(',')
            xy = (int(split_pair[0]), int(split_pair[1]))
            clean_pairs.append(xy)
        # check for horizontal lines and fill points
        if clean_pairs[0][0] == clean_pairs[1][0]:
            for point in range(max(clean_pairs[0][1],clean_pairs[1][1]) - min(clean_pairs[0][1],clean_pairs[1][1]) +1):
                final_points.append(str((clean_pairs[0][0], min(clean_pairs[0][1],clean_pairs[1][1])+point)))
        # check for vertical lines and fill points
        if clean_pairs[0][1] == clean_pairs[1][1]:
            for point in range(max(clean_pairs[0][0],clean_pairs[1][0]) - min(clean_pairs[0][0],clean_pairs[1][0]) +1):
                final_points.append(str((min(clean_pairs[0][0],clean_pairs[1][0])+point, clean_pairs[0][1])))
    _, counts = np.unique(final_points , return_counts=True)
    return sum(counts > 1)

def day_5_part_2(data):
    rows = [row.strip().split(' -> ') for row in data.strip().split("\n")]
    final_points = []
    clean_rows = []
    for row in rows:
        clean_pairs = []
        for pair in row:
            split_pair = pair.split(',')
            xy = (int(split_pair[0]), int(split_pair[1]))
            clean_pairs.append(xy)
        # check for horizontal lines and fill points
        if clean_pairs[0][0] == clean_pairs[1][0]:
            for point in range(max(clean_pairs[0][1],clean_pairs[1][1]) - min(clean_pairs[0][1],clean_pairs[1][1]) +1):
                final_points.append(str((clean_pairs[0][0], min(clean_pairs[0][1],clean_pairs[1][1])+point)))
        # check for vertical lines and fill points
        if clean_pairs[0][1] == clean_pairs[1][1]:
            for point in range(max(clean_pairs[0][0],clean_pairs[1][0]) - min(clean_pairs[0][0],clean_pairs[1][0]) +1):
                final_points.append(str((min(clean_pairs[0][0],clean_pairs[1][0])+point, clean_pairs[0][1])))
        # check for diagonal l-r lines and fill points
        if abs(clean_pairs[0][0] - clean_pairs[1][0]) == abs(clean_pairs[0][1] - clean_pairs[1][1]):
            for point in range(max(clean_pairs[0][1],clean_pairs[1][1]) - min(clean_pairs[0][1],clean_pairs[1][1]) +1):
                final_points.append(str((clean_pairs[0][0] + int(copysign(point, clean_pairs[1][0] - clean_pairs[0][0])), 
                                         clean_pairs[0][1] + int(copysign(point, clean_pairs[1][1] - clean_pairs[0][1])))))
    _, counts = np.unique(final_points , return_counts=True)
    return sum(counts > 1)
    

if __name__ == '__main__':
    print(day_5_part_2(test_data))

