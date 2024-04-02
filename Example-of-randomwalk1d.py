import numpy as np
import matplotlib.pyplot as plt 

def randomwalk(n):
    x = 0 
    y = 0 
    xposition = [0]
    yposition = [0]

    for i in range(1,n+1):
        step = np.random.uniform(0,1)

        if step < 0.5:
            x += 1
            y += 1
        else:
            x += 1 
            y += -1
        xposition.append(x)
        yposition.append(y)

    return [xposition,yposition]


steps = 1000
Randwalk = randomwalk(steps)
Randwalk = np.array(Randwalk)

msd = np.zeros(1001)
pos = 0.
for i,j in enumerate(Randwalk[1][:]):
    pos = pos + np.sqrt(j*j)
    msd[i] = pos 
print(msd/steps)


plt.figure()
plt.plot(Randwalk[0],Randwalk[1],'r-', label = "Randwalk1D")
plt.legend(loc="best")
plt.figure()
plt.plot(Randwalk[0][:],msd,'r-', label = "msd")
plt.legend(loc="best")

plt.show()