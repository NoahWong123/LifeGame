from random import seed
from random import randint
#variables
cols = 4
rows = 5
board_state = [[0 for i in range(rows)] for j in range(cols)]

#functions
def print_state(cols, rows):
   board_state = [[0 for i in range(rows)] for j in range(cols)]
   temp = [randint(0,1) for i in range(rows * cols)]
   for y in range(cols):
      for x in range(rows):
         board_state[y][x] = temp[x+(y * cols)]
   return(board_state)
   
def render(board_state):
   for y in board_state:
      for x in y:
         if x == 0:
            print(" ",end ='')
         else:
            print("X",end = '')
      print('')

#start
seed(1)
print(board_state)
board_state = print_state(cols, rows)
print(board_state)
render(board_state)
print("done")