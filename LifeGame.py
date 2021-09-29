#imports
from random import seed
from random import randint
#variables
cols = 3
rows = 4
boardState = [[0 for i in range(rows)] for j in range(cols)]

#function takes in int rows and columns and returns a 2d array with ether 1 or 0
def print_state(cols, rows):
   #create 2d array with apropriate rows and columns
   boardState = [[0 for i in range(rows)] for j in range(cols)]
   temp = [randint(0,1) for i in range(rows * cols)]
   for y in range(cols):
      for x in range(rows):
         boardState[y][x] = temp[x+(y * cols)]
   return(boardState)

#function takes in a 2d array and prints it to terminal with a " " if 0 or a "X" if 1
def render(boardState):
   for y in boardState:
      for x in y:
         if x == 0:
            print(" ",end ='')
         else:
            print("X",end = '')
      print('')
      
#function that takes in a 2d array and returns the next 2d array based on 4 rules:
#1. Any live cell with a 0 or 1 live neighbors becomes dead
#2. Any live cell with 2 or 3 live neighbors stays alive
#3. Any live cell with more then 3 live neighbors becomes dead
#4. Ant dead cell with exactly 3 live neighbors becomes alive
def next_board_state(boardState):
   nextBoardState = [[0 for i in range(rows)] for j in range(cols)]
   xSize = len(boardState[0]) - 1
   ySize = len(boardState) - 1
   for y in range(cols):
      for x in range(rows):
         #calculate how many cells are alive near current cell
         near = 0
         for j in range(3):
            for i in range(3):
               if y + j - 1 <= ySize and x + i - 1 <= xSize:
                  if y + j - 1 >= 0 and x + i - 1 >= 0:
                     near += boardState[y + j - 1][x + i - 1]
         #subtract board state because previoesly added in loop
         near - boardState[y][x]
         if boardState[y][x] == 0:
            if near == 3:
               nextBoardState[y][x] = 1
         if boardState[y][x] == 1:
            if near >= 2 and near <= 3:
               nextBoardState[y][x] = 1
   return(nextBoardState)

#start
seed(1)
boardState = print_state(cols, rows)
render(boardState)
boardState = next_board_state(boardState)
render(boardState)
print("done")