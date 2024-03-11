import random

win_count = 0
play_count = 0

WIN_NUM = 1
PLAY_NUM = 5
flag = False

# draw M x N board
def draw_board(board): # board is M x N matrix
    print('', end='\t')
    for i in range(len(board[0])):
        print(f'x{i}', end='\t')
    print()  
    for y_idx, y in enumerate(board):
        print(f'y{y_idx}', end='\t')
        for x_idx, x in enumerate(y):
            print(f'{x}', end='\t')
        print()     
           
# make 1-dim win list
def make_1d():
    print('1차원 추첨판 그리기')
    y_axis = int(input('y축 개수>>'))
    x_axis = int(input('x축 개수>>'))
    new_1d_board = [0 for _ in range(y_axis*x_axis)]
    win_num = int(input('당첨 개수>>'))
    win_1d_board = [1 for _ in range(win_num)]
    new_1d_board[0:len(win_1d_board)] = win_1d_board
    random.shuffle(new_1d_board)    
    return new_1d_board

# make 2-dim win list
def make_2d(board):
    print('2차원 추첨판 그리기')
    y_axis = int(input('y축 개수>>'))
    x_axis = int(input('x축 개수>>'))
    if y_axis * x_axis == len(board):
        new_board = [[0 for _ in range(x_axis)] for _ in range(y_axis)]
        for y in range(y_axis):
            for x in range(x_axis):
                new_board[y][x] = board[y*y_axis + x]
        return new_board
    
    else:
        return ValueError

# counting win and play game
def count(num):
    num += 1
    return num    
        
# comparing my point have win number (1 : win, 0 :lose)
def win_compare(win_board, result_board):
    global win_count, play_count
    my_xpoint = int(input('x좌표 >>'))
    my_ypoint = int(input('y좌표 >>'))

    if win_board[my_ypoint][my_xpoint] == 1:
        result_board[my_ypoint][my_xpoint] = '당첨'
        win_count = count(win_count)
    else:
        result_board[my_ypoint][my_xpoint] = '꽝'
    
    play_count = count(play_count)
    return result_board   

# check win or lose
def win_or_lose():
    global flag
    if win_count == WIN_NUM:
        print('승리')
        flag = True
        return
    if play_count == PLAY_NUM:
        print('패배')
        flag = True
        return

# main
if __name__ == '__main__':
    win_list = make_1d()
    win_list = make_2d(win_list)
    draw_board(win_list)
    result_list = [['추첨' for _ in range(len(win_list[0]))] for _ in range(len(win_list))]
    while not flag:
        result_list = win_compare(win_list, result_list)
        draw_board(result_list)
        win_or_lose()