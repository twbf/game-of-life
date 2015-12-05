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
    grid[1:size-1, 1:size-1] = (random > 0.8)
    return grid

def life(size,times,aliveRules=(2,3),deadRules=(3,)):#If thier are multiple values for aliveRules and deadRules you need to seperate them with a comma
    #grid = np.zeros((size, size), dtype=bool)
    #grid[2:5,2:5] = np.array([[0,1,0],
    #                          [0,0,1],
     #                         [1,1,1]])
    grid = randomGrid(size)
    p = plt.imshow(grid,cmap='Greys',interpolation='nearest')
    fig = plt.gcf()
    plt.axis("off")
    plt.title("Game of Life")
   # plt.savefig('project1.png')
    print sumAlive(grid)
    for i in range(times-1):
        grid = newGrid(size,grid,aliveRules,deadRules)
        p.set_data(grid)
        print sumAlive(grid)
        #print grid
        plt.pause(0.000001)
       # plt.savefig('project'+str(i+2)+'.png')

rules = {'regular':[(2,3),(3,)], 'decrease':[(1,2),(1,)], 'increased':[(3,4),(4,)],' massive increase':[(5,6),(6,)], 'wideRange':[(2,3,4,5),(3,4,5)], 'upper-wideRange':[(4,5,6,7),(5,6,7)]}
life(400,100,rules['regular'][0],rules['regular'][1])

# notes:   use plt.savefig('foo.png')
