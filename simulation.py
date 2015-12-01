#This is a simulation of the game of life

from random import *
import matplotlib.pyplot as plt
import numpy as np

def neighbors(data,i,j): #data is the list and position is in the form data[i[j]]
    neighbors = [data[i+1][j],data[i][j+1],data[i-1][j],data[i][j-1],data[i-1][j+1],data[i+1][j-1],data[i+1][j+1],data[i-1][j-1]]
    return sum(neighbors)

def newGrid(size,oldGrid):
    grid=oldGrid.copy()
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
    np.random.seed(0)
    grid = np.zeros((size, size), dtype=bool)
    random = np.random.random((size-2, size-2))
    grid[1:size-1, 1:size-1] = (random > 0.5)

def steps(size,times):
    
    #grid=np.array([[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,1,1,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
    #applying rules to grid
    for m in range(times):
        grid=newGrid(size,grid)
        sumAlive = sum(sum(grid))
        print sumAlive
    return grid

def life(size,times):
    for i in range(times):
        if i == 0:
            p = plt.imshow(grid)
            fig = plt.gcf()
            plt.clim()   # clamp the color limits
            plt.title("Boring slide show")
        else:
            z = z + 2
            p.set_data(z)

        print("step", i)
        plt.pause(0.5)
    plt.axis('off')
    plt.imshow(steps(size,times),cmap='Greys',  interpolation='nearest')
    plt.show()

    
life(100,1000)
