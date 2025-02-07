Project: Minesweeper Game
Description: This Python program implements a console-based Minesweeper game. The game randomly selects a grid file containing bombs ('X') and empty cells ('0').
The grid is processed to calculate adjacent bomb counts, and the user interacts with the grid by uncovering cells to win the game without stepping on a bomb.
"""

import random

def read_file(file_name):
    """Reads the grid file and processes it into a 2D list representation."""
    file = open(file_name, "r")
    final_list = []
    for lines in file:
        if len(lines.split(",")) != 1:
            words = lines.strip("\n").split(",")
            list = []
            for word in words:
                if word.strip() == '1':  # Convert bomb cells marked as '1' to 'X'
                    list.append("X")
                else:
                    list.append(word.strip())    
            final_list.append(list)
    file.close()
    return final_list  

def check(grid, x, y):
    """Checks if the given coordinates (x, y) are within grid boundaries."""
    if x < 0 or x >= len(grid):
        return False 
    elif y < 0 or y >= len(grid[0]):
        return False
    else:
        return True
    
def update_grid(grid): 
    """Updates the grid by replacing '0' cells with their corresponding bomb count."""
    for index in range(len(grid)):
        for index_1 in range(len(grid[index])):
            if grid[index][index_1] == '0':
                total = 0
                for i in range(index-1, index+2):
                    for j in range(index_1-1, index_1+2):
                        if check(grid, i, j) and grid[i][j] == "X":
                            total += 1
                grid[index][index_1] = str(total)  # Store bomb count as string
    return grid     

def make_empty_grid(grid):
    """Creates an empty grid (hidden view for the player)."""
    empty_grid = []
    for sub_list in grid:
        empty_grid.append([" "] * len(sub_list))  # Fill with spaces
    return empty_grid

def print_grid(grid):
    """Prints the grid in a formatted way for user readability."""
    alphabets = {i: chr(97 + i) for i in range(26)}  # Mapping numbers to alphabets
    final = ""
    for index in range(len(grid)):
        final += f"{len(grid)-index-1:2} "
        for cell in grid[index]:
            if cell == " ":
                final += "[ ]"
            elif cell == "X":
                final += "[X]"
            else:
                final += f"[{cell}]"
        final += "\n"
    final += "   " + "  ".join(alphabets[i] for i in range(len(grid[0])))
    return final

def dig(grid, move, user_view):
    """Handles user move, updates the user_view, and reveals cells accordingly."""
    alphabets_1 = {chr(97 + i): i for i in range(26)}
    row = int(move[1:])
    column = alphabets_1[move[0]]
    
    if check(grid, len(grid)-row-1, column):
        if grid[len(grid)-row-1][column] == "X":  # Bomb hit
            user_view[len(grid)-row-1][column] = "X"
            print(print_grid(user_view))
        else:
            for i in range(row-1, row+2):
                for j in range(column-1, column+2):
                    if check(grid, len(grid)-i-1, j) and grid[len(grid)-i-1][j] != "X":
                        user_view[len(grid)-i-1][j] = grid[len(grid)-i-1][j]
            print(print_grid(user_view))
                            
def count_total_moves(grid, user_view):
    """Counts the remaining safe moves for the user to win the game."""
    count = 0
    for index in range(len(grid)):
        for index_1 in range(len(grid[index])):
            if user_view[index][index_1] == " " and grid[index][index_1] != "X":
                count += 1
    return count
        
def determine_game_status(grid, user_view):
    """Determines whether the game is still ongoing or if the player has lost/won."""
    for row in user_view:
        if "X" in row:  # Bomb was hit
            return False
    return count_total_moves(grid, user_view) != 0

def game():
    """Main game loop, handling user input and checking game status."""
    file_number = random.randint(1, 5)
    grid = read_file(f"FILE_{file_number}.txt")
    user_view = make_empty_grid(grid)
    update_grid(grid)
    print(print_grid(user_view))
    
    index = 0 
    while index < 10 and determine_game_status(grid, user_view):
        step = input("Enter your move (e.g., a3, b5): ").lower()
        
        if len(step) < 2 or step[1] not in "0123456789":
            print("Invalid input. You lost a move!")
            continue
        
        row = int(step[1:])
        column = step[0]
        
        if 0 <= row < len(grid) and 0 <= ord(column)-97 < len(grid[0]):
            if user_view[len(grid)-row-1][ord(column)-97] in "1234567890":
                print("This cell is already opened. Choose another.")
            else: 
                dig(grid, step, user_view)
                if not determine_game_status(grid, user_view):
                    break
                print(f"{10-1-index} moves left to win")
                index += 1
        else:
            print("Invalid input. You lost a move!")
    
    if index < 10:
        print("BOOM!!! You stepped on a bomb. Better luck next time!")
    else:
        print("\n\nCongratulations! You are a minesweeper!!!")

def start_game():
    """Starts the Minesweeper game and allows the player to restart after finishing."""
    print("Let's Go!")
    input("Press enter to start the game: ")
    answer = "yes"
    while answer == "yes":
        game() 
        answer = input('If you want to play another game, type "yes", else type "no": ')

start_game()
