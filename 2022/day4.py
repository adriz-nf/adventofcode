def get_data(input_file):
    with open(input_file, 'r') as file:
        return [(line.strip()) for line in file.readlines()]

data = get_data('day4/input')

# spit into 2 elements by ',' L1, L2
#  split each element into first value, second value by '-' ABCD
# L1 A-B
# L2 C-D
# compare 2 ranges
# pair is fully contained:
# IF (A>=C AND B<=D) OR (C>=A AND D<B)
#
# count fully contained

    

def splitter(pair):
        elements = pair.split(sep=",")
        ABCD = [i.split(sep="-") for i in elements]
        AB = list(map(int,ABCD[0]))
        CD = list(map(int,ABCD[1]))
        return AB, CD

def check_inside(AB, CD):
    return ((AB[0]>=CD[0] and AB[1]<=CD[1]) or (CD[0]>=AB[0] and CD[1]<=AB[1]))

def check_overlap(AB, CD):
    return len(set(range(AB[0],(AB[1]+1))).intersection(set(range(CD[0],CD[1]+1)))) > 0


def combo(pair):
    return check_inside(*splitter(pair))

def combo_overlap(pair):
    return check_overlap(*splitter(pair))

def day4(data):
    results = list(map(combo, data))
    print(sum(results))

def day4_2(data):
    results = list(map(combo_overlap, data))
    print(sum(results))

day4(data)
day4_2(data)