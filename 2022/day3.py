from itertools import islice
input = 'day3/input'

string = "vJrwpWtwJgWrhcsFMMfFFhFp"

def convert(letter):
    '''convert letter to number priority '''
    letter_map = {chr(i) : (i-96) for i in range(97,123)}
    letter_map.update({chr(i) : (i-38) for i in range(65,91)})
    return letter_map[letter]

def splitter(string):
    '''# split string in half in middle and return intersection of sets'''
    h1 = set(string[0:int(len(string)/2)])
    h2 = set(string[int(len(string)/2):])
    item = h1.intersection(h2).pop()
    return item

def split_convert(line):
    return convert(splitter(line))


def day3(input_file):
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]
    
    sum_of_priority = 0
    for line in data:
        item = splitter(line)
        sum_of_priority += convert(item)
    print(sum_of_priority)


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

def day3_map(input_file):
    '''use map function instead of a loop'''
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]

    list_of_prio = map(split_convert, data)
    return sum(list_of_prio)

def group_splitter(group):
    '''# split string in half in middle and return intersection of sets'''
    h0 = set(group[0])
    h1 = set(group[1])
    h2 = set(group[2]) 
    item = h0.intersection(h2).intersection(h1).pop()
    return item


def group_split_convert(line):
    return convert(group_splitter(line))


def day3_2(input_file):
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]
    
    groups = list(batched(data, 3))
    list_of_prio = map(group_split_convert, groups)
    print(sum(list_of_prio))

day3(input)
day3_2(input)
