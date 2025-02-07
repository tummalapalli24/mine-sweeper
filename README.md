# mine-sweeper

Minesweeper Game Instructions:
Objective:
Uncover all the squares on the grid that do not contain mines without
being "blown up" by clicking on a square with a mine underneath.

Gameplay:

The game board consists of a grid of squares. Some squares contain mines
(designated by "X"), while others are empty.
The size of the grid is determined by the number entered at the start of the game.
This number indicates the dimensions of the square grid 
(e.g., entering '5' would result in a 5x5 grid).
Each square can be in one of three states:
Covered: Initially, all squares are covered.
Uncovered: When a square is clicked on, it reveals what's underneath.
Flagged: Players can flag squares they suspect contain mines to avoid accidental clicking.
The game starts with an empty grid, and the player's goal is to uncover all the squares without clicking on any with mines.
To uncover a square, the player inputs a move in the format <letter><number>, where <letter> represents the column (from A to Z) and <number> represents the row (from 1 to the grid's height).
If the uncovered square contains a mine, the game ends, and the player loses.
If the uncovered square does not contain a mine, it reveals a number indicating the total number of mines adjacent to that square (in the eight neighboring squares).
If an uncovered square has no adjacent mines, it recursively uncovers its neighboring squares until squares with adjacent mines are reached.
The game continues until either all non-mine squares are uncovered (player wins) or the player uncovers a square with a mine (player loses).
The game has a maximum limit of 10 moves to prevent infinite loops.
Controls:

Use keyboard input to enter your moves.
Enter the coordinates of the square you want to uncover in the format <letter><number>, e.g., "a1", "b3", "d5", etc.
Type "enter" and press Enter to start the game.
Outcome:

If the player uncovers all non-mine squares without triggering any mines, they win.
If the player uncovers a square with a mine, they lose.
The game also ends if the player reaches the maximum limit of 10 moves without completing the objective.
Note:

Pay attention to the numbers revealed when you click on a square; they indicate the number of mines adjacent to that square and help you strategize your moves.
Use flagging strategically to mark squares you suspect contain mines.
Enjoy playing Minesweeper!
