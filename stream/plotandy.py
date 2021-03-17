import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

from matplotlib.collections import LineCollection

Y, X = np.mgrid[0:300, 0:300]

U = [[]for i in range(300)]
V = [[]for i in range(300)]
counter = 0;

u = open('C:\\Users\\yoyob\\Documents\\stream\\u.dat',"r")

for line in u:
    if counter < 90000:
        #data = line.split("\\")[0]

        index = math.floor(counter/300);
        #print(index)
        
        U[index].append(float(line))
        counter = counter+1
        
counter = 0;

u.close()
v = open('C:\\Users\\yoyob\\Documents\\stream\\v.dat',"r")

for line in v:
    if counter < 90000:
        #data = line.split("\\")[0]

        index = math.floor(counter/300);
        #print(index)
        
        V[index].append(float(line))
        counter = counter+1

v.close()

U = np.array(U);
V = np.array(V);


fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

#Streamline Graph
ax0 = fig.add_subplot(gs[0, 1])
strm = ax0.streamplot(X, Y, U, V, color=U*10, linewidth=2, cmap='autumn')
fig.colorbar(strm.lines)
ax0.set_title('Data')   

segs = strm.lines.get_segments()

thingggg = LineCollection(segs,
                               linewidths=(10),
                               linestyles='solid')

N = 300
x = np.arange(N)
# Here are many sets of y to plot vs. x
ys = [x + i for i in x]

print(np.max(x))

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))
ax.add_collection(thingggg)
ax.set_title('Line collection with masked arrays')
ax.autoscale()
ax.margins(0.1)

'''out = open("segments.dat", "w")

for line in range(len(segs)):
    out.write("(" + str(segs[line][0][0]) + "," + str(segs[line][0][1]) + "),(" + str(segs[line][1][0]) + "," + str(segs[line][1][1]) + ")\n")
'''
plt.tight_layout()
plt.show()



