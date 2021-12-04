from aocd import get_data, submit

def save_new_data(day, year=2021, data_path='data/'):
    data_filename = f'aoc_{year}_{str(day).zfill(2)}.data'
    try:
        with open(data_path+data_filename, 'x') as file:
            data = get_data(day=day)
            file.write(data)
            data = [line for line in file.readlines()]
    except FileExistsError:
        with open(data_path+data_filename, 'r') as file:
            data = [line for line in file.readlines()]
    finally:
        return data


#test_answer = '''given result'''
#test_data = '''given sample data'''

def solution_func(input_data):
    '''the amazing code of the day, either part a or part b'''
    result = input_data
    return result

def submit_correct(test_answer, test_result, real_result, **kwargs):
    '''This code will check that the code works on the sample data and submit the real result only if assert passes'''
    assert (test_answer == test_result), f"Answer {test_result} doesn't match {test_answer}"
    submit(real_result, **kwargs)


if __name__ == '__main__':
    submit_correct(test_answer, solution_func(test_data), solution_func(get_data()))