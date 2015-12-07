#This is a simulation of the game of life

from random import *
import matplotlib.pyplot as plt
import numpy as np

def neighbors(data,i,j): #data is the list and position is in the form data[i[j]]
    neighbors = [data[i+1][j],data[i][j+1],data[i-1][j],data[i][j-1],data[i-1][j+1],data[i+1][j-1],data[i+1][j+1],data[i-1][j-1]]
    return sum(neighbors)
    
def sumAlive(grid):
    return np.sum(grid)
    
def newGrid(size,oldGrid,aliveRules,deadRules):
    grid = oldGrid.copy()
    for n in range(1,size-1):
        for o in range(1,size-1):
            if grid[n][o] == 1:
                grid[n][o] = (neighbors(oldGrid,n,o) in aliveRules)
            else:
                if neighbors(oldGrid,n,o) in deadRules:
                    grid[n][o] = 1
    return grid

def randomGrid(size):
    #creating random number grid
    grid = np.zeros((size, size), dtype=bool)
    random = np.random.random((size-2, size-2))
    grid[1:size-1, 1:size-1] = (random > 0.85)
    return grid

def life(size,times,aliveRules=(2,3),deadRules=(3,),animate=True):#If thier are multiple values for aliveRules and deadRules you need to seperate them with a comma
    #grid = np.zeros((size, size), dtype=bool)
    #grid[2:5,2:5] = np.array([[0,1,0],
    #                          [0,0,1],
     #                         [1,1,1]])
    grid = randomGrid(size)
    if animate==True:
        p = plt.imshow(grid,cmap='Greys',interpolation='nearest')
        fig = plt.gcf()
        plt.axis("off")
        plt.title("Game of Life")
    alive = [sumAlive(grid)]
    for i in range(times):
        grid = newGrid(size,grid,aliveRules,deadRules)
        if animate==True:p.set_data(grid)
        alive.append(sumAlive(grid))
        plt.pause(0.00000001)
        print i
    return alive
       # plt.savefig('project'+str(i+2)+'.png')

rules = {"Conway's Game of Life":[(2,3),(3,)],
         'Rule 1':[(2,3),(2,3)],
         'Rule 2':[(1,2),(1,)],
         'Rule 3':[(3,4),(4,)],
         'Rule 4':[(5,6),(6,)],
         'Rule 5':[(2,3,4,5),(3,4,5)],
         'Rule 6':[(4,5,6,7),(5,6,7)]}

# notes:   use plt.savefig('foo.png')
