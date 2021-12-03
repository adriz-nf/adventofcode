import pandas as pd
import numpy as np

input_file = '/Users/andrewemmett/Projects/adventofcode/2021/data/day3aocd.data'
test_input = '/Users/andrewemmett/Projects/adventofcode/2021/data/day3_test.data'
my_input = '/Users/andrewemmett/Projects/adventofcode/2021/data/day3_my_test.data'

def binary_convert(binary):
    gamma = 0
    epsilon = 0
    for i, x in enumerate(binary[::-1]):
        # decode binary gamma
        gamma += int(x) * 2 ** i
        # handle inverse for epsilon
        if int(x) == 1:
            y = 0
        else:
            y = 1
        epsilon += int(y) * 2 ** i
    return gamma * epsilon

def single_binary_convert(binary):
    int_num = 0
    for i, x in enumerate(binary[::-1]):
        int_num += int(x) * 2 ** i
    return int_num 


def get_gamma(input_file):
    '''returns the binary value for gamma'''
    with open(input_file, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    array = np.array(data).astype(int)    
    return np.ceil(np.median(array, axis=0))


def get_oxygen_rating(input_file):
    with open(input_file, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    bin_array = np.array(data).astype(int)
    for col in range(bin_array.shape[1]):
        key = np.ceil(np.median(bin_array, axis=0)).astype(int)
        for row in range(bin_array.shape[0] -1, -1, -1):
            if bin_array[row,col] != key[col]:
                bin_array = np.delete(bin_array, [row], axis=0)
                if bin_array.shape[0] == 1:
                    return bin_array[0]
    return bin_array[0]

def get_co2_rating(input_file):
    with open(input_file, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    bin_array = np.array(data).astype(int)
    for col in range(bin_array.shape[1]):
        key = np.ceil(np.median(bin_array, axis=0)).astype(int)
        for row in range(bin_array.shape[0] -1, -1, -1):
            if bin_array[row,col] == key[col]:
                bin_array = np.delete(bin_array, [row], axis=0)
                if bin_array.shape[0] == 1:
                    return bin_array[0]
    return bin_array[0]

print(single_binary_convert(get_oxygen_rating(test_input)) * single_binary_convert(get_co2_rating(test_input)))


def get_gamma_pandas(input_file):
    with open(input_file, 'r') as file:
        data = [list(line.strip()) for line in file.readlines()]
    df = pd.DataFrame(data)
    sums = []
    for column in df.columns:
        sums.append(df[column].astype('int32').mode().values[0]) 
    return sums



