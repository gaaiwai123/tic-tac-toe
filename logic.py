# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #check who is the winner
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=None:
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=None:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=None:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=None:
        return board[0][2]
    return None
  

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    else:
        return 'X'
    r
def print_board(board):
    # 1 | 2 | 3
    # ---------
    # 4 | 5 | 6
    # ---------
    # 7 | 8 | 9

    """Prints the given board to the console."""
    print_str=""
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                # print(i*3+j+1,end=" ")
                print_str+=str(i*3+j+1)+" "
            else:
                # print(board[i][j],end=" ")
                print_str+=board[i][j]+" "
            if j<2:
                # print("|",end=" ")
                print_str+="|"+" "
        # print()
        print_str+="\n"
        if i<2:
            # print("---------")
            print_str+="---------"
            print_str+="\n"
    return print_str
    
def make_move(board, player, position):
    """Makes a move on the board for the given player at the given position.
    Returns the new board."""
    position-=1
    
    if board[position//3][position%3]==None:
        board[position//3][position%3]=player
        return True, board
    else:
        return False,board
  
def check_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                return False
    return True
    
