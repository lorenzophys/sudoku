#Screen
WIDTH = 600
HEIGHT = 600
FPS = 10

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (255,192,203)

#Example board from wikipedia.it, too slow to solve, not good for animation
BOARD = [[5,6,0,8,4,7,0,0,0],
         [3,0,9,0,0,0,6,0,0],
         [0,0,8,0,0,0,0,0,0],
         [0,1,0,0,8,0,0,4,0],
         [7,9,0,6,0,2,0,1,8],
         [0,5,0,0,3,0,0,9,0],
         [0,0,0,0,0,0,2,0,0],
         [0,0,6,0,0,0,8,0,7],
         [0,0,0,3,1,6,0,5,9]] 

#For animation, FPS=10 good
BOARD_ANIM = [[5,0,1,0,4,7,0,2,3],
              [3,7,0,0,2,0,6,0,0],
              [0,0,0,0,6,3,0,7,0],
              [0,1,3,0,0,9,0,4,0],
              [7,9,0,6,0,0,3,0,8],
              [0,5,0,1,0,4,0,0,0],
              [9,0,5,0,7,0,2,6,0],
              [0,4,0,2,9,0,0,3,7],
              [2,8,0,0,0,6,4,0,9]] 

#Others
OFFSET = 20
TILE = (WIDTH-2*OFFSET)/9