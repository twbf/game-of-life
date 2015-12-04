#This is a simulation of the game of life

from random import *
import matplotlib.pyplot as plt
import numpy as np

def neighbors(data,i,j): #data is the list and position is in the form data[i[j]]
    neighbors = [data[i+1][j],data[i][j+1],data[i-1][j],data[i][j-1],data[i-1][j+1],data[i+1][j-1],data[i+1][j+1],data[i-1][j-1]]
    return sum(neighbors)

def newGrid(size,oldGrid):
    grid = oldGrid.copy()
    for n in range(1,size-1):
        for o in range(1,size-1):
            if grid[n][o] == 1:
                if neighbors(oldGrid,n,o)==3 or neighbors(oldGrid,n,o)==2:
                    grid[n][o] = 1
                else:
                    grid[n][o] = 0
            else:
                if neighbors(oldGrid,n,o)==3:
                    grid[n][o] = 1
    return grid

def randomGrid(size):
    #creating random number grid
    #np.random.seed(0)
    grid = np.zeros((size, size), dtype=bool)
    random = np.random.random((size-2, size-2))
    grid[1:size-1, 1:size-1] = (random > 0.9)
    #grid = [[round(random()) for i in range(size)] for j in range(size)]
    return grid

def life(size,times):
    grid = np.zeros((size, size), dtype=bool)
    grid[2:5,2:5] = np.array([[0,1,0],
                              [0,0,1],
                              [1,1,1]])
    grid = randomGrid(size)
    p = plt.imshow(grid,cmap='Greys',interpolation='nearest')
    fig = plt.gcf()
    plt.axis("off")
    plt.title("Life")
    print "a"
    for i in range(times-1):
        grid = newGrid(size,grid)
        p.set_data(grid)
        print "b"
        #print grid
        plt.pause(0.0001)

life(100,1000)

# notes:   use plt.savefig('foo.png')
