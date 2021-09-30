#imports
from random import seed
from random import randint
from time import sleep
#variables
cols = 10
rows = 15
boardState = [[0 for i in range(rows)] for j in range(cols)]

#function takes in int rows and columns and returns a 2d array with ether 1 or 0
def randome_state(cols, rows):
   #create 2d array with apropriate rows and columns
   boardState = [[0 for i in range(rows)] for j in range(cols)]
   temp = [randint(0,1) for i in range(rows * cols)]
   for y in range(cols):
      for x in range(rows):
         boardState[y][x] = temp[x+(y * rows)]
   return(boardState)

#function takes in a 2d array and prints it to terminal with a " " if 0 or a "X" if 1
def render(boardState):
   xSize = len(boardState[0]) - 1
   for i in range(xSize + 1):
      print("-", end = '')
   print("")
   for y in boardState:
      for x in y:
         if x == 0:
            print(" ",end ='')
         else:
            print("X",end = '')
      print('')
   for i in range(xSize + 1):
      print("-", end = '')
   print("")
      
#function that takes in a 2d array and returns the next 2d array based on 4 rules:
#1. Any live cell with a 0 or 1 live neighbors becomes dead
#2. Any live cell with 2 or 3 live neighbors stays alive
#3. Any live cell with more then 3 live neighbors becomes dead
#4. Ant dead cell with exactly 3 live neighbors becomes alive
def next_board_state(boardState):
   xSize = len(boardState[0]) - 1
   ySize = len(boardState) - 1
   nextBoardState = [[0 for i in range(xSize + 1)] for j in range(ySize + 1)]
   for y in range(ySize + 1):
      for x in range(xSize + 1):
         #calculate how many cells are alive near current cell
         near = 0
         for j in range(3):
            for i in range(3):
               if y + j - 1 <= ySize and x + i - 1 <= xSize:
                  if y + j - 1 >= 0 and x + i - 1 >= 0:
                     near += boardState[y + j - 1][x + i - 1]
         #subtract board state because previoesly added in loop
         near -= boardState[y][x]
         if boardState[y][x] == 0:
            if near == 3:
               nextBoardState[y][x] = 1
         if boardState[y][x] == 1:
            if near >= 2 and near <= 3:
               nextBoardState[y][x] = 1
   return(nextBoardState)

#function takes in string with filename and returns a 2d array containing it
def open_board_state(fileName):
   xSize = 0
   ySize = 0
   stringBoard = ""
   with open(fileName, 'r') as f:
      for line in f:
         line = line.strip()
         ySize += 1
         xSize = len(line)
         stringBoard += line
   boardState = [[0 for i in range(xSize)] for j in range(ySize)]
   for y in range(ySize):
      for x in range(xSize):
         boardState[y][x] = ord(stringBoard[x+(y * xSize)]) - 48
         
   print(xSize, "  ", ySize, "  ", len(stringBoard))
   return(boardState)

#function to infinitely print next state to terminal with 1 second delay
def inf_board_state(boardState):
   while(True):
      render(boardState)
      boardState = next_board_state(boardState)
      sleep(0.25)

#start
seed(1)
boardState = open_board_state("gosperGliderGun.txt")
render(boardState)
inf_board_state(boardState)
print("done")