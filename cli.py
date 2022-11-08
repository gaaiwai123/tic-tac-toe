# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import other_player
from logic import *
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    print_str=print_board(board)
    print(print_str)
    current_player =""
    current_player = input("Who goes first? X or O? ")

    while winner == None:
        move=int(input("Player %s, enter your move: "%current_player))
        if move<1 or move>9:
            print("Invalid move!")
            continue
        flag,board=make_move(board,current_player,move)
        if flag==False:
            print("Invalid move!The position is already occupied!")
            continue
        print_str=print_board(board)
        print(print_str)
        winner=get_winner(board)
        if winner!=None:
            print("Player %s wins!"%winner)
            break
        if check_full(board):
            print("The board is full!")
            break
        current_player=other_player(current_player)

        

