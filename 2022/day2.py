input = 'day2/input'
test_input=['A Y','B X','C Z']

results = { "A X":3+1,
            "B Y":3+2,
            "C Z":3+3,
            "A Z":0+3,
            "B X":0+1,
            "C Y":0+2,
            "A Y":6+2,
            "B Z":6+3,
            "C X":6+1}
codes = {   "A":"rock",
            "B":"paper",
            "C":"scissor",
            "X":"rock",
            "Y":"paper",
            "Z":"scissor"}
points = {  "rock":1,
            "paper":2,
            "scissor":3}


coders1 = { "A X":0+3,
            "A Y":3+1,
            "A Z":6+2,
            "B X":0+1,
            "B Y":3+2,
            "B Z":6+3,
            "C X":0+2,
            "C Y":3+3,
            "C Z":6+1,
            }

def score(input,results=results):
    '''takes two moves as out put as single string
        returns value based on combination of values and individual second value'''
    return results[input]


def tday2(input_file):
    #with open(input_file, 'r') as file:
    data = input_file
    total = 0
    for line in data:
        total += score(line,coders1)
    print(total)
    return total


def day2(input_file,results=results):
    with open(input_file, 'r') as file:
        data = [(line.strip()) for line in file.readlines()]
    total = 0
    for line in data:
        total += score(line,results)
    print(total)
    return total
tday2(test_input)
day2(input,coders1)