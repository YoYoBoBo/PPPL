import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math

from matplotlib.collections import LineCollection

'''
Importing data and creating the streamplot/histogram
'''

#creates a 300x300 grid
Y, X = np.mgrid[0:300, 0:300]

#sets up 2D arrays for U and V components
U = [[]for i in range(300)]
V = [[]for i in range(300)]
counter = 0; #to keep track of the index within the array

#import u.dat
u = open('u.dat',"r")
for line in u:
    if counter < 90000:
        index = math.floor(counter/300);
        #print(index)
        
        U[index].append(float(line))
        counter = counter+1
        
counter = 0;
u.close()

#import v.dat
v = open('v.dat',"r")
for line in v:
    if counter < 90000:
        index = math.floor(counter/300);
        #print(index)
        
        V[index].append(float(line))
        counter = counter+1

v.close()

#converts into numpy arrays
U = np.array(U);
V = np.array(V);
speedTemp = np.sqrt(U**2 + V**2) #calculate magnitude of vector at each point
        
#Streamline Graph
scale = 10
fig, ax0 = plt.subplots()
ax0.margins(0.1)
strm = ax0.streamplot(X, Y, U, V, linewidth=speedTemp*scale)
ax0.set_title('Streamline Graph')
ax0.autoscale()
ax0.margins(0.1)

#to make a 1D array of the magnitudes for the histogram
spd=[]
for i in range(len(speedTemp)):
    for j in range(len(speedTemp[0])):
        spd.append(speedTemp[i][j])

#Histogram
fig, ax1 = plt.subplots()
#ax1.set_xlim(0,1)
ax1.hist(spd, bins = 10)
plt.yscale('log')

'''
Exporting streamplot data
'''

#export line segment vertices
segs = strm.lines.get_segments()
out = open("vertices.txt", "w")
for line in range(len(segs)):
    #formatted as '(0,1),(2,3)' each line, each line is a line segment
    out.write("(" + str(segs[line][0][0]) + "," + str(segs[line][0][1]) + "),(" + str(segs[line][1][0]) + "," + str(segs[line][1][1]) + ")\n")
out.close()

#export line widths of each segment
lwTemp = strm.lines.get_linewidths()
out = open("lw.txt", "w")
for line in range(len(lwTemp)):
    out.write(str(lwTemp[line]/scale)+"\n") #divides by scale to get original magnitudes
out.close()

'''
Recreating streamplot with the exported data
'''

#importing the vertices
l = open("vertices.txt", "r")
ls = [] #list of line segment vertices
for line in l:
    #changes line to '0,1,2,3'
    line = line.replace('(','').replace(')','')

    #makes a list [0,1,2,3]
    nums = line.split(',')

    #converts to float and stores nums in tuples (0,1) (2,3)
    start = (float(nums[0]),float(nums[1]))
    end = (float(nums[2]),float(nums[3]))

    ls.append([start, end])
l.close()

lws = [] #list of line width for each segment
f_lw = open("lw.txt", "r")
for line in f_lw:
    lws.append(float(line))
f_lw.close()

lws = np.array(lws)

#creates linecollection for plotting
lc = LineCollection(ls, linewidth=lws*scale) #scale = 10

fig, ax = plt.subplots()

ax.add_collection(lc)
ax.set_title('Reproduced Streamplot')
ax.autoscale()

plt.show()



