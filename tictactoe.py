#list of things to do
#error check and V
#set up win conditions, need diagonal and vertical



def print_board(game_board):                                                                #prints board, super simple
    index = 0                                                                               # 1 2 3                 BOARD LAYOUT
    for places in play_board:                                                               # 4 5 6    
        print('|' + places, end='|')                                                        # 7 8 9
        index += 1
        if index % 3 == 0 and index < 9:
            print("\r")
        

def player_command(player, game_board):                                                     #takes in player input and puts into the board
    print("Player, please enter your input.")
    user_input = input("Enter a spot on the board from 1-9 > " )
    while( int(user_input) < 1 or int(user_input) > 9):
        user_input = input("Error, please enter another place, this one is out of range > ")# this error check is to secure valid in put (numbers less than 0 or over 9)

    while(game_board[int(user_input) - 1] != '-'):
        user_input = input("Error, please enter another place, this one has been taken > ") #simple error check for putting in the same area
    
    game_board[int(user_input) - 1] = player

    return game_board

def condition_one(win_condition, game_board):
    full_board = 0
    for places in game_board:                                                               #win condition if the board is full
        if places != '-':
            full_board += 1
        if full_board == len(game_board):
            print_board(game_board)
            print("\nBoard is full, stalemate!")
            win_condition = True
            return win_condition

    if game_board[0:3] == ['x'] * 3 or game_board[0:3] == ['o'] * 3:                        #win condition for places 1-3
        print_board(game_board)
        print("\nWe have a winner!!!!")
        win_condition = True
        return win_condition
    else:
        pass

    if game_board[3:6] == ['x'] * 3 or game_board[3:6] == ['o'] * 3:                        #win condition for places 4-6
        print_board(game_board)
        print("\nWe have a winner!!!!")
        win_condition = True
        return win_condition
    else:
        pass

    if game_board[6:9] == ['x'] * 3 or game_board[6:9] == ['o'] * 3:                        #win condition for places 7-9
        print_board(game_board)
        print("\nWe have a winner!!!!")
        win_condition = True
        return win_condition
    else:
        pass

    if game_board[0] != '-':
        if game_board[0] == game_board[4] and game_board[4] == game_board[8]:                        #win condition for places 1,5,9
            print_board(game_board)
            print("\nWe have a winner!!!!")
            win_condition = True
            return win_condition
        else:
            pass

    if game_board[2] != '-':
        if game_board[2] == game_board[4] and game_board[4] == game_board[6]:                        #win condition for places 3,5,7
            print_board(game_board)
            print("\nWe have a winner!!!!")
            win_condition = True
            return win_condition
        else:
            pass

    if game_board[0] != '-':
        if game_board[0] == game_board[3] and game_board[3] == game_board[6]:                        #win condition for places 1,4,7
            print_board(game_board)
            print("\nWe have a winner!!!!")
            win_condition = True
            return win_condition
        else:
            pass

    if game_board[1] != '-':
        if game_board[1] == game_board[4] and game_board[4] == game_board[7]:                        #win condition for places 2,5,8
            print_board(game_board)
            print("\nWe have a winner!!!!")
            win_condition = True
            return win_condition
        else:
            pass

    if game_board[2] != '-':
        if game_board[2] == game_board[5] and game_board[5] == game_board[8]:                        #win condition for places 3,6,9
            print_board(game_board)
            print("\nWe have a winner!!!!")
            win_condition = True
            return win_condition
        else:
            pass


def win_diagonal(win_condition,game_board):                                                  # diagonal = /
    pass                    

def replay(replay_condition):
    user_choice = input("Would you like to play again? [y/n] > ")
    user_choice.lower()
    if user_choice == 'y':
        replay_condition = False
        return replay_condition
    elif user_choice == 'n':
        replay_condition = True
        return replay_condition
    else:
        print("Error, invalid input, the game will now end.")
        replay_condition = True
        return replay_condition

def reset_board(game_board):
    game_board.clear()
    new_board = ['-'] * 9  
    return new_board   

    
play_board = ['-'] * 9                                                                      #creates playboard
win_condition = False                                                                       #sets up while loop for win condition, no do whiles in python ):
replay_condition = False
turns = 0

print("Welcome to tictactoe!\r")
print("Decide who is going to be Player 1 and Player 2")
player1 = input("Player 1, do you want to be X or O > ")
player1 = player1.lower()
if player1 == 'x':
    print("Player 1 has selected x, Player 2 will be o")
    player2 = 'o'
elif player1 =='o':
    print("Player 1 has selected o, Player 2 will be x")
    player2 = 'x'

while(True):

    win_condition = condition_one(win_condition,play_board)
    if win_condition == True:
        if replay(replay_condition) == True:
            break
        elif replay_condition == False:
            print(f"Game is reset!")
            play_board = reset_board(play_board)

    print_board(play_board)
    if turns % 2 == 0:
        print(f"\n\nIt is Player {player1.upper()}'s turn.")
        player_command(player1,play_board)
    else:
        print(f"\n\nIt is Player {player2.upper()}'s turn.")
        player_command(player2,play_board)
    
    turns += 1
    print('\r')


    


