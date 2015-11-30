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

def steps(size,times):
    #creating random number grid
    grid = np.array([[round(random()) for i in range(size)] for j in range(size)])
    print grid
    #applying rules to grid
    for m in range(times):
        grid=newGrid(size,grid)
    return grid

def life():
    plt.axis('off')
    plt.imshow(steps(10,10),cmap='Greys',  interpolation='nearest')
    plt.show()

    
life()
