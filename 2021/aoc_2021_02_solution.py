test_input = '/Users/andrewemmett/Projects/adventofcode/2021/day2sample.data'
real_input = '/Users/andrewemmett/Projects/adventofcode/2021/day2aocd.data'

from aoc_helper import save_new_data, submit_correct

test_data = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
day = 2
data = save_new_data(day)
test_answer_a = 150
test_answer_b = 900

def day2_1(data):
        data = [(line.split()[0], int(line.split()[1])) for line in data]
        x, z = 0, 0
        for i in data:
            if i[0] == 'forward':
                x += int(i[1])
            elif i[0] == 'down':
                z += int(i[1])
            elif i[0] == 'up':
                z -= int(i[1])
        return (x * z)
print(day2_1(data))

def day2_2(data):
    data = [(line.split()[0], int(line.split()[1])) for line in data]
    x, z, aim = 0, 0, 0
    for i in data:
        if i[0] == 'forward':
            x += i[1]
            z += aim * i[1]
        elif i[0] == 'down':
            aim += i[1]
        elif i[0] == 'up':
            aim -= i[1]
    return (x * z)

print(day2_2(test_data))





