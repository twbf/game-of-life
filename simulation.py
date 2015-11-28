#This is a simulation of the game of life

from random import *
import matplotlib.pyplot as plt
import numpy as np

def life():
    #creating random number grid
    def randomGrid (size):
        grid = [[round(random()) for i in range(size)] for j in range(size)]
               
        return grid

    plt.imshow(randomGrid(1000))
    plt.figure(dpi=500)
    plt.show()
   
life()
