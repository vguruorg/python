import random
import time
import sys

def print_board(game_board):
    for row in game_board:
        print(f"{row[0]} | {row[1]} | {row[2]}")


def switch_player(player_turn):
    if (player_turn == 0):
        player_turn = 1
    else:
        player_turn= 0
    return player_turn

def check_all_rows(game_board, player):
    #input player = "x" or "O"
    # return True if any row is all player
    #otherwise return False
    for row in range(len(game_board)): # 0,1,2
        if (game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player) :
            return True
    return False


def check_all_columns(game_board, player):
    # input player = "x" or "O"
    # return True if any columns (verticle) is all player
    # otherwise return False
    for column in range(len(game_board)): # 0,1,2
        if (game_board[0][column] == player and game_board[1][column] == player and game_board[2][column] == player) :
            return True
    return False

def check_all_diags(game_board, player):
    # input player = "x" or "O"
    # return True if any digonal is all player
    # otherwise return False

    if (game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player):
        return True
    if (game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player):
        return True
    return False

def is_winner(game_board, player_turn):
    #return True if player winner
    # otherwise False
    row_result = check_all_rows(game_board, player_turn)
    column_result = check_all_columns(game_board, player_turn)
    diag_result = check_all_diags(game_board, player_turn)
    if (row_result == True or
        column_result == True or
        diag_result == True):
        return True
    return False

def player_choice(game_board):
    while True:
        row = -1
        while row > 2 or row < 0:
            row = int(input("Enter a row(from 0 to 2) : "))
        column = -1
        while column > 2 or column < 0:
            column = int(input("Enter a column(from 0 to 2) : "))    
        if game_board[row][column] == "_":
            break
    return (row, column)

def is_moves_left(game_board):
    for row in range(len(game_board)): 
        for column in range(len(game_board)):
           if game_board[row][column] == "_":
               return True
    return False

def minimax(game_board, depth, is_max):
 
    if(is_winner(game_board, "C") == True):
        score = 10
        return score
    if(is_winner(game_board, "P") == True):
        score = -10
        return score
    if(is_moves_left(game_board) == False):
        score = 0
        return score

    if is_max:
        best_val = -1000
        for row in range(len(game_board)): 
            for column in range(len(game_board)):
                if game_board[row][column] == "_":
                    #print(f"minimax evaluating ({row},{column}) for 'C' is_max={is_max}")
                    game_board[row][column] = "C"
                    move_val = minimax(game_board, depth+1, False)
                    game_board[row][column] = "_"
                    if(move_val > best_val):
                        best_val = move_val
                        #print(f"minimax best score={best_val} for 'C'")
        return best_val-depth        
    else:
        best_val = 1000
        for row in range(len(game_board)): 
            for column in range(len(game_board)):
                if game_board[row][column] == "_":
                    #print(f"minimax evaluating ({row},{column}) for 'P'  is_max={is_max}")
                    game_board[row][column] = "P"
                    move_val = minimax(game_board, depth+1,  True)
                    game_board[row][column] = "_"
                    if(move_val < best_val):
                        best_val = move_val
                        #print(f"minimax best score={best_val} for 'P'")
        return best_val+depth        


def find_best_move(game_board, player_name):
    best_val = -1000
    best_row = -1
    best_col = -1
    for row in range(len(game_board)): 
        for column in range(len(game_board)):
           if game_board[row][column] == "_":
                #print(f"evaluating ({row},{column}) for {player_name}")
                game_board[row][column] = player_name
                move_val = minimax(game_board, 0, False)
                game_board[row][column] = "_"
                if(move_val > best_val):
                    best_val = move_val
                    best_row = row
                    best_col = column

    #print(f"best ({row},{column}) score={best_val} for {player_name}")
    return (best_row, best_col)
'''
def computer_choice(game_board):
    while True:
        row = -1
        while row > 2 or row < 0:
            row = random.randint(0,2)
        column = -1
        while column > 2 or column < 0:
            column = random.randint(0,2)
        if game_board[row][column] == "_":
            break
    return (row, column)
'''

def computer_choice(game_board):
    return find_best_move(game_board,"C")

ttt_board = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

player_name = ["C","P"]
random.seed(time.time())
player_turn = random.randint(0,1)
'''
ttt_board = [
    ["C","P","_"],
    ["P","C","_"],
    ["_","_","_"]
]
ttt_board = [
    ["P","_","C"],
    ["P","C","P"],
    ["_","C","P"]
]

print_board(ttt_board)
(row, column) = computer_choice(ttt_board)
ttt_board[row][column] = "C"
time.sleep(1)
print()
print_board(ttt_board)
sys.exit()
ttt_board = [
    ["C","P","C"],
    ["P","P","C"],
    ["_","C","_"]
]

print_board(ttt_board)
(row, column) = computer_choice(ttt_board)
ttt_board[row][column] = "C"
time.sleep(1)
print()
print_board(ttt_board)
'''

print_board(ttt_board)
while is_moves_left(ttt_board):
    if player_name[player_turn] == "C":
        print("Player turn computer =", player_name[player_turn])
        (row, column) = computer_choice(ttt_board)
    else:
        print("Player turn user =", player_name[player_turn])
        (row, column) = player_choice(ttt_board)

    ttt_board[row][column] = player_name[player_turn]
    print_board(ttt_board)
    time.sleep(1)
    if is_winner(ttt_board, player_name[player_turn]) == True:
        print("Winner is ", player_name[player_turn])
        break
    player_turn = switch_player(player_turn)
else :
    print("Tie")