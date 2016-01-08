import random
import Tkinter
import time


top = Tkinter.Tk()
C = Tkinter.Canvas(top,height=200,width=100)
C.pack()


def create_board(width,height):
    return [[False] * width for _ in range(height)]

def lose(board):
    for col in board[0]:
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
                C.create_rectangle(x,y,x+10,y+10,fill='black')
            x += 10
        y += 10


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

def check_clear_line(board):
    y = len(board) - 1
    while y > 0:
        x = 0
        for row in board[y]:
            if row:
                x += 1
        if x == len(board[0]):
            board[y] = [False] * len(board[0])
            #gravity(board)
        y -= 1
    return board
            

def is_falling(board):
    return
    y = 0
    while y < len(board)-2:
        x = 0
        while x < len(board[0])-2:
            if board[y][x] and board[y+1][x]:
                break
    
    

def add_piece(board):
    #pieces = ['line','T','L','RevL','squiggle','Revsquiqqle','box']
    pieces = ['line']
    current = random.choice(pieces)
    if current == 'line':
        board[1][len(board[0]) / 2 - 2] = True
        board[1][len(board[0]) / 2 - 1] = True
        board[1][len(board[0]) / 2] = True
        board[1][len(board[0]) / 2 + 1] = True
    return current


board = create_board(10,20)
add_piece(board)
board[19][0]=True
board[19][1]=True
board[19][2]=True
board[19][7]=True
board[19][8]=True
board[19][9]=True
#print_board(board)
while not lose(board):
    board = check_clear_line(board)
    if not is_falling:
        current = add_piece(board)
    else:
        board = gravity(board)
    #print_board(board)
    draw_board(board)
    top.update()
    time.sleep(1)
top.mainloop()
