from simulation import life
from simulation import rules
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

class game():

    def setRule(self, rule):
        self.rule = rule
        
    def setGame(self, problem):
        self.prob = problem
        
    def game(self):
        if self.prob == 1:
            life(13,20,self.rule,rules[self.rule][0],rules[self.rule][1],animate=True)
        elif self.prob == 2:
            lif = life(300,500,rules[self.rule][0],rules[self.rule][1],animate=False)
            data1 = np.array(lif)
            data2 = np.array(lif)
            data3 = np.array(lif)
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
            
        
game = game()
    
game.setRule("Conway's Game of Life")
game.setGame(2)
game.game()
