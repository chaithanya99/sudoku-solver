import pyautogui as pg
import numpy as np
import time
board=[]

while len(board)<9:
    b=list(input("enter row:"))
    row=[]
    for i in b:
        row.append(int(i))
    board.append(row)
    print("row "+str(len(board))+" is complete")


time.sleep(3)
def solve_board(board):
    next_pos=find_empty(board)
    if(not next_pos):
        return True
    
    row,col=next_pos
    for i in range(1,10):
        if(valid_board(board,(row,col),i)):
            board[row][col]=i
            if solve_board(board):
                return True
            board[row][col]=0
    return False
def valid_board(board,position,number):
    row,col=position
    #rows
    for i in range(len(board[0])):
        if i!=col and board[row][i]==number:
            return False
    #cols
    for i in range(len(board)):
        if(i!=row and board[i][col]==number):
            return False
    #box
    start_row=row//3
    start_col=col//3
    start_row*=3
    start_col*=3
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if((i!=row or j!=col) and board[i][j]==number):
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None
def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("--------------------")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("| ",end="")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ",end="")

def write(board):
    nums=[]
    for row in board:
        for n in row:
            nums.append(str(n))
    counter=0
    for i in nums:
        pg.press(i)
        pg.hotkey('right')
        counter+=1
        if counter%9==0:
            pg.hotkey('down')
            for _ in range(1,9):
                pg.hotkey('left')
solve_board(board)
write(board)
