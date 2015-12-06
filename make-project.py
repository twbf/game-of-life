from simulation import life 
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

data=np.array(life(20,100))
sio.savemat('out.txt', {'data':data})

#f = file('out.txt', 'w')
#f.write()
#f.close()

#file = open('out.txt', 'r')


#plt.plot(int(file.read()))

#plt.xlabel('time (s)')
#plt.ylabel('voltage (mV)')
#plt.title('About as simple as it gets, folks')
#plt.grid(True)
#plt.savefig("test.png")
#plt.show()

