from random import randint
# ❌ 💥 🌊 🚢
# https://github.com/Thibaud-Mathis/BattleShip
# ["1A", "1B ", ... x8], [" ", " ", ... x8], ...x8
#Boards for holding ship locations
AI_HIDDEN_BOARD = [["  "] * 8 for x in range(8)]
PLAYER_HIDDEN_BOARD = [["  "] * 8 for x in range(8)]
# Boards for displaying hits and misses
AI_GUESS_BOARD = [["🌊"] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [["🌊"] * 8 for i in range(8)]

def print_board(board):
    print("   A   B   C   D   E   F   G   H")
    row_number = 1
    for row in board:
        print("%d|%s |" % (row_number, " |".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
numbers_to_letters = {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H'
}
#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "🚢":
            ship_row, ship_column = get_user_guess()
        board[ship_row][ship_column] = "🚢"

def get_user_guess():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "💥":
                count += 1
    return count

def dispay_interface():
    print('Boats left: ' + str(5 - count_hit_ships(AI_HIDDEN_BOARD)))
    print("You have " + str(turns) + " bullets left")
    print('Guess a battleship location')
    print("--------- 🤖 AI board 🤖 ----------")
    print_board(AI_GUESS_BOARD)
    print("====================================")
    print("-------- 👑 Your board 👑 ---------")
    print_board(PLAYER_HIDDEN_BOARD)
     
def handle_turn(guessBoard, hiddenBoard, row, column):
    if guessBoard[row][column] == "❌" or guessBoard[row][column] == "💥":
        print("You guessed that one already.")
        return True
    elif hiddenBoard[row][column] == "🚢":
        print("Hit !")
        guessBoard[row][column] = "💥"  
        hiddenBoard[row][column] = "💥"  
    else:
        print("MISS!")
        guessBoard[row][column] = "❌"   
        hiddenBoard[row][column] = "❌"   

if __name__ == "__main__":
    create_ships(PLAYER_HIDDEN_BOARD)
    create_ships(AI_HIDDEN_BOARD)
    turns = 50
    while turns > 0:
        dispay_interface()
        # Player turn
        print("==== YOUR TURN ====")
        row, column = get_user_guess()
        alreadyTried = handle_turn(AI_GUESS_BOARD, AI_HIDDEN_BOARD, row, column)
        # IA turn
        print("==== AI TURN ====")
        ai_row, ai_column = randint(0,7), randint(0,7)
        print("AI guessed " + str(ai_row + 1) + numbers_to_letters[ai_column])
        aiAlreadyTried = handle_turn(PLAYER_GUESS_BOARD, PLAYER_HIDDEN_BOARD, ai_row, ai_column)
        if not alreadyTried or not aiAlreadyTried : turns -= 1

        if count_hit_ships(AI_GUESS_BOARD) == 5:
            print("You win!")
            break
        if count_hit_ships(PLAYER_GUESS_BOARD) == 5:
            print("You lost!")
            break
        if turns == 0:
            print("You lost !")
