from aoc_helper import submit_correct, get_data
import numpy as np

test_answer = 4512
test_answer_2 = 1924
test_data = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 '''



def read(data):
    ''' Takes data input and splits out bingo calls and returns a list of boards'''
    data = [line.replace(',', ' ').split() for line in data.strip().split("\n")]
    bingo_calls = (data.pop(0))
    boards = [data[row+1:row+6] for row in range(0,len(data),6)]
    return boards, bingo_calls

def check_win(board):
    for row in board:
        if len(set(row))==1:
            return True
    for col in range(len(board[0])):
        if len({board[0][col],board[1][col],board[2][col], board[3][col], board[4][col]}) == 1:
            return True
    return False

def sum_board(board):
    sum_flat = 0
    flat = [x for sub in board for x in sub]
    for x in flat:
        try:            
            sum_flat += int(x)
        except:
            continue
    
    return sum_flat

def call_number(boards, call):
    new_boards=[]
    for board in boards:
        new_board = []
        for row in board:
            new_row = ['X' if item == str(call) else item for item in row]
            new_board.append(new_row)
        if check_win(new_board):
            return sum_board(new_board) * int(call)
        new_boards.append(new_board)
    return new_boards

def call_number_part_2(boards, call, scores):
    new_boards=[]
    for board in boards:
        new_board = []
        for row in board:
            new_row = ['X' if item == str(call) else item for item in row]
            new_board.append(new_row)
        if check_win(new_board):
            scores.append(sum_board(new_board) * int(call))
        else:
            new_boards.append(new_board)
    return new_boards, scores


def run_bingo(data):
    boards, bingo_calls = read(data)
    scores = []
    for call in bingo_calls:
        boards, scores = call_number_part_2(boards, call, scores)
    return scores[0]
    #return boards
    

if __name__ == '__main__':
    #submit_correct(test_answer_2, run_bingo(test_data), run_bingo(get_data()))
    print(run_bingo(test_data))
