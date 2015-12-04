import matplotlib.pyplot as plt
import numpy as np

x = np.arange(9)
y = np.arange(5)
z = x * y[:, np.newaxis]

for i in range(5):
    if i == 0:
        p = plt.imshow(z)
        fig = plt.gcf()
        plt.clim()   # clamp the color limits
        plt.title("Boring slide show")
        print z

    else:
        z = z * 2
        p.set_data(z)


    print("step", i)
    plt.pause(0.5)
