from simulation import life
from simulation import rules
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

def p1(rule):
    data1 = np.array(life(300,500,rules[rule][0],rules[rule][1],animate=False))
    data2 = np.array(life(300,500,rules[rule][0],rules[rule][1],animate=False))
    data3 = np.array(life(300,500,rules[rule][0],rules[rule][1],animate=False))
    plt.figure()
    plt.plot(data1,label='Test 1')
    plt.plot(data2, label='Test 2')
    plt.plot(data3, label='Test 3')
    plt.xlabel('Steps')
    plt.ylabel('Alive Cells')
    plt.title(rule)
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.savefig(rule+'-graph.png',dpi=1000)

def p2(rule):
    life(7,9,rule,rules[rule][0],rules[rule][1],animate=True,save=False)
    
p2("Conway's Game of Life")
