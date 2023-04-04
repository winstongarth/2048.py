# 2048.py
Text-based 2048 game in python
Game Menu
You will then see "Welcome to 2048", and "Press ENTER to continue!". 
You may press your enter button to proceed to the game.
Please wait a while until you see "Complete!" and the game will be loaded.
You will see menu bar, which consists of:
"2048
1. Game Instruction
2. Play
3. Exit
Choose (1-3): "
 - Enter "1" to read the game instruction
 - Enter "2" to play the game
 - Enter "3" to exit the game
After you input your option, you may press enter button to continue.

If you enter "1", you will see the game instructions, and you may press enter button to go back to the menu bar.
If you enter "2", you will see 4 options:
 - Enter "1" for 3x3 grid size game.
 - Enter "2" for 4x4 grid size game
 - Enter "3" for 5x5 grid size game
 - Enter "4" to go back to the menu bar.
If you enter "4", you will then see "Thank you for playing!", and you have exitted the game.

After you choose the grid size, you will be ask to choose the difficulty level:
If you enter "1", you will need to reach 256 points to win (easy).
If you enter "2", you will need to reach 512 points to win (medium).
If you enter "3", you will need to reach 1024 points to win (hard).
If you enter "4", you will need to reach 2048 points to win (original).

How to Play the Game
1. There are 3 choices of grid; 3*3 grid, 4*4 grid, and 5x5 grid.
  1. 3x3 Grid
      ┏━━━━━┳━━━━━┳━━━━━┓
      ┃     ┃    2┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃    4┃
      ┣━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃
      ┗━━━━━┻━━━━━┻━━━━━┛
    2. 4x4 Grid
      ┏━━━━━┳━━━━━┳━━━━━┳━━━━━┓
      ┃     ┃    2┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃    4┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃     ┃
      ┗━━━━━┻━━━━━┻━━━━━┻━━━━━┛

  3. 5x5 Grid
      ┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
      ┃     ┃     ┃     ┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃    4┃     ┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃    2┃     ┃     ┃
      ┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫
      ┃     ┃     ┃     ┃     ┃     ┃
      ┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛
2. The grid can be filled with any number. Initially two random cells are filled with either 2 or 4 in it. The rest of the cells are empty.
3. When you see “Move (W, A, S, D):”
 - Enter "W" to move the number up.
 - Enter "A" to move the number left.
 - Enter "S" to move the number down.
 - Enter "D" to move the number right.
4. When you press any key, all the elements of the cell move to that direction such that if any two identical numbers are contained in that particular row (in case of moving left or right) or column (in case of moving up and down) they get add up and cell in that direction fill itself with that number and the rest cells goes empty again.
5. After this grid compression, any random cell gets itself with either 2 or 4.
6. Following the above process, we have to double the elements by adding up and make 2048 in any of the cell. 
7. If you managed to make 2048, you win the game. But if during the game there is no empty cell left to be filled with a new 2 or 4, the game is over.

Exit the Game
 1. Enter "3" in the menu bar to exit the game
 2. Enter "e" during the game, to go back to the menu bar 
     Then enter "3" in the menu bar to exit the game

Rules
1. There are 3 size of grid to choose, 3x3 grid size, 4x4 grid size, and 5x5 grid size.
2. In order to win, you have to reach the goal according to the difficulty that you have chosen (256 or 512 or 1024 or 2048) in one of the box.
3. The game could only be continued if there still an empty box to spawn a new number, or there are 2 same numbers side by side.
4. There are 4 keys to move, "W" to move up, "S" to move down, "A" to move left, and "D" to move right.
5. You cannot undo the moves you have made.
6. Try to win the game with the least move possible.

Best History
The best record (with the least move possible) of each different grid size will be shown with the players’ names
Grid Size    Username     Moves
3x3          None         None
4x4          Clarence     429
5x5          Hannah       517
