# This is a basic Tic Tac Toe game where the player plays against the computer

import random

def main():
    display_ui()
    player_turn()
    check_victory()
    player_victory()

# Starts new game
gameStillOn = True
playerWins = False
computerWins = False

def newGame():
    global gameStillOn

    if not gameStillOn:
        print("New Game!")
        ui = ["-", "-","-","-","-","-","-","-","-"]
        display_ui()
        player_turn()
        gameStillOn = True



# Tic Tac Toe UI
ui = ["-", "-","-","-","-","-","-","-","-"]

# Displays Tic Tac Toe board
def display_ui():
    print(" | " + ui[0] +" | " + ui[1] +" | " + ui[2] + " | ")
    print(" | " + ui[3] +" | " + ui[4] +" | " + ui[5] + " | ")
    print(" | " + ui[6] +" | " + ui[7] +" | " + ui[8] + " | ")



# Player Turn
def player_turn():
    print("Your Turn!")
    choice = input("Choose a spot from 1 - 9: ")
    # Players move
    


    # Input validation code based off of https://www.youtube.com/watch?v=BHh654_7Cmw
    validMove = False
    while not validMove: 
        while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            choice = input("Choose a spot from 1 - 9: ")
            
        choice = int(choice) - 1
        
        if ui[choice] == "-":
            validMove = True
        else:
            print("Ooops, that spot is filled. Pick another")
    
    
    ui[choice] = "X"
    display_ui()
    check_victory()
    player_victory()
    computer_victory()
    tie()
    computer_turn()

# Computer Turn 
def computer_turn():
    print("Computers Turn!")
    
    choice = random.randint(0, 8)
    markO = choice

    ui[markO] = "O"
    display_ui()
    check_victory()
    player_victory()
    computer_victory()
    tie()
    player_turn()


# Check victory
def check_victory():
    global playerWins
    global computerWins
    
    row_1 = ui[0] == ui[1] == ui[2] == "X"
    row_2 = ui[3] == ui[4] == ui[5] == "X"
    row_3 = ui[6] == ui[7] == ui[8] == "X"
    column_1 = ui[0] == ui[3] == ui[6] == "X"
    column_2 = ui[1] == ui[4] == ui[7] == "X"
    column_3 = ui[2] == ui[5] == ui[8] == "X"
    diagonal_1 = ui[0] == ui[4] == ui[8] == "X"
    diagonal_2 = ui[2] == ui[4] == ui[6] == "X"
    
    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2:
        playerWins = True
        return playerWins


    
    com_row_1 = ui[0] == ui[1] == ui[2] == "O"
    com_row_2 = ui[3] == ui[4] == ui[5] == "O"
    com_row_3 = ui[6] == ui[7] == ui[8] == "O"
    com_column_1 = ui[0] == ui[3] == ui[6] == "O"
    com_column_2 = ui[1] == ui[4] == ui[7] == "O"
    com_column_3 = ui[2] == ui[5] == ui[8] == "O"
    com_diagonal_1 = ui[0] == ui[4] == ui[8] == "O"
    com_diagonal_2 = ui[2] == ui[4] == ui[6] == "O"

    if com_row_1 or com_row_2 or com_row_3 or com_column_1 or com_column_2 or com_column_3 or com_diagonal_1 or com_diagonal_2:
        computerWins = True
        return computerWins






# Player Wins
def player_victory():
    global gameStillOn

    if playerWins:
        print("Player wins!")
        gameStillOn = False

# Computer Wins
def computer_victory():
    global gameStillOn

    if computerWins:
        gameStillOn = False
        print("Computer wins!")
        



# Tie
def tie():
    global gameStillOn

    if "-" not in ui and not playerWins and not computer_victory:
        gameStillOn = False
        print("Tie!")





main()