import random
from Tkinter import *
import time


top = Tk()
frame = Frame(top,height=0,width=200)
#frame.bind("<Key>",key)
C = Canvas(top,height=400,width=200)
C.pack()
#frame.pack()

def create_board(width,height):
    return [[False] * width for _ in range(height)]

def lose(board):
    for col in board[1]:
        if col:
            return True
    return False

def draw_board(board):
    C.delete('all')
    y = 0
    for row in board:
        x = 0 
        for col in row:
            if col:
                C.create_rectangle(x,y,x+20,y+20,fill='black')
            x += 20
        y += 20


def print_board(board):
    for row in board:
        for col in row:
            if col:
                print 'X',
            else:
                print '_',
        print ''
    print ''

def gravity(board):
    y = len(board)-1
    while y > 0:
        x = len(board[0])-2
        while x > 0:
            if board[y-1][x] and not board[y][x]:
                print str(x) + ' ' + str(y)
                board[y-1][x] = False
                board[y][x] = True
            x -= 1
        y -= 1
    return board

def fall(board, current):
    y = len(board) - 2
    while y > 0:
        x = len(board[0]) - 1
        while x > 0:
            if board[y][x] and current[y][x]:
                current[y+1][x] = board[y+1][x] = True
                current[y][x] = board[y][x] = False
            x -= 1
        y -= 1
    return board

def check_clear_line(board):
    y = len(board) - 1
    while y > 0:
        x = 0
        for row in board[y]:
            if row:
                x += 1
        if x == len(board[0]):
            board[y] = [False] * len(board[0])
            board = gravity(board)
            y += 1
        y -= 1
    return board
            

def is_falling(board,current):
    print current
    y = len(board) - 1
    while y > 0:
        x = 0
        while x < len(board[0]):
            if current[len(board) - 1][x]:
                return False
            elif current[y][x] and board[y+1][x] and not current[y+1][x]:
                return False
            x += 1
        y -= 1
    return True

def valid_left(board,current):
    y = len(board) - 1
    while y > 0:
        x = 0
        while x < len(board[0]) - 1:
            if current[y][x] and board[y][x-1] and not current[y][x-1]:
                return True
            x -= 1
        y -= 1
    return False

def valid_right(board,current):
    y = len(board) - 1
    while y > 0:
        x = len(board[0]) - 1
        while x > 0:
            if current[y][x] and board[y][x+1] and not current[y][x+1]:
                return True
            x -= 1
        y -= 1
    return False

def move_left(board,current):
    pass

def move_right(board,current):
    pass

def key(event):
    print 'pressed', repr(event.char)

def callback(event):
    frame.focus_set()
    print 'clicked at', event.x, event.y
    

def add_piece(board):
    current = create_board(len(board[0]),len(board))
    pieces = ['line','T','L','RevL','squiggle','Revsquiqqle','box']
    picked = random.choice(pieces)
    center = len(current[0]) / 2
    if picked == 'line':
        for i in [center - 2, center - 1, center, center + 1]:
            current[1][i] = True
            board[1][i] = True
    elif picked == 'T':
        for i in [center - 2, center - 1, center]:
            current[1][i] = True
            board[1][i] = True
        current[2][center - 1] = True
        board[2][center - 1] = True
    elif picked == 'L' or picked == 'RevL':
        for i in [center - 2, center - 1, center]:
            current[1][i] = True
            board[1][i] = True
        if picked == 'L':
            current[2][center] = True
            board[2][center] = True
        else:
            current[2][center - 2] = True
            board[2][center - 2] = True
    elif picked == 'squiggle' or picked == 'Revsquiggle':
        for i in [center - 1, center]:
            current[1][i] = True
            board[1][i] = True
        if  picked == 'squiggle':
            for i in [center - 2, center - 1]:
                current[2][i] = True
                board[2][i] = True
        else:
            for i in [center, center + 1]:
                current[2][i] = True
                board[2][i] = True
    elif picked == 'box':
        for i in [1, 2]:
            for j in [center - 1, center]:
                current[i][j] = True
                board[i][j] = True
    return current

frame.bind('<Key>',key)
frame.bind('<Button-1>', callback)
frame.pack()

difficulty = .2
board = create_board(10,20)
current = add_piece(board)
fall(board,current)
while not lose(board):
    board = check_clear_line(board)
    if not is_falling(board,current):
        current = add_piece(board)
    fall(board,current)
    draw_board(board)
    top.update()
    time.sleep(difficulty)
top.mainloop()
