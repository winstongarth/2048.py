#imports
import random 
import os
import time
from termcolor import colored as c


#functions
def title():
   print("--------------------------------")
   print(c("██████╗", 'yellow') + "  █████╗  " + c(" ██╗██╗", 'yellow') + " █████╗")
   print(c("╚════██╗", 'yellow') + "██╔══██╗ " + c("██╔╝██║", 'yellow') + "██╔══██╗")
   print(c("  ███╔═╝", 'yellow') + "██║  ██║" + c("██╔╝ ██║", 'yellow') + "╚█████╔╝")
   print(c("██╔══╝  ", 'yellow') + "██║  ██║" + c("███████║", 'yellow') + "██╔══██╗")
   print(c("███████╗", 'yellow') + "╚█████╔╝" + c("╚════██║", 'yellow') + "╚█████╔╝")
   print(c("╚══════╝", 'yellow') + " ╚════╝ " + c("    ╚═╝ ", 'yellow') + " ╚════╝ ")
   print("--------------------------------")

def addNewBlock(board, size): #add new block 
   x = random.randint(0, size-1)
   y = random.randint(0, size-1)

   while (board[x][y] != 0): #rechoose if cell already taken
      x = random.randint(0, size-1)
      y = random.randint(0, size-1)
   
   possiblity = [2, 4]
   board[x][y] = random.choice(possiblity)


   
def checkWin(board, difficulty, size):
   if difficulty == "1":
      goal = 256
   elif difficulty == "2":
      goal = 512
   elif difficulty == "3":
      goal = 1024
   elif difficulty == "4":
      goal = 2048
   for i in range(size):
      for ii in range(size):
         if board[i][ii] == goal:
            return True
   else:
      return False
      


def checkGameOver(board, size):
   for i in range(size):
      for ii in range(size):
         if board[i][ii] == 0:
            return False

   for i in range(size-1):
      for ii in range(size-1):
         if board[i][ii] == board[i][ii+1] or board[i][ii] == board[i+1][ii]:
            return False

   for i in range(size-1):
      if board[i][size-1] == board[i+1][size-1]:
         return False
   for i in range(size-1):
      if board[size-1][i] == board[size-1][i+1]:
         return False

   return True
   
   



def game(board, size):
   board =[[0]*size for i in range(size)]
   prevboard = []
   while True:
      print("Choose Difficulty: ")
      print("1. " + c('Easy:', 'blue') + " Reach " + c('256', 'blue') +  " to win")
      print("2. " + c('Medium:', 'green') + " Reach " + c('512', 'green') + " to win")
      print("3. " + c('Hard:', 'yellow') + " Reach " + c('1024', 'yellow') + " to win")
      print("4. " + c('Original:', 'red') + " Reach " + c('2048', 'red') + " to win")
      difficulty = input("Choose game difficulty (1-4): ")
      if difficulty == "e":
         return
      elif difficulty not in [str(i) for i in range(1, 5)]:
         _ = input("Please input the number 1-4..")
      else:
         break
   os.system('clear')
   addNewBlock(board, size)
   addNewBlock(board, size) #starts with 2 block innitially
   printBoard(board, size)
   while True:
      breakout = False
      
      move = input("Move (W, A, S, D): ")
      if move.lower() == "a":
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #compress to the left
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): # add value 
            for x in range(size-1):
               if board[y][x] != 0 and board[y][x] == board[y][x+1]:
                  board[y][x] += board[y][x+1]
                  board[y][x+1] = 0
         for y in range(size): #compress again
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         for i in range(size):
            for ii in range(size):
               if board[i][ii] == 0 and board != prevboard:# check if there is empty space and if the move is valid(move is valid if it changed the board's position)
                  addNewBlock(board, size)
                  breakout = True
                  break
            if breakout:
               break
         breakout = False

      elif move.lower() == "d":
         for i in board: #reverse vertically
            i.reverse()
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #move to the left
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size):
            for x in range(size-1):
               if board[y][x] != 0 and board[y][x] == board[y][x+1]:
                  board[y][x] += board[y][x+1]
                  board[y][x+1] = 0
         for y in range(size):
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         for i in board: #revert the reversed board
            i.reverse()
         for i in range(size):
            for ii in range(size):
               if board[i][ii] == 0 and board != prevboard:# check if there is empty space and if the move is valid(move is valid if it changed the board's position)
                  addNewBlock(board, size)
                  breakout = True
                  break
            if breakout:
               break
         breakout = False
         

      elif move.lower() == "w":
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): # transpose the board x=y y=x
            for x in range(size):
               temporaryBoard[y][x] = board[x][y]
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #move to the left
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size):
            for x in range(size-1):
               if board[y][x] != 0 and board[y][x] == board[y][x+1]:
                  board[y][x] += board[y][x+1]
                  board[y][x+1] = 0
         for y in range(size):
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #revert transposed board to original
            for x in range(size):
               temporaryBoard[y][x] = board[x][y]
         board = temporaryBoard
         for i in range(size):
            for ii in range(size):
               if board[i][ii] == 0 and board != prevboard:# check if there is empty space and if the move is valid(move is valid if it changed the board's position)
                  addNewBlock(board, size)
                  breakout = True
                  break
            if breakout:
               break
         breakout = False
         
      elif move.lower() == "s":
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #transpose
            for x in range(size):
               temporaryBoard[y][x] = board[x][y]
         board = temporaryBoard
         for i in board: #reverse
            i.reverse()
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #move to the left
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size):
            for x in range(size-1):
               if board[y][x] != 0 and board[y][x] == board[y][x+1]:
                  board[y][x] += board[y][x+1]
                  board[y][x+1] = 0
         for y in range(size): 
            position = 0
            for x in range(size):
               if board[y][x] != 0:
                  temporaryBoard[y][position] = board[y][x]
                  position += 1
         board = temporaryBoard
         for i in board: #reverse back to original
            i.reverse()
         temporaryBoard = [[0]*size for i in range(size)]
         for y in range(size): #transpose back to original
            for x in range(size):
               temporaryBoard[y][x] = board[x][y]
         board = temporaryBoard
         for i in range(size):
            for ii in range(size):
               if board[i][ii] == 0 and board != prevboard:# check if there is empty space and if the move is valid(move is valid if it changed the board's position)
                  addNewBlock(board, size)
                  breakout = True
                  break
            if breakout:
               break
         breakout = False
         
      elif move.lower() == "e":
         return
      else:
         _ = input("Please input W, A, S or D to pick a move.")

      os.system('clear')
      printBoard(board, size)
      prevboard = board #store previous board data
      if checkWin(board, difficulty, size):
         print(c("██╗   ██╗", 'yellow') + ' █████╗ ' + c('██╗   ██╗', 'yellow') + '   ██╗       ██╗' + c('██╗', 'yellow') + '███╗  ██╗' + c("██╗", 'yellow'))
         print(c("╚██╗ ██╔╝", 'yellow') + '██╔══██╗' + c('██╗   ██╗', 'yellow') + '   ██║  ██╗  ██║' + c('██║', 'yellow') + '████╗ ██║' + c("██║", 'yellow'))
         print(c(" ╚████╔╝ ", 'yellow') + '██╔══██╗' + c('██╗   ██╗', 'yellow') + '   ╚██╗████╗██╔╝' + c('██║', 'yellow') + '██╔██╗██║' + c("██║", 'yellow'))
         print(c("  ╚██╔╝  ", 'yellow') + '██║  ██║' + c('██╗   ██╗', 'yellow') + '    ████╔═████║ ' + c('██║', 'yellow') + '██║╚████║' + c("╚═╝", 'yellow'))
         print(c("   ██║   ", 'yellow') + '╚█████╔╝' + c('╚██████╔╝', 'yellow') + '    ╚██╔╝ ╚██╔╝ ' + c('██║', 'yellow') + '██║ ╚███║' + c("██╗", 'yellow'))
         print(c("   ╚═╝   ", 'yellow') + ' ╚════╝ ' + c(' ╚═════╝ ', 'yellow') + '     ╚═╝   ╚═╝  ' + c('╚═╝', 'yellow') + '╚═╝  ╚══╝' + c("╚═╝", 'yellow'))
         _ = input("Well done! Thank you for playing :)")
         exit()
      if checkGameOver(board, size):
         print(c(' ██████╗', 'yellow') + '  █████╗ ' + c('███╗   ███╗', 'yellow') + '███████╗' + c('   █████╗', 'yellow') + ' ██╗   ██╗' + c('███████╗', 'yellow') + '██████╗ ')
         print(c('██╔════╝', 'yellow') + ' ██╔══██╗' + c('████╗ ████║', 'yellow') + '██╔════╝' + c('  ██╔══██╗', 'yellow') + '██║   ██║' + c('██╔════╝', 'yellow') + '██╔══██╗ ')
         print(c('██║  ██╗', 'yellow') + ' ███████║' + c('██╔████╔██║', 'yellow') + '█████╗  ' + c('  ██║  ██║', 'yellow') + '╚██╗ ██╔╝' + c('█████╗  ', 'yellow') + '██████╔╝')
         print(c('██║  ╚██╗', 'yellow') + '██╔══██║' + c('██║╚██╔╝██║', 'yellow') + '██╔══╝  ' + c('  ██║  ██║', 'yellow') + ' ╚████╔╝ ' + c('██╔══╝  ', 'yellow') + '██╔══██╗')
         print(c('╚██████╔╝', 'yellow') + '██║  ██║' + c('██║ ╚═╝ ██║', 'yellow') + '███████╗' + c('  ╚█████╔╝', 'yellow') + '  ╚██╔╝  ' + c('███████╗', 'yellow') + '██║  ██║')
         print(c(' ╚═════╝ ', 'yellow') + '╚═╝  ╚═╝' + c('╚═╝     ╚═╝', 'yellow') + '╚══════╝' + c('   ╚════╝ ', 'yellow') + '   ╚═╝   ' + c('╚══════╝', 'yellow') + '╚═╝  ╚═╝')

         _ = input("Thank you for playing! try again next time :)")
         exit()
      
      




def printBoard(board, size):
   if size == 5:
      print('┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓')
      print ('┃%5s┃%5s┃%5s┃%5s┃%5s┃' %(board[0][0] if board[0][0] != 0 else " ",board[0][1] if board[0][1] != 0 else " ",board[0][2] if board[0][2] != 0 else " ",board[0][3] if board[0][3] != 0 else " ", board[0][4] if board[0][4] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃%5s┃' %(board[1][0] if board[1][0] != 0 else " ",board[1][1] if board[1][1] != 0 else " ",board[1][2] if board[1][2] != 0 else " ",board[1][3] if board[1][3] != 0 else " ", board[1][4] if board[1][4] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃%5s┃' %(board[2][0] if board[2][0] != 0 else " ",board[2][1] if board[2][1] != 0 else " ",board[2][2] if board[2][2] != 0 else " ",board[2][3] if board[2][3] != 0 else " ", board[2][4] if board[2][4] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃%5s┃' %(board[3][0] if board[3][0] != 0 else " ",board[3][1] if board[3][1] != 0 else " ",board[3][2] if board[3][2] != 0 else " ",board[3][3] if board[3][3] != 0 else " ", board[3][4] if board[3][4] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃%5s┃' %(board[4][0] if board[4][0] != 0 else " ",board[4][1] if board[4][1] != 0 else " ",board[4][2] if board[4][2] != 0 else " ",board[4][3] if board[4][3] != 0 else " ", board[4][4] if board[4][4] != 0 else " "))
      print("┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛")
   elif size ==4:
      print('┏━━━━━┳━━━━━┳━━━━━┳━━━━━┓')
      print ('┃%5s┃%5s┃%5s┃%5s┃' %(board[0][0] if board[0][0] != 0 else " ",board[0][1] if board[0][1] != 0 else " ",board[0][2] if board[0][2] != 0 else " ",board[0][3] if board[0][3] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃' %(board[1][0] if board[1][0] != 0 else " ",board[1][1] if board[1][1] != 0 else " ",board[1][2] if board[1][2] != 0 else " ",board[1][3] if board[1][3] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃' %(board[2][0] if board[2][0] != 0 else " ",board[2][1] if board[2][1] != 0 else " ",board[2][2] if board[2][2] != 0 else " ",board[2][3] if board[2][3] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃%5s┃' %(board[3][0] if board[3][0] != 0 else " ",board[3][1] if board[3][1] != 0 else " ",board[3][2] if board[3][2] != 0 else " ",board[3][3] if board[3][3] != 0 else " "))
      print("┗━━━━━┻━━━━━┻━━━━━┻━━━━━┛")
   elif size ==3:
      print('┏━━━━━┳━━━━━┳━━━━━┓')
      print ('┃%5s┃%5s┃%5s┃' %(board[0][0] if board[0][0] != 0 else " ",board[0][1] if board[0][1] != 0 else " ",board[0][2] if board[0][2] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃' %(board[1][0] if board[1][0] != 0 else " ",board[1][1] if board[1][1] != 0 else " ",board[1][2] if board[1][2] != 0 else " "))
      print("┣━━━━━╋━━━━━╋━━━━━┫")
      print ('┃%5s┃%5s┃%5s┃' %(board[2][0] if board[2][0] != 0 else " ",board[2][1] if board[2][1] != 0 else " ",board[2][2] if board[2][2] != 0 else " "))
      print("┗━━━━━┻━━━━━┻━━━━━┛")

def chooseMode():  
   while True: 
      size = 0    
      board = []
      os.system('clear')
      title()
      print("1. 3x3 Grid")
      print("2. 4x4 Grid")
      print('3. 5x5 Grid')
      print("4. Back")
      mode = input("Choose game mode (1-4): ")
      if mode == '1':
         size =3
         game(board, size)
      elif mode == '2':
         size =4
         game(board, size)
      elif mode == '3':
         size = 5
         game(board, size)
      elif mode == '4':
         os.system("clear")
         return
      else:
         print(("Please choose 1, 2, or 3"))



#intro
print("-----------" + c("Welcome to", 'yellow') + "-----------")
print(c("██████╗", 'yellow') + "  █████╗  " + c(" ██╗██╗", 'yellow') + " █████╗")
print(c("╚════██╗", 'yellow') + "██╔══██╗ " + c("██╔╝██║", 'yellow') + "██╔══██╗")
print(c("  ███╔═╝", 'yellow') + "██║  ██║" + c("██╔╝ ██║", 'yellow') + "╚█████╔╝")
print(c("██╔══╝  ", 'yellow') + "██║  ██║" + c("███████║", 'yellow') + "██╔══██╗")
print(c("███████╗", 'yellow') + "╚█████╔╝" + c("╚════██║", 'yellow') + "╚█████╔╝")
print(c("╚══════╝", 'yellow') + " ╚════╝ " + c("    ╚═╝ ", 'yellow') + " ╚════╝ ")
print("--------------------------------")
time.sleep(1)
_ = input("Press " + c("ENTER", 'yellow') + " to continue!")

#loading simulation
loading = 0
while loading <= 100:
   os.system("clear")
   print (f'Loading: {loading}%')
   loading += 10
   time.sleep(0.2)
print("Complete!")
time.sleep(1)
os.system('clear')

#main loop
while True:
   title()
   print("1. Game Instruction")
   print("2. " + c('P', 'red') + c('l', 'green') + c('a', 'yellow') + c('y', 'blue'))
   print("3. Exit")
   choose = input("Choose (1-3): ")

   if choose == '1':
      os.system('clear')
      print("""1. There are 3 choices of grid; 3*3 grid, 4*4 grid, and 5x5 grid.
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

2. There are 4 choices of difficulty mode; easy, medium, hard and original.  
3. The grid can be filled with any number. Initially two random cells are filled with either 2 or 4 in it. The rest of the cells are empty.
4. When you see “Move (W, A, S, D):”
 - Enter "W" to move the number up.
 - Enter "A" to move the number left.
 - Enter "S" to move the number down.
 - Enter "D" to move the number right.
5. When you press any key, all the elements of the cell move to that direction such that if any two identical numbers are contained in that particular row (in case of moving left or right) or column (in case of moving up and down) they get add up and cell in that direction fill itself with that number and the rest cells goes empty again.
6. After this grid compression, any random cell gets itself with either 2 or 4.
7. Following the above process, we have to double the elements by adding up and make the target of the difficulty mode in any of the cell.
8. If you managed to meet the target of the game, you win the game. But if during the game there is no empty cell left to be filled with a new 2 or 4, the game is over.
""")
      _ = input("Press ENTER to continue!")
   elif choose == '2':
      chooseMode()
      continue
   elif choose == '3':
      print("Thank you for playing!")
      exit()
   else:
      print("Please choose 1, 2, or 3")
   os.system('clear')