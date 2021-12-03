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


def test_get_func(**kwargs):
    print(kwargs)

def submit_correct(test_func, test_answer, test_result, real_result, **kwargs):
    assert (test_answer == test_result), f"Answer {test_result} doesn't match {test_answer}"
    test_func(real_result, **kwargs)
    #submit(real_result, **kwargs)

#submit_correct(test_get_func)

def test_func(func, **kwargs):
    print(func(kwargs))


if __name__ == '__main__':
    print(test_func(test_get_func(help='help')))