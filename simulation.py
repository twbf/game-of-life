#This is a simulation of the game of life

from random import *
import matplotlib.pyplot as plt
import numpy as np

def neighbors(data,i,j): #data is the list and position is in the form data[i[j]]
    neighbors = [data[i+1][j],data[i][j+1],data[i-1][j],data[i][j-1],data[i-1][j+1],data[i+1][j-1],data[i+1][j+1],data[i-1][j-1]]
    return sum(neighbors)
    
def sumAlive(grid):
    return np.sum(grid)
    
def newGrid(size,oldGrid):
    grid = oldGrid.copy()
    for n in range(1,size-1):
        for o in range(1,size-1):
            if grid[n][o] == 1:
                if neighbors(oldGrid,n,o) in (2,3):
                    grid[n][o] = 1
                else:
                    grid[n][o] = 0
            else:
                if neighbors(oldGrid,n,o)==3:
                    grid[n][o] = 1
    return grid

def randomGrid(size):
    #creating random number grid
    grid = np.zeros((size, size), dtype=bool)
    random = np.random.random((size-2, size-2))
    grid[1:size-1, 1:size-1] = (random > 0.8)
    return grid

def life(size,times,):
    grid = np.zeros((size, size), dtype=bool)
    grid[2:5,2:5] = np.array([[0,1,0],
                              [0,0,1],
                              [1,1,1]])
    grid = randomGrid(size)
    p = plt.imshow(grid,cmap='Greys',interpolation='nearest')
    fig = plt.gcf()
    plt.axis("off")
    plt.title("Game of Life")
   # plt.savefig('project1.png')
    print sumAlive(grid)
    print "a"
    for i in range(times-1):
        grid = newGrid(size,grid)
        p.set_data(grid)
        print "b"
        print sumAlive(grid)
        #print grid
        plt.pause(0.000001)
       # plt.savefig('project'+str(i+2)+'.png')

life(100,1000)

# notes:   use plt.savefig('foo.png')
